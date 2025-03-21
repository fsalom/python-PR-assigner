from domain.pull_request import PullRequest
from domain.repository import Repository
from domain.user import User
from domain.webhook_payload import WebhookPayload
from driving.api_rest.v1.bitbucket.models import WebhookPayloadRequest


class BitbucketDTOMapper:

    @staticmethod
    def to_domain(payload: WebhookPayloadRequest) -> WebhookPayload:
        repository = Repository(
            name=payload.repository.name,
            full_name=payload.repository.full_name,
            uuid=payload.repository.uuid,
            links=payload.repository.links,
        )
        pull_request = PullRequest(id=payload.pullrequest.id,
                                   title=payload.pullrequest.title,
                                   description=payload.pullrequest.description,
                                   state=payload.pullrequest.state,
                                   author=payload.pullrequest.author.account_id,)
        return WebhookPayload(
            repository=repository,
            pull_request=pull_request,
            event=payload.event
        )
