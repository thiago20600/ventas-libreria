from uuid import UUID

from fastapi import APIRouter, Depends, status
from fastapi_pagination import Page
from .tipo_insumo_schema import  TipoInsumoCreate, TipoInsumoResponse
from .tipo_insumo_dependencies import TipoInsumoServiceDep
from common.security.require_roles import require_roles

router = APIRouter(prefix="v1/tipo-insumo")


@router.post("/", response_model=TipoInsumoResponse, status_code=status.HTTP_201_CREATED, dependencies=[Depends(require_roles("VENDEDOR"))])
def crear_tipo_insumo(tipo_insumo: TipoInsumoCreate, service: TipoInsumoServiceDep):
    return service.crear_tipo_insumo(tipo_insumo)


@router.get("/", response_model=Page[TipoInsumoResponse], status_code=status.HTTP_200_OK, dependencies=[Depends(require_roles("VENDEDOR"))])
def listar_tipos_insumos(service: TipoInsumoServiceDep):
    return service.listar_tipos_insumos()


@router.get("/{id}", response_model=TipoInsumoResponse, status_code=status.HTTP_200_OK, dependencies=[Depends(require_roles("VENDEDOR"))])
def consultar_tipo_insumo_id(service: TipoInsumoServiceDep, id: UUID):
    return service.consultar_tipo_insumo_id(id)


