from sqlalchemy.orm import Session

from app.models import Artist


def create_artist(db: Session, name: str) -> Artist:
    """새로운 아티스트를 생성하고 데이터베이스에 저장한다.
    - 아티스트의 이름은 고유해야 하며, 유효한 문자열이어야 한다.

    Args:
        db (Session)
        name (str)
    Returns:
        Artist
    Raises:
        ValueError: 동일한 이름의 아티스트가 이미 존재하거나, 이름이 유효하지 않을 경우
    """
    if not name or name.isspace():
        raise ValueError("Artist name cannot be empty or whitespace")

    existing_artist = db.query(Artist).filter(Artist.name == name).first()
    if existing_artist:
        raise ValueError(f"Artist with name '{name}' already exists")

    artist = Artist(name=name)
    db.add(artist)
    db.commit()
    db.refresh(artist)
    return artist


def get_artist_by_id(db: Session, artist_id: int) -> Artist | None:
    """아티스트 정보를 조회한다.

    Args:
        db (Session)
        artist_id (int)
    Returns:
        Artist | None
    """
    return db.query(Artist).filter(Artist.id == artist_id).first()


def get_artist_by_name(db: Session, name: str) -> Artist | None:
    """아티스트 정보를 이름으로 조회한다.

    Args:
        db (Session)
        name (str)
    Returns:
        Artist | None
    """
    return db.query(Artist).filter(Artist.name == name).first()


# TODO: 현재는 이름밖에 수정할 필드가 없으므로 그냥 받는데, 필드가 늘어난다면 별도의 자료구조로 받기
def update_artist(db: Session, artist: Artist, name: str) -> Artist:
    """아티스트 정보를 업데이트한다.

    Args:
        db (Session)
        artist (Artist)
        name (str)
    Returns:
        Artist
    """
    if not name:
        raise ValueError("Artist name must be a valid string.")

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
