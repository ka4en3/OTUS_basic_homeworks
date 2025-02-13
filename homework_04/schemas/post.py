from typing import Annotated

from pydantic import BaseModel
from annotated_types import MaxLen


class PostBase(BaseModel):
    title: Annotated[str, MaxLen(400)]
    body: str = ""
    userId: int
