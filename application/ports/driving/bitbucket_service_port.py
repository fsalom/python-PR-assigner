from abc import ABC, abstractmethod

from domain.actor import User
from domain.webhook_payload import WebhookPayload


class BitbucketServicePort(ABC):
    @abstractmethod
    async def assign(self, payload: WebhookPayload) -> [User]:
        pass
