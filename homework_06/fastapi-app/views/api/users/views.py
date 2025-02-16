from typing import Annotated

from fastapi import (
    APIRouter,
    HTTPException,
    status,
    Depends,
)
from pydantic import PositiveInt

from schemas.user import (
    UserCreate,
    UserRead,
)

from .crud import UsersStorage
from .dependencies import users_crud_dependency

router = APIRouter(
    prefix="/users",
    tags=["User"],
)


@router.get(
    "/",
    response_model=list[UserRead],
)
def get_users_list(
    storage: Annotated[
        UsersStorage,
        Depends(users_crud_dependency),
    ],
):
    return storage.get()


@router.post(
    "/",
    status_code=status.HTTP_201_CREATED,
    response_model=UserRead,
)
def create_user(
    user_in: UserCreate,
    storage: Annotated[
        UsersStorage,
        Depends(users_crud_dependency),
    ],
):
    return storage.create(user_in=user_in)


@router.get(
    "/{user_in}/",
    response_model=UserRead,
    responses={
        status.HTTP_404_NOT_FOUND: {
            "description": "User not found",
            "content": {
                "application/json": {
                    "example": {
                        "detail": "User #0 not found",
                    },
                },
            },
        },
    },
)
def get_user(
    user_in: PositiveInt,
    storage: Annotated[
        UsersStorage,
        Depends(users_crud_dependency),
    ],
):
    user = storage.get_by_id(user_in=user_in)
    if user:
        return user

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"User #{user_in} not found",
    )
