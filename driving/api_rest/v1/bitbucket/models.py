from typing import Literal, Optional, Dict

from pydantic import BaseModel, HttpUrl


class BranchRequest(BaseModel):
    name: str


class PullRequestLinksRequest(BaseModel):
    self: Dict[str, HttpUrl]
    html: Dict[str, HttpUrl]


class UserDrivingRequest(BaseModel):
    display_name: str
    type: str
    uuid: str
    account_id: str
    nickname: str


class PullRequestRequest(BaseModel):
    id: int
    title: str
    description: Optional[str]
    state: str
    author: UserDrivingRequest
    source: Dict[str, BranchRequest]
    destination: Dict[str, BranchRequest]
    links: PullRequestLinksRequest


class RepositoryRequest(BaseModel):
    name: str
    full_name: str
    uuid: str
    links: Dict[str, Dict[str, HttpUrl]]


class ActorRequest(BaseModel):
    display_name: str
    uuid: str
    nickname: Optional[str]


class WebhookPayloadRequest(BaseModel):
    actor: ActorRequest
    repository: RepositoryRequest
    pullrequest: PullRequestRequest
    event: str
