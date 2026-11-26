
from uuid import UUID, uuid4
from sqlmodel import Field, Relationship, SQLModel
from ..insumos.insumo_model import Insumo
from ..agendas_insumos.agenda_insumo_model import AgendaInsumo

class AgendaCatalogo(SQLModel, table=True):
    id: UUID = Field(default_factory=uuid4, primary_key=True)
    creador_id: UUID = Field(index=True)
    insumos: list["Insumo"] = Relationship(back_populates="agendas", link_model=AgendaInsumo)