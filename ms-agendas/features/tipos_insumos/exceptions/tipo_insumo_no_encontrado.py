from uuid import UUID

from common.exceptions.business_exception import BusinessException
from fastapi import status

class TipoInsumoNoEncontradoException(BusinessException):
    def __init__(self, tipo_insumo_id: UUID):
        super().__init__(message=f"Tipo de insumo {tipo_insumo_id} no encontrado",
                         status_code=status.HTTP_404_NOT_FOUND)