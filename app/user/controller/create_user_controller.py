from app.core.controller.base_controller import BaseController
from app.user.controller.request.create_user_request import CreateUserRequest
from app.user.repository.user_repository import UserRepository


class CreateUserController(BaseController):
    _user_repo: UserRepository

    def __init__(
        self,
        request: CreateUserRequest,
        user_repo: UserRepository,
    ):
        super().__init__(request)
        self._user_repo = user_repo

    async def invoke(self):
        return {
            'login': self._request.login,
            'email': self._request.email,
            'phone': self._request.phone,
            'save': self._user_repo.save(),
        }
