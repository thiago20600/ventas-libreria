from .tipo_insumo_repository import TipoInsumoRepository
from .tipo_insumo_schema import TipoInsumoResponse, TipoInsumoCreate

class TipoInsumoService():
    def __init__(self, repository: TipoInsumoRepository):
        self.repository = repository    


    def crear_tipo_insumo(self, tipo_insumo: TipoInsumoCreate) -> TipoInsumoResponse:
        tipo_insumo_creado = self.repository.crear_tipo_insumo(tipo_insumo)
        return TipoInsumoResponse.model_validate(tipo_insumo_creado)