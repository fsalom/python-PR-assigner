import os
from typing import List

import httpx

from application.ports.driven.rudo_repository_port import RudoRepositoryPort
from domain.user import User
from driven.api_rest.v1.rudo.mapper import RudoMapper
from driven.api_rest.v1.rudo.models import UsersRudoResponse


class RudoRepositoryAdapter(RudoRepositoryPort):
    API_KEY = os.environ.get("RUDO_API_KEY")

    def __init__(self, mapper: RudoMapper):
        self.mapper = mapper

    async def get_users_for_tech(self, tech) -> List[User]:
        headers = {
            "Authorization": f"{self.API_KEY}",
            "Content-Type": "application/x-www-form-urlencoded"
        }

        users = []

        async with httpx.AsyncClient() as client:
            response = await client.get("", headers=headers)
            response.raise_for_status()

            data = UsersRudoResponse(**response.json())
            users.extend([membership.user for membership in data.values])

            return users
