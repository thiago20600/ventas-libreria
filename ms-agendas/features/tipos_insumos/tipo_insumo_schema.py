from uuid import UUID

from sqlmodel import Field, SQLModel


class TipoInsumoCreate(SQLModel):
    nombre: str = Field(min_length=2, max_length=100)
    obligatorio: bool = False


class TipoInsumoResponse(SQLModel):
    id: UUID 
    nombre: str 
    obligatorio: bool


class TipoInsumoUpdate(SQLModel):
    nombre: str | None = Field(default=None, min_length=2, max_length=100)
    obligatorio: bool | None = None

