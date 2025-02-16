from typing import Annotated

from pydantic import BaseModel, EmailStr
from annotated_types import MaxLen


class UserBase(BaseModel):
    username: Annotated[str, MaxLen(20)]
    name: Annotated[str, MaxLen(200)]
    email: EmailStr | None = None


class UserRead(UserBase):
    """
    Reads author
    """
    id: int


class UserCreate(UserBase):
    """
    Creates author
    """
