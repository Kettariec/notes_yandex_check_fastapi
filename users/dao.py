from dao.base import BaseDAO
from users.model import User
from sqlalchemy import update
from database import async_session_maker


class UserDAO(BaseDAO):
    model = User

    @classmethod
    async def add(cls, email: str, hashed_password: str):
        async with async_session_maker() as session:
            new_user = User(email=email, hashed_password=hashed_password)
            session.add(new_user)
            await session.commit()
            return new_user

    @classmethod
    async def update(cls, user: User):
        async with async_session_maker() as session:
            stmt = (
                update(User)
                .where(User.id == user.id)
                .values(is_email_verified=user.is_email_verified)
            )
            await session.execute(stmt)
            await session.commit()
