# env/data.py

DATA = [

    # ---------------- TASK 1: BUG DETECTION ---------------- #
    {
        "task": "bug_detection",
        "code": "if x = 5:",
        "type": "syntax_error",
        "difficulty": "easy",
        "correct_action": "report_bug"
    },

    {
        "task": "bug_detection",
        "code": "a = 5\nb == 10\nprint(a + b)",
        "type": "logic_error",
        "difficulty": "medium",
        "correct_action": "report_bug"
    },

    {
        "task": "bug_detection",
        "code": "password = '12345'",
        "type": "security_issue",
        "difficulty": "hard",
        "correct_action": "report_bug"
    },

    {
        "task": "bug_detection",
        "code": "eval(user_input)",
        "type": "security_issue",
        "difficulty": "hard",
        "correct_action": "report_bug"
    },

    {
        "task": "bug_detection",
        "code": "eval(input())",
        "type": "security_issue",
        "difficulty": "hard",
        "correct_action": "report_bug"
    },

    # ---------------- TASK 2: PERFORMANCE REVIEW ---------------- #
    {
        "task": "performance_review",
        "code": "for i in range(len(arr)):\n    print(arr[i])",
        "type": "performance_issue",
        "difficulty": "medium",
        "correct_action": "improve_code"
    },

    {
        "task": "performance_review",
        "code": "for i in range(len(arr)): print(arr[i])",
        "type": "performance_issue",
        "difficulty": "medium",
        "correct_action": "improve_code"
    },

    # ---------------- TASK 3: CLEAN CODE APPROVAL ---------------- #
    {
        "task": "clean_code_approval",
        "code": "print('Hello World')",
        "type": "clean",
        "difficulty": "easy",
        "correct_action": "approve"
    },

    {
        "task": "clean_code_approval",
        "code": "if x == 5:\n    print(x)",
        "type": "clean",
        "difficulty": "easy",
        "correct_action": "approve"
    }

]