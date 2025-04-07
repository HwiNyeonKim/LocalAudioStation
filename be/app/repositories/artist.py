from sqlalchemy.orm import Session

from app.models import Artist


# TODO: Add type hints for return values
def create_artist(db: Session, name: str):
    """새로운 아티스트를 생성하고 데이터베이스에 저장한다.

    Args:
        db (Session)
        name (str)
    """
    artist = Artist(name=name)
    db.add(artist)
    db.commit()
    db.refresh(artist)
    return artist


def get_artist_by_id(db: Session, artist_id: int):
    """아티스트 정보를 조회한다.

    Args:
        db (Session)
        artist_id (int)
    Returns:
        Artist
    """
    return db.query(Artist).filter(Artist.id == artist_id).first()


def get_artist_by_name(db: Session, name: str):
    """아티스트 정보를 이름으로 조회한다.

    Args:
        db (Session)
        name (str)
    Returns:
        Artist
    """
    return db.query(Artist).filter(Artist.name == name).first()


# TODO: 현재는 이름밖에 수정할 필드가 없으므로 그냥 받는데, 필드가 늘어난다면 별도의 자료구조로 받기
def update_artist(db: Session, artist: Artist, name: str):
    """아티스트 정보를 업데이트한다.

    Args:
        db (Session)
        artist (Artist)
        name (str)
    Returns:
        Artist
    """
    if not name:
        raise ValueError("이름은 공란으로 만들 수 없다.")

    artist.name = name
    db.commit()
    db.refresh(artist)
    return artist


# XXX: 이 기능은 제거 or 비활성화 고려
def delete_artist(db: Session, artist: Artist):
    """아티스트 정보를 삭제한다.

    Args:
        db (Session)
        artist (Artist)
    """
    db.delete(artist)
    db.commit()
    return artist
