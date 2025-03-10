from dependency_injector import containers, providers

from application.services.bitbucket_service import BitbucketServices
from driving.api_rest.v1.bitbucket.mapper import BitbucketDTOMapper


class BitbucketContainer(containers.DeclarativeContainer):
    config = providers.Configuration()
    wiring_config = containers.WiringConfiguration(modules=["driving.api_rest.v1.bitbucket.adapter"])

    service = providers.Factory(
        BitbucketServices
    )

    api_mapper = providers.Factory(
        BitbucketDTOMapper
    )
