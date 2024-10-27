from pydantic import BaseModel


class SchemeNoteCreate(BaseModel):
    title: str
    content: str
    owner_id: int


class SchemeNoteResponse(SchemeNoteCreate):
    owner_id: int
