from typing import Optional
from pydantic import BaseModel
from domain.user import User


class PullRequest(BaseModel):
    id: int
    title: str
    description: Optional[str]
    state: str
    author: User
