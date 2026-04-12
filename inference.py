import asyncio
import os
from typing import List, Optional

from openai import OpenAI

from env.data import DATA
from env.models import CodeAction

IMAGE_NAME = os.getenv("IMAGE_NAME")
API_KEY = os.getenv("HF_TOKEN") or os.getenv("API_KEY")
API_BASE_URL = os.getenv("API_BASE_URL") or "https://router.huggingface.co/v1"
MODEL_NAME = os.getenv("MODEL_NAME") or "Qwen/Qwen2.5-72B-Instruct"

BENCHMARK = os.getenv("BENCHMARK", "code-review-env")

client: Optional[OpenAI] = None
if API_KEY:
    client = OpenAI(base_url=API_BASE_URL, api_key=API_KEY)

TASK_ORDER = [
    "bug_detection",
    "performance_review",
    "clean_code_approval",
]


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
    if "range(len(" in code or "result +=" in code:
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


def calculate_reward(action: str, correct_action: str) -> float:
    if action == correct_action:
        return 0.9

    if correct_action == "report_bug" and action == "improve_code":
        return 0.5
    if correct_action == "improve_code" and action == "report_bug":
        return 0.5
    if correct_action == "approve" and action == "improve_code":
        return 0.3

    return 0.1


async def run_task(task_name: str) -> None:
    task_examples = [item for item in DATA if item["task"] == task_name]

    rewards: List[float] = []
    steps_taken = 0

    log_start(task=task_name, env=BENCHMARK, model=MODEL_NAME)

    for step, sample in enumerate(task_examples, start=1):
        code = sample["code"]

        action_str = ai_policy(code)
        if not action_str:
            action_str = simple_policy(code)

        reward = calculate_reward(action_str, sample["correct_action"])
        rewards.append(reward)
        steps_taken = step

        done = step == len(task_examples)

        log_step(
            step=step,
            action=action_str,
            reward=reward,
            done=done,
            error=None,
        )

    score = sum(rewards) / len(rewards) if rewards else 0.1
    score = min(max(score, 0.1), 0.9)
    success = score >= 0.5

    log_end(success=success, steps=steps_taken, score=score, rewards=rewards)


async def main() -> None:
    for task_name in TASK_ORDER:
        await run_task(task_name)


if __name__ == "__main__":
    asyncio.run(main())