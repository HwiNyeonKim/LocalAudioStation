from sqlalchemy import Column, Integer, String

from app.database import Base


class Artist(Base):
    __tablename__ = "Artists"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), unique=True, nullable=False)
