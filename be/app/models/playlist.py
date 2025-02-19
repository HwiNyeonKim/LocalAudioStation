from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, func

from .base import Base


class Playlist(Base):
    __tablename__ = "Playlists"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(
        Integer, ForeignKey("Users.id", ondelete="CASCADE"), nullable=False
    )
    name = Column(String(255), nullable=False)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())
