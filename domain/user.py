from pydantic import BaseModel


class User(BaseModel):
    name: str
    email: str = None
    bitbucket_id: str
