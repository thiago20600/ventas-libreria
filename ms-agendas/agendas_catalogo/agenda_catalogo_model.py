from datetime import datetime, timezone
from decimal import Decimal
from uuid import UUID, uuid4
from pydantic import HttpUrl
from sqlalchemy import JSON, Column
from sqlmodel import Field, SQLModel


class AgendaCatalogo(SQLModel, table=True):
    id: UUID | None = Field(default_factory=uuid4, primary_key=True)
    nombre: str = Field(max_length=300, min_length=10)
    descripcion: str | None = Field(default=None ,max_length=900)
    precio_base: Decimal = Field(max_digits=10, decimal_places=2, ge=0)
    vendedor_id: UUID = Field(index=True)
    fotos: list[str] | None = Field(default=None, sa_column=Column(JSON))
    fecha_publicacion: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))