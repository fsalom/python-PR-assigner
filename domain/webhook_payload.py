from pydantic import BaseModel

from domain.actor import Actor
from domain.pull_request import PullRequest
from domain.repository import Repository


class WebhookPayload(BaseModel):
    actor: Actor
    repository: Repository
    pullrequest: PullRequest
    event: str
