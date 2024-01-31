from abc import ABC, abstractmethod
from typing import TypeVar

from dataclasses import dataclass

from app.core.controller.base_request import BaseRequest

RequestType = TypeVar('RequestType', bound=BaseRequest)


@dataclass(slots=True)
class BaseController(ABC):
    _request: RequestType

    @abstractmethod
    async def invoke(self):
        pass
