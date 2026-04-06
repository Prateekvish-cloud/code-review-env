import random
from .models import CodeObservation, StepResult
from .data import DATA
from .reward import calculate_reward

class CodeReviewEnv:

    def __init__(self):
        self.current = None
        self.steps = 0
        self.max_steps = 5

    @classmethod
    async def from_docker_image(cls, image_name: str):
        return cls()

    async def reset(self):
        self.current = random.choice(DATA)
        self.steps = 0

        return StepResult(
            observation=CodeObservation(
                code=self.current["code"],
                difficulty=self.current["difficulty"],
                hint="Analyze the code"
            ),
            reward=0.0,
            done=False
        )

    async def step(self, action):
        self.steps += 1

        reward = calculate_reward(
            action.action,
            self.current
        )

        done = self.steps >= self.max_steps

        self.current = random.choice(DATA)

        return StepResult(
            observation=CodeObservation(
                code=self.current["code"],
                difficulty=self.current["difficulty"],
                hint="Analyze the code"
            ),
            reward=reward,
            done=done
        )

    async def close(self):
        pass