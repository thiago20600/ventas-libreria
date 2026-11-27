from sqlmodel import Session
from ...db.engine import DbSession

class AgendaRepository():
    def __init__(self, session: Session):
        self.session = session