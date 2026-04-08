from dataclasses import dataclass

@dataclass
class CodeAction:
    action: str

@dataclass
class CodeObservation:
    task: str        # 🔥 NEW FIELD (VERY IMPORTANT)
    code: str
    difficulty: str
    hint: str

@dataclass
class StepResult:
    observation: CodeObservation
    reward: float
    done: bool