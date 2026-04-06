def calculate_reward(action: str, task: dict):
    reward = 0.0

    correct_action = task.get("correct_action")
    difficulty = task.get("difficulty", "easy")

    # ✅ PERFECT match
    if action == correct_action:
        reward += 1.0

    # ⚠️ PARTIAL LOGIC (smart scoring)
    elif task["type"] == "security_issue" and action == "report_bug":
        reward += 0.8
    elif task["type"] == "performance_issue" and action == "improve_code":
        reward += 0.8
    elif action == "approve":
        reward += 0.3

    # 🔥 Difficulty bonus
    if difficulty == "hard":
        reward += 0.5
    elif difficulty == "medium":
        reward += 0.2

    return reward