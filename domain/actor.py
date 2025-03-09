from pydantic import BaseModel, HttpUrl
from typing import Optional, Dict


class Actor(BaseModel):
    display_name: str
    uuid: str
    nickname: Optional[str]
    links: Dict[str, Dict[str, HttpUrl]]

