from app.database.config import Base, engine
from app.models import Album, Artist, Playlist, PlaylistSong, Song, User


def init_db(engine=engine):
    """데이터베이스 테이블 생성"""
    Base.metadata.create_all(bind=engine)
