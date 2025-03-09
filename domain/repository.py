from typing import Dict

from pydantic import BaseModel, HttpUrl


class Repository(BaseModel):
    name: str
    full_name: str
    uuid: str
    links: Dict[str, Dict[str, HttpUrl]]
