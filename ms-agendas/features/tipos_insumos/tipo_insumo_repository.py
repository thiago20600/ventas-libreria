from sqlmodel import Session
from .tipo_insumo_schema import TipoInsumoCreate
from .tipo_insumo_model import TipoInsumo

class TipoInsumoRepository():
    def __init__(self, session: Session):
        self.session = session


    def crear_tipo_insumo(self, tipo_insumo: TipoInsumoCreate) -> TipoInsumo:
        nuevo_tipo_insumo = TipoInsumo.model_validate(tipo_insumo)

        self.session.add(nuevo_tipo_insumo)
        self.session.commit()
        self.session.refresh(nuevo_tipo_insumo)

        return nuevo_tipo_insumo
