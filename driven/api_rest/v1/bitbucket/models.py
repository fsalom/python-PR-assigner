from typing import Optional, List

from pydantic import BaseModel, HttpUrl


class OAUTH2Response(BaseModel):
    access_token: str
    token_type: str
    expires_in: int
    scopes: Optional[str] = None

    class Config:
        from_attributes = True


class UserResponse(BaseModel):
    display_name: str
    type: str
    uuid: str
    account_id: str
    nickname: str


class WorkspaceMembershipResponse(BaseModel):
    user: UserResponse


class BitbucketResponse(BaseModel):
    values: List[WorkspaceMembershipResponse]
    pagelen: int
    size: int
    page: int
    next: Optional[HttpUrl] = None
