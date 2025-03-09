from typing import Dict, Optional

from pydantic import BaseModel, HttpUrl

from domain.branch import Branch
from domain.actor import User


class PullRequestLinks(BaseModel):
    self: Dict[str, HttpUrl]
    html: Dict[str, HttpUrl]


class PullRequest(BaseModel):
    id: int
    title: str
    description: Optional[str]
    state: str
    author: User
    source: Dict[str, Branch]
    destination: Dict[str, Branch]
    links: PullRequestLinks
