from typing import Optional

from pydantic import BaseModel


class BaseAccess(BaseModel):
    title: str
    parent_id: Optional[int] = None


class Accessid(BaseAccess):
    id: int
