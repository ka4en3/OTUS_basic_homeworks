from typing import Generator

from fastapi import Depends
from sqlalchemy.orm import Session

from models.db_sync import session_factory
from .crud import UsersStorage


def session_dependency() -> Generator[Session, None, None]:
    with session_factory() as session:
        yield session


def users_crud_dependency(
    session: Session = Depends(session_dependency),
) -> UsersStorage:
    return UsersStorage(session=session)
