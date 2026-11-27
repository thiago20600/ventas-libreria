from uuid import UUID

from fastapi_pagination import Page
from sqlmodel import Session, asc, select
from .tipo_insumo_schema import TipoInsumoCreate
from .tipo_insumo_model import TipoInsumo
from fastapi_pagination.ext.sqlalchemy import paginate

class TipoInsumoRepository():
    def __init__(self, session: Session):
        self.session = session


    def crear_tipo_insumo(self, tipo_insumo: TipoInsumoCreate) -> TipoInsumo:
        nuevo_tipo_insumo = TipoInsumo.model_validate(tipo_insumo)

        self.session.add(nuevo_tipo_insumo)
        self.session.commit()
        self.session.refresh(nuevo_tipo_insumo)

        return nuevo_tipo_insumo


 
    def listar_tipos_insumos(self) -> Page[TipoInsumo]:
        query = select(TipoInsumo).order_by(asc(TipoInsumo.id))
        return paginate(self.session, query)


    def consultar_tipo_insumo_id(self, id: UUID) -> TipoInsumo | None:
        return self.session.get(TipoInsumo, id)

