from sqlalchemy.orm import Session

from app.models import Album


def create_album(db: Session, title: str, artist_id: int, release_year: int):
    """새로운 앨범을 생성하고 데이터베이스에 저장한다.

    Args:
        db (Session)
        title (str)
        artist_id (int)
        release_year (int)
    """
    album = Album(title=title, artist_id=artist_id, release_year=release_year)
    db.add(album)
    db.commit()
    db.refresh(album)
    return album


def get_album_by_id(db: Session, album_id: int):
    """앨범 정보를 조회한다.

    Args:
        db (Session)
        album_id (int)
    Returns:
        Album
    """
    # TODO: artist_id 등 다른 필드가 숫자가 아니라 정상적인 이름으로 돌아가는지 확인
    return db.query(Album).filter(Album.id == album_id).first()


def get_album_by_artist_id(db: Session, artist_id: int):
    """아티스트의 앨범 정보를 조회한다.

    Args:
        db (Session)
        artist_id (int)
    Returns:
        Album
    """
    return db.query(Album).filter(Album.artist_id == artist_id).all()


def update_album(
    db: Session, album: Album, title: str, artist_id: int, release_year: int
):
    """앨범 정보를 업데이트한다.

    Args:
        db (Session)
        album (Album)
        title (str)
        artist_id (int)
        release_year (int)
    Returns:
        Album
    """
    if not any([title, artist_id, release_year]):
        raise ValueError(
            "title, artist_id, release_year 중 하나의 값은 존재해야 한다."
        )

    album.title = title
    album.artist_id = artist_id
    album.release_year = release_year
    db.commit()
    db.refresh(album)
    return album


def delete_album(db: Session, album: Album):
    """앨범 정보를 삭제한다.

    Args:
        db (Session)
        album (Album)
    """
    db.delete(album)
    db.commit()
    return album
