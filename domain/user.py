from pydantic import BaseModel


class User(BaseModel):
    name: str
    email: str = None
    slack_id: str = None
    bitbucket_id: str = None
