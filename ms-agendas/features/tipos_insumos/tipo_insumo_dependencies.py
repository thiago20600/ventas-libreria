from typing import Annotated

from fastapi import Depends

from ...db.engine import DbSession
from .tipo_insumo_repository import TipoInsumoRepository
from .tipo_insumo_service import TipoInsumoService

def get_tipo_insumo_repository(session: DbSession) -> TipoInsumoRepository:
    return TipoInsumoRepository(session)

TipoInsumoRepositoryDep = Annotated[TipoInsumoRepository, Depends(get_tipo_insumo_repository)]


def get_tipo_insumo_service(repository: TipoInsumoRepositoryDep) -> TipoInsumoService:
    return TipoInsumoService(repository)

TipoInsumoServiceDep = Annotated[TipoInsumoService, Depends(get_tipo_insumo_service)]