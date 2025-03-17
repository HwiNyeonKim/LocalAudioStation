from sqlalchemy import (
    Boolean,
    CheckConstraint,
    Column,
    ForeignKey,
    Integer,
    String,
)

from app.database import Base


class Song(Base):
    __tablename__ = "Songs"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False)
    artist_id = Column(Integer, ForeignKey("Artists.id", ondelete="SET NULL"))
    album_id = Column(Integer, ForeignKey("Albums.id", ondelete="SET NULL"))
    genre = Column(String(64), nullable=True)
    duration = Column(Integer, nullable=True)  # [sec]
    file_path = Column(String(512), unique=True, nullable=False)
    play_count = Column(Integer, default=0)
    favorite = Column(Boolean, default=False)
    rating = Column(Integer, nullable=True)  # 1-5 stars

    __table_args__ = (
        CheckConstraint("rating BETWEEN 1 AND 5", name="validate_rating"),
    )
