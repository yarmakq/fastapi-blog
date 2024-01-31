from abc import ABC

from pydantic import BaseModel


class BaseRequest(ABC, BaseModel):
    pass
