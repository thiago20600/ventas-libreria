from datetime import datetime
from typing import Annotated
from decimal import Decimal
from uuid import UUID
from pydantic import Field, HttpUrl, field_validator
from sqlmodel import SQLModel



class AgendaCatalogoCreate(SQLModel):
    nombre: str = Field(min_length=10, max_length=300)
    descripcion: str | None = Field(default=None, max_length=900)
    precio_base: Decimal = Field(max_digits=10, decimal_places=2, ge=0)
    fotos: Annotated[list[HttpUrl], Field(max_length=5)] | None = None
    #insumos: list[InsumoItem] = Field(min_length=1)
    insumos: list[str] = Field(min_length=1)
    stock_agenda: int = Field(default=1, ge=1)



class AgendaCatalogoResponse(SQLModel):
    id: UUID
    nombre: str
    descripcion: str | None
    precio_base: Decimal
    vendedor_id: UUID
    fotos: list[str] | None
    stock_agenda: int
    fecha_publicacion: datetime