from sqlalchemy import Column, ForeignKey, Integer, String

from .base import Base


class Album(Base):
    __tablename__ = "Albums"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False)
    artist_id = Column(Integer, ForeignKey("Artists.id", ondelete="SET NULL"))
    release_year = Column(Integer, nullable=True)
