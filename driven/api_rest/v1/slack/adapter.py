from dependency_injector.wiring import inject
from fastapi import APIRouter
from starlette.responses import JSONResponse

slack_router = APIRouter()


@slack_router.patch('/slack/me/device')
@inject
async def update_fcm(service: UserServicePort = Depends(Provide[UserContainer.service]),
                     api_mapper: UserDTOMapper = Depends(Provide[UserContainer.api_mapper])):
    await service.update_fcm_token(user, fcm_request.device_id, fcm_request.platform)
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content=jsonable_encoder(api_mapper.to_domain())
    )
