from datetime import datetime, timezone
from uuid import UUID, uuid4

from sqlmodel import Field, Relationship, SQLModel
from ..insumos.insumo_model import Insumo


class TipoInsumo(SQLModel, table=True):
    id: UUID = Field(default_factory=uuid4, primary_key=True)
    nombre: str = Field(min_length=2, max_length=100)
    obligatorio: bool = Field(default=False)
    insumos: list["Insumo"] = Relationship(back_populates="tipo_insumo")
    fecha_creacion: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))