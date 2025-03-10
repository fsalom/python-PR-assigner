from typing import List

from application.ports.driving.bitbucket_service_port import BitbucketServicePort
from domain.webhook_payload import WebhookPayload


class BitbucketServices(BitbucketServicePort):
    def __init__(self):
        pass

    async def assign(self, payload: WebhookPayload) -> [User]:
        pass
