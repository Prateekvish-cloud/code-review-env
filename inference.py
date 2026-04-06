import asyncio
from typing import List
import os

from openai import OpenAI

from env.environment import CodeReviewEnv
from env.models import CodeAction

MAX_STEPS = 5

# Initialize OpenAI client
client = OpenAI(
    api_key=os.getenv("API_KEY")
)

# ---------------- LOG FUNCTIONS ---------------- #

def log_start():
    print("[START] task=code-review env=custom model=hybrid-ai-reviewer", flush=True)

def log_step(step, action, reward, done):
    print(
        f"[STEP] step={step} action={action} reward={reward:.2f} done={str(done).lower()} error=null",
        flush=True
    )

def log_end(success, steps, rewards):
    rewards_str = ",".join(f"{r:.2f}" for r in rewards)

    # 🔥 Normalize score between 0 and 1
    max_possible_reward = 2.0 * steps if steps > 0 else 1.0
    score = sum(rewards) / max_possible_reward
    score = min(max(score, 0.0), 1.0)

    print(
        f"[END] success={str(success).lower()} steps={steps} score={score:.2f} rewards={rewards_str}",
        flush=True
    )

# ---------------- RULE-BASED POLICY ---------------- #

def simple_policy(code: str):
    code = code.lower()

    # 🔐 Security issues
    if "eval(" in code or "input(" in code:
        return "report_bug"
    if "password" in code:
        return "report_bug"

    # 🐞 Syntax / logic issues
    if " = " in code and "==" not in code:
        return "report_bug"
    if "==" in code and "print" not in code:
        return "improve_code"

    # ⚡ Performance issues
    if "range(len(" in code:
        return "improve_code"

    # ✅ Clean code
    return "approve"

# ---------------- AI POLICY ---------------- #

def ai_policy(code: str):
    try:
        prompt = f"""
        You are a professional code reviewer.

        Analyze the following code and choose ONE action:
        - report_bug
        - improve_code
        - approve

        Code:
        {code}

        Reply with ONLY one word: report_bug / improve_code / approve
        """

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}],
            temperature=0
        )

        action = response.choices[0].message.content.strip().lower()

        if action in ["report_bug", "improve_code", "approve"]:
            return action

        return None

    except Exception:
        
        return None

# ---------------- MAIN FUNCTION ---------------- #

async def main():
    env = await CodeReviewEnv.from_docker_image(None)

    rewards: List[float] = []
    steps = 0

    log_start()

    try:
        result = await env.reset()

        for step in range(1, MAX_STEPS + 1):
            code = result.observation.code

            # 🔥 HYBRID DECISION
            action_str = ai_policy(code)

            if not action_str:
                action_str = simple_policy(code)

            action = CodeAction(action=action_str)

            result = await env.step(action)

            reward = result.reward or 0.0
            done = result.done

            rewards.append(reward)
            steps = step

            log_step(step, action_str, reward, done)

            if done:
                break

        success = sum(rewards) > 1.5

    finally:
        try:
            await env.close()
        except Exception:
            pass

        log_end(success, steps, rewards)

# ---------------- RUN ---------------- #

if __name__ == "__main__":
    asyncio.run(main())