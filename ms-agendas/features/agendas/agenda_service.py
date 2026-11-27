from .agenda_repository import AgendaRepository

class AgendaService():
    def __init__(self, repository: AgendaRepository):
        self.repository = repository