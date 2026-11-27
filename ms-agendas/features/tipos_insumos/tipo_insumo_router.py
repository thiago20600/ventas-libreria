from fastapi import APIRouter, status
from .tipo_insumo_schema import  TipoInsumoCreate, TipoInsumoResponse
from .tipo_insumo_dependencies import TipoInsumoServiceDep

router = APIRouter(prefix="/tipo-insumo")


@router.post("/", response_model=TipoInsumoResponse, status_code=status.HTTP_201_CREATED)
def crear_tipo_insumo(tipo_insumo: TipoInsumoCreate, service: TipoInsumoServiceDep):
    return service.crear_tipo_insumo(tipo_insumo)