from uuid import UUID

from fastapi_pagination import Page
from pydantic import TypeAdapter
from fastapi import HTTPException, status
from .tipo_insumo_repository import TipoInsumoRepository
from .tipo_insumo_schema import TipoInsumoResponse, TipoInsumoCreate
from .tipo_insumo_model import TipoInsumo
from .exceptions.tipo_insumo_no_encontrado import TipoInsumoNoEncontradoException

class TipoInsumoService():
    def __init__(self, repository: TipoInsumoRepository):
        self.repository = repository    


    def crear_tipo_insumo(self, tipo_insumo: TipoInsumoCreate) -> TipoInsumoResponse:
        tipo_insumo_creado = self.repository.crear_tipo_insumo(tipo_insumo)
        return TipoInsumoResponse.model_validate(tipo_insumo_creado)


    def listar_tipos_insumos(self) -> Page[TipoInsumo]:
        return self.repository.listar_tipos_insumos()


    def consultar_tipo_insumo_id(self, id: UUID) -> TipoInsumo:
            
        tipo_insumo = self.repository.consultar_tipo_insumo_id(id)

        if tipo_insumo is None:
            raise TipoInsumoNoEncontradoException(tipo_insumo_id=id)
        
        return tipo_insumo