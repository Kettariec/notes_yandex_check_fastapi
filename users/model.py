from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship
from database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, nullable=False)
    email = Column(String, nullable=False, unique=True)
    hashed_password = Column(String, nullable=False)
    is_email_verified = Column(Boolean, default=False)

    notes = relationship("Note", back_populates='owner')

    def __str__(self):
        return f'User {self.email}'