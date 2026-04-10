# env/data.py

DATA = [

    # ---------------- TASK 1: BUG DETECTION ---------------- #
    {
        "task": "bug_detection",
        "code": "if x = 5:",
        "type": "syntax_error",
        "difficulty": "easy",
        "correct_action": "report_bug"
    }

    # ---------------- TASK 2: PERFORMANCE REVIEW ---------------- #
    {
        "task": "performance_review",
        "code": "for i in range(len(arr)):\n    print(arr[i])",
        "type": "performance_issue",
        "difficulty": "easy",
        "correct_action": "improve_code"
    }
    # ---------------- TASK 3: CLEAN CODE APPROVAL ---------------- #
    {
        "task": "clean_code_approval",
        "code": "print('Hello World')",
        "type": "clean",
        "difficulty": "easy",
        "correct_action": "approve"
    }

]