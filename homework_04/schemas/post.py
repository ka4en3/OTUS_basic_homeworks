from typing import Annotated

from pydantic import BaseModel, EmailStr
from annotated_types import MaxLen


class PostBase(BaseModel):
    title: Annotated[str, MaxLen(400)]
    body: str = ""


class PostRead(PostBase):
    """
    Reads post
    """
    id: int


class PostCreate(PostBase):
    """
    Creates post
    """
