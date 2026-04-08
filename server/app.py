from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn

app = FastAPI()


class GraderRequest(BaseModel):
    task: str
    action: str


TASK_EXPECTED_ACTIONS = {
    "bug_detection": "report_bug",
    "performance_review": "improve_code",
    "clean_code_approval": "approve",
}


@app.get("/")
def read_root():
    return {"status": "ok", "message": "Code Review Env is running"}


@app.get("/health")
def health():
    return {"status": "healthy"}


@app.post("/reset")
def reset():
    return {"status": "ok"}


@app.post("/grader")
def grader(payload: GraderRequest):
    expected = TASK_EXPECTED_ACTIONS.get(payload.task)

    # Unknown task → small non-zero score
    if expected is None:
        return {
            "score": 0.1,
            "task": payload.task,
            "expected_action": None,
            "received_action": payload.action,
            "reason": "unknown task",
        }

    # ✅ FIX: score must be strictly between 0 and 1
    if payload.action == expected:
        score = 0.9
        reason = "correct"
    else:
        score = 0.1
        reason = "incorrect"

    return {
        "score": score,
        "task": payload.task,
        "expected_action": expected,
        "received_action": payload.action,
        "reason": reason,
    }


def main():
    uvicorn.run(app, host="0.0.0.0", port=7860)


if __name__ == "__main__":
    main()