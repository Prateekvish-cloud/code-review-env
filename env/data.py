# env/data.py

DATA = [

    # SYNTAX BUG
    {
        "code": "if x = 5:",
        "type": "syntax_error",
        "difficulty": "easy",
        "correct_action": "report_bug"
    },

    # OGIC BUG
    {
        "code": "a = 5\nb == 10\nprint(a + b)",
        "type": "logic_error",
        "difficulty": "medium",
        "correct_action": "report_bug"
    },

    # SECURITY ISSUE - PASSWORD
    {
        "code": "password = '12345'",
        "type": "security_issue",
        "difficulty": "hard",
        "correct_action": "report_bug"
    },

    # SECURITY ISSUE - EVAL
    {
        "code": "eval(user_input)",
        "type": "security_issue",
        "difficulty": "hard",
        "correct_action": "report_bug"
    },

    # SECURITY ISSUE - INPUT EXECUTION
    {
        "code": "eval(input())",
        "type": "security_issue",
        "difficulty": "hard",
        "correct_action": "report_bug"
    },

    # PERFORMANCE ISSUE - LOOP
    {
        "code": "for i in range(len(arr)):\n    print(arr[i])",
        "type": "performance_issue",
        "difficulty": "medium",
        "correct_action": "improve_code"
    },

    # PERFORMANCE ISSUE - INLINE LOOP
    {
        "code": "for i in range(len(arr)): print(arr[i])",
        "type": "performance_issue",
        "difficulty": "medium",
        "correct_action": "improve_code"
    },

    # CLEAN CODE
    {
        "code": "print('Hello World')",
        "type": "clean",
        "difficulty": "easy",
        "correct_action": "approve"
    },

    # CLEAN CONDITION
    {
        "code": "if x == 5:\n    print(x)",
        "type": "clean",
        "difficulty": "easy",
        "correct_action": "approve"
    }

]