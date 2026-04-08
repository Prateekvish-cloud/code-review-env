def calculate_reward(action: str, task: dict) -> float:
    reward = 0.1  # default minimum (never 0)

    correct_action = task.get("correct_action")
    difficulty = task.get("difficulty", "easy")

    # Full credit for exact correct action (NOT 1.0)
    if action == correct_action:
        reward = 0.9

    # Partial credit for near-correct actions
    elif correct_action == "report_bug" and action == "improve_code":
        reward = 0.5
    elif correct_action == "improve_code" and action == "report_bug":
        reward = 0.5
    elif correct_action == "approve" and action == "improve_code":
        reward = 0.3
    elif action == "approve":
        reward = 0.2
    else:
        reward = 0.1  # ensure never 0

    # Keep reward strictly between (0,1)
    reward = min(max(reward, 0.1), 0.9)

    return reward