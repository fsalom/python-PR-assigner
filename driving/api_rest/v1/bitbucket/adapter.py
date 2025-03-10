from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends
from fastapi.encoders import jsonable_encoder
from starlette import status
from starlette.responses import JSONResponse

from driving.api_rest.v1.bitbucket.mapper import BitbucketDTOMapper
from infrastructure.di.bitbucket.container import BitbucketContainer

bitbucket_router = APIRouter()


@bitbucket_router.get('/bitbucket/me')
@inject
async def webhook(api_mapper: BitbucketDTOMapper = Depends(Provide[BitbucketContainer.api_mapper])):
    return JSONResponse(
                status_code=status.HTTP_200_OK,
                content=jsonable_encoder(api_mapper.to_domain())
            )
