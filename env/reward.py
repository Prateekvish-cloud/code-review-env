def calculate_reward(action: str, task: dict) -> float:
    reward = 0.0

    correct_action = task.get("correct_action")
    difficulty = task.get("difficulty", "easy")

    # Full credit for exact correct action
    if action == correct_action:
        reward = 1.0

    # Partial credit for near-correct actions
    elif correct_action == "report_bug" and action == "improve_code":
        reward = 0.4
    elif correct_action == "improve_code" and action == "report_bug":
        reward = 0.4
    elif correct_action == "approve" and action == "improve_code":
        reward = 0.2
    elif action == "approve":
        reward = 0.1
    else:
        reward = 0.0

    # Small difficulty bonus, but keep score bounded
    if reward > 0:
        if difficulty == "hard":
            reward += 0.0
        elif difficulty == "medium":
            reward += 0.0

    return min(max(reward, 0.0), 1.0)