from sqlalchemy.orm import Session

from app.models.playlist_song import PlaylistSong


def create_playlist_song(
    db: Session,
    playlist_id: int,
    song_id: int,
) -> PlaylistSong:
    """플레이리스트에 노래를 추가한다.

    Args:
        db (Session)
        playlist_id (int): 플레이리스트 ID
        song_id (int): 노래 ID

    Returns:
        PlaylistSong
    """
    playlist_song = PlaylistSong(
        playlist_id=playlist_id,
        song_id=song_id,
    )
    db.add(playlist_song)
    db.commit()
    db.refresh(playlist_song)
    return playlist_song


def get_playlist_songs_by_playlist_id(
    db: Session, playlist_id: int
) -> list[PlaylistSong]:
    """플레이리스트 ID로 플레이리스트에 포함된 노래 목록을 조회한다.

    Args:
        db (Session)
        playlist_id (int)
    Returns:
        list[PlaylistSong]
    """
    return (
        db.query(PlaylistSong)
        .filter(PlaylistSong.playlist_id == playlist_id)
        .all()
    )


def delete_playlist_song(db: Session, playlist_song: PlaylistSong):
    """플레이리스트에서 노래를 삭제한다.

    Args:
        db (Session)
        playlist_song (PlaylistSong)
    """
    db.delete(playlist_song)
    db.commit()
