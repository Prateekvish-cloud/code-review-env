SCORE_MIN = 0.02
SCORE_MAX = 0.98


def squash_score(raw: float) -> float:
    raw = max(0.0, min(1.0, raw))
    return SCORE_MIN + raw * (SCORE_MAX - SCORE_MIN)


def grade_bug_detection(trajectory: dict = None, action: str = "", history=None) -> float:
    if action == "report_bug":
        raw = 1.0
    elif action == "improve_code":
        raw = 0.5
    else:
        raw = 0.0
    return squash_score(raw)


def grade_performance_review(trajectory: dict = None, action: str = "", history=None) -> float:
    if action == "improve_code":
        raw = 1.0
    elif action == "report_bug":
        raw = 0.5
    else:
        raw = 0.0
    return squash_score(raw)


def grade_clean_code_approval(trajectory: dict = None, action: str = "", history=None) -> float:
    if action == "approve":
        raw = 1.0
    elif action == "improve_code":
        raw = 0.4
    else:
        raw = 0.0
    return squash_score(raw)


GRADERS = {
    "bug_detection": grade_bug_detection,
    "performance_review": grade_performance_review,
    "clean_code_approval": grade_clean_code_approval,
}