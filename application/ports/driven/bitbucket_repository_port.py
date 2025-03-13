from abc import ABC, abstractmethod
from typing import List

from domain.user import User


class BitbucketRepositoryPort(ABC):
    @abstractmethod
    async def fetch_workspace_members(self) -> List[User]:
        pass
