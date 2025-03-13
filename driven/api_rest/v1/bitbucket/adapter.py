from base64 import b64encode
from typing import List

import httpx
from fastapi import HTTPException

from application.ports.driven.bitbucket_repository_port import BitbucketRepositoryPort
from domain.user import User
from driven.api_rest.v1.bitbucket.mapper import BitbucketMapper
from driven.api_rest.v1.bitbucket.models import BitbucketResponse
from driven.api_rest.v1.slack.models import OAUTH2Response


class BitbucketRepositoryAdapter(BitbucketRepositoryPort):
    BITBUCKET_URL_WORKSPACE = "https://api.bitbucket.org/2.0/workspaces"
    BITBUCKET_URL = "https://bitbucket.org/site/oauth2/access_token"
    CLIENT_ID = "hZVH5esUUkaRyxQKbz"
    CLIENT_SECRET = "wsakSb9UX5wkGbNkcNxMbBCRjjc5kV4D"
    WORKSPACE = "rudoapps"

    def __init__(self, mapper: BitbucketMapper):
        self.mapper = mapper

    async def get_access_token(self) -> str:
        credentials = f"{self.CLIENT_ID}:{self.CLIENT_SECRET}"
        encoded_credentials = b64encode(credentials.encode()).decode()

        headers = {
            "Authorization": f"Basic {encoded_credentials}",
            "Content-Type": "application/x-www-form-urlencoded"
        }

        data = {"grant_type": "client_credentials"}

        async with httpx.AsyncClient() as client:
            response = await client.post(self.BITBUCKET_URL, headers=headers, data=data)
            response.raise_for_status()

            tokens = OAUTH2Response(**response.json())
            return tokens.access_token

    async def fetch_workspace_members(self) -> List[User]:
        url = f"{self.BITBUCKET_URL_WORKSPACE}/{self.WORKSPACE}/members"
        headers = {
            "Authorization": f"Bearer {self.get_access_token()}",
            "Accept": "application/json",
        }

        users = []

        async with httpx.AsyncClient() as client:
            while url:
                response = await client.get(url, headers=headers)

                if response.status_code != 200:
                    raise HTTPException(status_code=response.status_code, detail=response.json())

                data = BitbucketResponse.parse_raw(response.text)
                users.extend([membership.user for membership in data.values])

                url = data.next

        return [self.mapper.to_user_domain(user) for user in users]
