


from decimal import Decimal
from uuid import UUID

from sqlalchemy import CheckConstraint
from sqlmodel import Field, SQLModel


class AgendaInsumo(SQLModel, table=True):
    __table_args__ = (
        CheckConstraint("cantidad > 0", name="ck_agenda_insumo_cantidad"),
        CheckConstraint("precio_historico >= 0", name="ck_agenda_insumo_precio_historico"),
    )

    agenda_id: UUID = Field(foreign_key="agendacatalogo.id", primary_key=True)
    insumo_id: UUID = Field(foreign_key="insumo.id", primary_key=True)
    cantidad: int = Field(gt=0)
    precio_historico: Decimal = Field(max_digits=10, decimal_places=2, ge=0)