SCORE_MIN = 0.02
SCORE_MAX = 0.98


def squash_score(raw: float) -> float:
    raw = max(0.0, min(1.0, raw))
    return SCORE_MIN + raw * (SCORE_MAX - SCORE_MIN)


def grade_bug_detection(state: dict | None = None, action: str = "", history=None) -> tuple[float, dict]:
    expected = "report_bug"

    if action == expected:
        raw = 1.0
        reason = "correct bug detection"
    elif action == "improve_code":
        raw = 0.5
        reason = "partially correct, found an issue but chose optimization"
    elif action == "approve":
        raw = 0.0
        reason = "missed the bug"
    else:
        raw = 0.0
        reason = "invalid action"

    return squash_score(raw), {"task": "bug_detection", "reason": reason}


def grade_performance_review(state: dict | None = None, action: str = "", history=None) -> tuple[float, dict]:
    expected = "improve_code"

    if action == expected:
        raw = 1.0
        reason = "correct performance review"
    elif action == "report_bug":
        raw = 0.5
        reason = "identified a problem but wrong category"
    elif action == "approve":
        raw = 0.0
        reason = "missed performance issue"
    else:
        raw = 0.0
        reason = "invalid action"

    return squash_score(raw), {"task": "performance_review", "reason": reason}


def grade_clean_code_approval(state: dict | None = None, action: str = "", history=None) -> tuple[float, dict]:
    expected = "approve"

    if action == expected:
        raw = 1.0
        reason = "correct approval"
    elif action == "improve_code":
        raw = 0.4
        reason = "overly cautious but still non-destructive"
    elif action == "report_bug":
        raw = 0.0
        reason = "false bug report"
    else:
        raw = 0.0
        reason = "invalid action"

    return squash_score(raw), {"task": "clean_code_approval", "reason": reason}


GRADERS = {
    "bug_detection": grade_bug_detection,
    "performance_review": grade_performance_review,
    "clean_code_approval": grade_clean_code_approval,
}