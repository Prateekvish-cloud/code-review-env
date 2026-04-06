from dataclasses import dataclass

@dataclass
class CodeAction:
    action: str

@dataclass
class CodeObservation:
    code: str
    difficulty: str
    hint: str

@dataclass
class StepResult:
    observation: CodeObservation
    reward: float
    done: bool