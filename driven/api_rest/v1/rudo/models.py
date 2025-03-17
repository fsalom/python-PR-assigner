from typing import List

from pydantic import BaseModel


class UserRudoResponse(BaseModel):
    email: str
    name: str
    slack_id: str

    class Config:
        from_attributes = True


class UsersRudoResponse(BaseModel):
    values: List[UserRudoResponse]