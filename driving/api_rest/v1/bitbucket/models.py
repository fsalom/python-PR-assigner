from typing import Literal, Optional, Dict

from pydantic import BaseModel, HttpUrl


class BranchResponse(BaseModel):
    name: str


class PullRequestLinksResponse(BaseModel):
    self: Dict[str, HttpUrl]
    html: Dict[str, HttpUrl]


class UserDrivingResponse(BaseModel):
    display_name: str
    type: str
    uuid: str
    account_id: str
    nickname: str


class PullRequestResponse(BaseModel):
    id: int
    title: str
    description: Optional[str]
    state: str
    author: UserDrivingResponse
    source: Dict[str, BranchResponse]
    destination: Dict[str, BranchResponse]
    links: PullRequestLinksResponse


class RepositoryResponse(BaseModel):
    name: str
    full_name: str
    uuid: str
    links: Dict[str, Dict[str, HttpUrl]]


class ActorResponse(BaseModel):
    display_name: str
    uuid: str
    nickname: Optional[str]


class WebhookPayloadResponse(BaseModel):
    actor: ActorResponse
    repository: RepositoryResponse
    pullrequest: PullRequestResponse
    event: str
