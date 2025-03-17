from abc import ABC, abstractmethod
from typing import List

from domain.pull_request import PullRequest
from domain.user import User


class PullRequestRepositoryPort(ABC):
    @abstractmethod
    async def get_prs_for_user(self, user: User) -> List[PullRequest]:
        pass

    @abstractmethod
    async def get_prs_last_days(self, days: int) -> List[PullRequest]:
        pass

    @abstractmethod
    async def save(self, pull_request: PullRequest, user: User):
        pass