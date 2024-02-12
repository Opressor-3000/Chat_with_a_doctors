from typing import Optional

from pydantic import BaseModel


class BaseAccess(BaseModel):
    title: str


class Accessid(BaseAccess):
    id: int
