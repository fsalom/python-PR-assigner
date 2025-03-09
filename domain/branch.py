from pydantic import BaseModel


class Branch(BaseModel):
    name: str
