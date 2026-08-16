from abc import ABC, abstractmethod


class BaseAgent(ABC):
    name: str = "base"

    @abstractmethod
    async def run(self, task: dict) -> dict:
        raise NotImplementedError
