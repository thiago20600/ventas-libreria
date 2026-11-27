


from datetime import datetime, timezone
from decimal import Decimal
from typing import Any
from uuid import UUID, uuid4
from sqlalchemy.dialects.postgresql import JSONB

from sqlalchemy import CheckConstraint, Column
from sqlmodel import Field, Relationship, SQLModel
from ..agendas.agenda_model import AgendaCatalogo
from ..agendas_insumos.agenda_insumo_model import AgendaInsumo
from ..tipos_insumos.tipo_insumo_model import TipoInsumo


class Insumo(SQLModel, table=True):

    __table_args__ = (
        CheckConstraint("stock >= 0", name="ck_insumo_stock"),
        CheckConstraint("version >= 1", name="ck_insumo_version"),
        CheckConstraint("precio_unitario >= 0", name="ck_insumo_precio_unitario"),
    )



    id: UUID = Field(default_factory=uuid4, primary_key=True)
    nombre: str = Field(min_length=10, max_length=300)
    tipo_insumo_id: UUID = Field(foreign_key="tipoinsumo.id", index=True) 
    descripcion: str | None = Field(default=None, min_length=10, max_length=700)
    imagen: list[str] | None = Field(default=None, sa_column=Column(JSONB))
    stock: int = Field(ge=0)
    precio_unitario: Decimal = Field(max_digits=10, decimal_places=2, ge=0)
    fecha_creacion: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    version: int = Field(default=1, ge=1)
    agendas: list["AgendaCatalogo"] = Relationship(back_populates="insumos", link_model=AgendaInsumo)
    tipo_insumo: "TipoInsumo" = Relationship(back_populates="insumos")