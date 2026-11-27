from typing import Annotated
from fastapi import Depends

from ...db.engine import DbSession
from .agenda_repository import AgendaRepository


def get_agenda_repository(session: DbSession) -> AgendaRepository:
    return AgendaRepository(session)


AgendaRepositoryDep = Annotated[AgendaRepository, Depends(get_agenda_repository)]