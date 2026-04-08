import asyncio
import os
from typing import List, Optional

from openai import OpenAI

from env.environment import CodeReviewEnv
from env.models import CodeAction

IMAGE_NAME = os.getenv("IMAGE_NAME")
API_KEY = os.getenv("HF_TOKEN") or os.getenv("API_KEY")
API_BASE_URL = os.getenv("API_BASE_URL") or "https://router.huggingface.co/v1"
MODEL_NAME = os.getenv("MODEL_NAME") or "Qwen/Qwen2.5-72B-Instruct"

TASK_NAME = os.getenv("TASK_NAME", "code-review")
BENCHMARK = os.getenv("BENCHMARK", "code-review-env")

MAX_STEPS = 5
SUCCESS_SCORE_THRESHOLD = 0.1

client: Optional[OpenAI] = None
if API_KEY:
    client = OpenAI(base_url=API_BASE_URL, api_key=API_KEY)


def log_start(task: str, env: str, model: str) -> None:
    print(f"[START] task={task} env={env} model={model}", flush=True)


def log_step(step: int, action: str, reward: float, done: bool, error: Optional[str]) -> None:
    error_val = error if error else "null"
    done_val = str(done).lower()
    print(
        f"[STEP] step={step} action={action} reward={reward:.2f} done={done_val} error={error_val}",
        flush=True,
    )


def log_end(success: bool, steps: int, score: float, rewards: List[float]) -> None:
    rewards_str = ",".join(f"{r:.2f}" for r in rewards)
    print(
        f"[END] success={str(success).lower()} steps={steps} score={score:.2f} rewards={rewards_str}",
        flush=True,
    )


def simple_policy(code: str) -> str:
    code = code.lower()

    if "eval(" in code or "input(" in code:
        return "report_bug"
    if "password" in code:
        return "report_bug"

    if " = " in code and "==" not in code:
        return "report_bug"

    if "range(len(" in code:
        return "improve_code"

    return "approve"


def ai_policy(code: str) -> Optional[str]:
    if client is None:
        return None

    try:
        prompt = f"""
You are a professional code reviewer.

Analyze the following code and choose exactly one action:
- report_bug
- improve_code
- approve

Code:
{code}

Reply with only one word: report_bug or improve_code or approve
""".strip()

        response = client.chat.completions.create(
            model=MODEL_NAME,
            messages=[{"role": "user", "content": prompt}],
            temperature=0,
            max_tokens=10,
        )

        action = (response.choices[0].message.content or "").strip().lower()

        if action in ["report_bug", "improve_code", "approve"]:
            return action

        return None

    except Exception:
        return None


async def main() -> None:
    env = await CodeReviewEnv.from_docker_image(IMAGE_NAME)

    rewards: List[float] = []
    steps_taken = 0
    success = False
    score = 0.0

    log_start(task=TASK_NAME, env=BENCHMARK, model=MODEL_NAME)

    try:
        result = await env.reset()

        for step in range(1, MAX_STEPS + 1):
            if result.done:
                break

            code = result.observation.code

            action_str = ai_policy(code)
            if not action_str:
                action_str = simple_policy(code)

            result = await env.step(CodeAction(action=action_str))

            reward = result.reward or 0.0
            done = result.done
            error = None

            rewards.append(reward)
            steps_taken = step

            log_step(
                step=step,
                action=action_str,
                reward=reward,
                done=done,
                error=error,
            )

            if done:
                break

        max_total_reward = float(MAX_STEPS)
        score = sum(rewards) / max_total_reward if max_total_reward > 0 else 0.0
        score = min(max(score, 0.0), 1.0)
        success = score >= SUCCESS_SCORE_THRESHOLD

    finally:
        try:
            await env.close()
        except Exception:
            pass

        log_end(success=success, steps=steps_taken, score=score, rewards=rewards)


if __name__ == "__main__":
    asyncio.run(main())