from typing import Annotated

from fastapi import (
    APIRouter,
    Depends,
    Request,
)
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from db.crud import UsersStorage
from db.dependencies import users_crud_dependency
from schemas.user import UserRead

templates = Jinja2Templates(directory="templates")
router = APIRouter(
    prefix="/users",
    tags=["HTMLUser"],
)


@router.get(
    "/",
    response_class=HTMLResponse,
)
def get_users_list(
    request: Request,
    storage: Annotated[
        UsersStorage,
        Depends(users_crud_dependency),
    ],
):
    return templates.TemplateResponse(
        "index.html", {"request": request, "users": storage.get()}
    )
