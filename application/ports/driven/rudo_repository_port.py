from abc import ABC, abstractmethod
from typing import List

from domain.user import User


class RudoRepositoryPort(ABC):
    @abstractmethod
    async def get_users_for_tech(self, tech) -> List[User]:
        pass
