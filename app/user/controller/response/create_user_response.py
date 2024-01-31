from typing import Annotated, Optional

from annotated_types import MinLen, MaxLen
from pydantic import BaseModel, EmailStr


class CreateUserRequest(BaseModel):
    login: Annotated[str, MinLen(3), MaxLen(20)]
    password: Annotated[str, MinLen(6)]
    email: EmailStr
    phone: Optional[str] = None
