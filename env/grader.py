SCORE_FLOOR = 0.02
SCORE_CEIL = 0.98


def _squish(raw: float) -> float:
    raw = max(0.0, min(1.0, raw))
    return SCORE_FLOOR + raw * (SCORE_CEIL - SCORE_FLOOR)


def grade_bug_detection(task_input: dict, action: str) -> float:
    expected = "report_bug"
    raw = 1.0 if action == expected else 0.0
    return _squish(raw)


def grade_performance_review(task_input: dict, action: str) -> float:
    expected = "improve_code"
    raw = 1.0 if action == expected else 0.0
    return _squish(raw)


def grade_clean_code_approval(task_input: dict, action: str) -> float:
    expected = "approve"
    raw = 1.0 if action == expected else 0.0
    return _squish(raw)


GRADERS = {
    "bug_detection": grade_bug_detection,
    "performance_review": grade_performance_review,
    "clean_code_approval": grade_clean_code_approval,
}