from dependency_injector.wiring import inject
from fastapi import APIRouter
from starlette.responses import JSONResponse

from application.ports.driven.slack_repository_port import SlackRepositoryPort

slack_router = APIRouter()


class SlackRepositoryAdapter(SlackRepositoryPort):
    async def notify(self, user, message):
        pass
