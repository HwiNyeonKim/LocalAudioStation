from sqlalchemy import Column, ForeignKey, Integer

from app.database import Base


class PlaylistSong(Base):
    __tablename__ = "Playlist_Songs"

    playlist_id = Column(
        Integer,
        ForeignKey("Playlists.id", ondelete="CASCADE"),
        primary_key=True,
    )
    song_id = Column(
        Integer, ForeignKey("Songs.id", ondelete="CASCADE"), primary_key=True
    )
