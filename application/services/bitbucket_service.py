from application.ports.driven.pull_request_repository_port import PullRequestRepositoryPort
from application.ports.driving.bitbucket_service_port import BitbucketServicePort
from domain.pull_request import PullRequest
from domain.repository import Repository
from domain.user import User
from collections import defaultdict
from typing import List, Dict


class BitbucketServices(BitbucketServicePort):
    def __init__(self, db_repository: PullRequestRepositoryPort):
        self.db_repository = db_repository

    async def assign(self, pull_request: PullRequest) -> [User]:
        pass

    async def get_least_assigned_users(self, users: List[str], days: int = 7) -> List[str]:
        """
        Encuentra los 2 usuarios con menos PRs asignadas en los últimos `days` días.

        :param users: Lista de emails de los usuarios disponibles.
        :param days: Número de días a considerar para el balanceo de asignación.
        :return: Lista con los 2 usuarios con menos PRs asignadas.
        """

        recent_prs = await self.db_repository.get_prs_last_days(days)
        pr_counts: Dict[str, int] = defaultdict(int)

        for pr in recent_prs:
            pr_counts[pr.assigned_to_email] += 1

        user_pr_counts = {user: pr_counts.get(user, 0) for user in users}
        sorted_users = sorted(user_pr_counts.keys(), key=lambda user: user_pr_counts[user])
        return sorted_users[:2]