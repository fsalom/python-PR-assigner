from abc import ABC, abstractmethod


class SlackRepositoryPort(ABC):
    @abstractmethod
    async def notify(self, user, message):
        pass
