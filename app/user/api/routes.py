from typing import Annotated

from fastapi import APIRouter, Depends

from app.user.controller.create_user_controller import CreateUserController
from app.user.controller.request.create_user_request import CreateUserRequest
from app.user.repository.user_repository import UserRepository

router = APIRouter(
    prefix='/user',
    tags=['user'],
)


@router.get('/')
def get_users():
    return {
        'user': [],
    }


@router.post('/create')
async def create_user(
    request: Annotated[CreateUserRequest, Depends(CreateUserRequest)],
    user_repo: Annotated[UserRepository, Depends(UserRepository)]
):
    return await CreateUserController(
        request=request,
        user_repo=user_repo,
    ).invoke()
