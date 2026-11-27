from pydantic import BaseModel, Field


class CurrentUser(BaseModel):
    id: str
    email: str | None = None
    username: str | None = None
    roles: list[str] = Field(default_factory=list)