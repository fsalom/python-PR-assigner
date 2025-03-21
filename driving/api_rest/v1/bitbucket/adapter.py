from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends
from starlette import status
from starlette.responses import JSONResponse

from application.ports.driving.bitbucket_service_port import BitbucketServicePort
from driving.api_rest.v1.bitbucket.mapper import BitbucketDTOMapper
from driving.api_rest.v1.bitbucket.models import WebhookPayloadRequest
from infrastructure.di.bitbucket.container import BitbucketContainer

bitbucket_router = APIRouter()


@bitbucket_router.post('/webhook')
@inject
async def webhook(
        payload_request: WebhookPayloadRequest,
        service: BitbucketServicePort = Depends(Provide[BitbucketContainer.service]),
        api_mapper: BitbucketDTOMapper = Depends(Provide[BitbucketContainer.api_mapper])):
    payload = api_mapper.to_domain(payload_request)
    service.assign(payload)
    return JSONResponse(
                status_code=status.HTTP_200_OK,
                content={"result": "ok"})
