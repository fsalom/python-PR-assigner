from domain.webhook_payload import WebhookPayload


class BitbucketDTOMapper:

    @staticmethod
    def to_domain() -> WebhookPayload:
        return WebhookPayload()
