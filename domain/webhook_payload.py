from pydantic import BaseModel

from domain.pull_request import PullRequest
from domain.repository import Repository


class WebhookPayload(BaseModel):
    repository: Repository
    pull_request: PullRequest
    event: str
