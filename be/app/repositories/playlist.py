from sqlalchemy.orm import Session

from app.models.playlist import Playlist


def create_playlist(
    db: Session,
    user_id: int,
    name: str,
) -> Playlist:
    """플레이리스트를 생성한다.

    Args:
        db (Session)
        user_id (int): 플레이리스트 소유자 ID
        name (str): 플레이리스트 이름

    Returns:
        Playlist

    Raises:
        ValueError: name이 없는 경우
    """
    if not name:
        raise ValueError("Name cannot be empty")

    playlist = Playlist(
        user_id=user_id,
        name=name,
    )
    db.add(playlist)
    db.commit()
    db.refresh(playlist)
    return playlist


def get_playlist_by_id(db: Session, playlist_id: int) -> Playlist | None:
    """플레이리스트 ID로 조회한다.

    Args:
        db (Session)
        playlist_id (int)
    Returns:
        Playlist | None
    """
    return db.query(Playlist).filter(Playlist.id == playlist_id).first()


def get_playlists_by_user_id(db: Session, user_id: int) -> list[Playlist]:
    """사용자 ID로 플레이리스트 목록을 조회한다.

    Args:
        db (Session)
        user_id (int)
    Returns:
        list[Playlist]
    """
    return db.query(Playlist).filter(Playlist.user_id == user_id).all()


def update_playlist(
    db: Session,
    playlist: Playlist,
    name: str | None = None,
) -> Playlist:
    """플레이리스트 정보를 업데이트한다.

    Args:
        db (Session)
        playlist (Playlist)
        name (str | None)
    Returns:
        Playlist

    Raises:
        ValueError: name이 빈 문자열인 경우
    """
    if name is not None:
        if not name:
            raise ValueError("Name cannot be empty")
        playlist.name = name

    db.commit()
    db.refresh(playlist)
    return playlist


def delete_playlist(db: Session, playlist: Playlist):
    """플레이리스트를 삭제한다.

    Args:
        db (Session)
        playlist (Playlist)
    """
    db.delete(playlist)
    db.commit()
