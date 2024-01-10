from datetime import datetime

from sqlalchemy import MetaData, Column, Integer, String, TIMESTAMP, ForeignKey, JSON
from sqlalchemy.orm import declarative_base

Base = declarative_base()
metadata = Base.metadata


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    email = Column(String(50), nullable=False)
    username = Column(String(50), nullable=False)
    password = Column(String(50), nullable=False)
    registered_at = Column(TIMESTAMP, default=datetime.utcnow)
    role_id = Column(ForeignKey("roles.id"))


class Roles(Base):
    __tablename__ = "roles"

    id = Column(Integer, primary_key=True)
    title = Column(String(50), nullable=False)
    permissions = Column(JSON)
