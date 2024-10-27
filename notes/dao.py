from sqlalchemy import insert, select
from dao.base import BaseDAO
from notes.model import Note
from database import async_session_maker


class NoteDAO(BaseDAO):
    model = Note

    @classmethod
    async def add_note(cls, title: str, content: str, owner_id: int):
        async with async_session_maker() as session:
            query = insert(cls.model).values(title=title, content=content, owner_id=owner_id)
            await session.execute(query)
            await session.commit()
            new_note = Note(title=title, content=content, owner_id=owner_id)
            return new_note

    @classmethod
    async def get_user_notes(cls, owner_id: int):
        async with async_session_maker() as session:
            query = select(cls.model).where(cls.model.owner_id == owner_id)
            result = await session.execute(query)
            return result.scalars().all()
