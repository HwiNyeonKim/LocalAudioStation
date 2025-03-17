from app.database.config import Base, engine
from app.models import Album, Artist, Playlist, PlaylistSong, Song, User


def init_db():
    """데이터베이스 테이블 생성"""
    Base.metadata.create_all(bind=engine)


if __name__ == "__main__":
    init_db()
