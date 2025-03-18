from datetime import datetime, timedelta
from typing import Callable, List
from logging import Logger

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from application.ports.driven.pull_request_repository_port import PullRequestRepositoryPort
from domain.pull_request import PullRequest
from domain.user import User
from driven.db.pr_per_user.mapper import DBPullRequestMapper
from driven.db.pr_per_user.models import PullRequestPerUserMO


class PullRequestRepositoryAdapter(PullRequestRepositoryPort):
    def __init__(self,
                 sqlalchemy_repository: Callable[[], AsyncSession],
                 db_pull_request_mapper: DBPullRequestMapper,
                 logger: Logger):
        self.sqlalchemy_repository = sqlalchemy_repository
        self.db_pull_request_mapper = db_pull_request_mapper
        self.logger = logger

    async def save(self, pull_request: PullRequest, user: User):
        example_mo = self.db_pull_request_mapper.to_model(pull_request)
        try:
            self.sqlalchemy_repository.add(example_mo)
            await self.sqlalchemy_repository.commit()
        except Exception as e:
            self.logger.error(str(e))

        return self.db_pull_request_mapper.from_model_decorator(example_mo)

    async def get_prs_for_user(self, user: User) -> List[PullRequest]:
        try:
            result = await self.sqlalchemy_repository.execute(
                select(PullRequestPerUserMO).where(PullRequestPerUserMO.email == user.email)
            )
            prs_models = result.scalars().all()
        except Exception as e:
            self.logger.error(str(e))

        return self.db_pull_request_mapper.from_models(prs_models)

    async def get_prs_last_days(self, days: int) -> List[PullRequest]:
        try:
            date_limit = datetime.utcnow() - timedelta(days=days)

            result = await self.sqlalchemy_repository.execute(
                select(PullRequestPerUserMO).where(PullRequestPerUserMO.created_at >= date_limit)
            )
            prs_models = result.scalars().all()

        except Exception as e:
            self.logger.error(f"Error en get_prs_last_days: {str(e)}")
            return []

        return self.db_pull_request_mapper.from_models(prs_models)
