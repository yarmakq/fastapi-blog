from typing import Annotated, Optional

from annotated_types import MinLen, MaxLen
from pydantic import EmailStr

from app.core.controller.base_request import BaseRequest


class CreateUserRequest(BaseRequest):
    login: Annotated[str, MinLen(3), MaxLen(20)]
    password: Annotated[str, MinLen(6)]
    email: EmailStr
    phone: Optional[str] = None
