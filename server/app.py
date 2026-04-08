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

    if expected is None:
        return {
            "score": 0.0,
            "task": payload.task,
            "expected_action": None,
            "received_action": payload.action,
            "reason": "unknown task",
        }

    score = 1.0 if payload.action == expected else 0.0

    return {
        "score": score,
        "task": payload.task,
        "expected_action": expected,
        "received_action": payload.action,
        "reason": "correct" if score == 1.0 else "incorrect",
    }


def main():
    uvicorn.run(app, host="0.0.0.0", port=7860)


if __name__ == "__main__":
    main()