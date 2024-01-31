from abc import ABC

from pydantic import BaseModel


class BaseResponse(ABC, BaseModel):
    pass
