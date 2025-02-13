from typing import Annotated

from pydantic import BaseModel, EmailStr
from annotated_types import MaxLen


class UserBase(BaseModel):
    id: int
    username: Annotated[str, MaxLen(20)]
    name: Annotated[str, MaxLen(200)]
    email: EmailStr | None = None
