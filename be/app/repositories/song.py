from sqlalchemy.orm import Session

from app.models.song import Song


# TODO: create_songs로 대체.
def create_song(
    db: Session,
    title: str,
    file_path: str,
    artist_id: int | None = None,
    album_id: int | None = None,
    genre: str | None = None,
    duration: int | None = None,
    play_count: int = 0,
    favorite: bool = False,
    rating: int | None = None,
) -> Song:
    """로컬 스토리지에서 스캔된 노래의 데이터를 데이터베이스에 저장한다.

    Args:
        db (Session)
        title (str)
        file_path (str): 스캔된 파일 경로
        artist_id (int | None)
        album_id (int | None)
        genre (str | None)
        duration (int | None): 초 단위
        play_count (int)
        favorite (bool)
        rating (int | None)
    Returns:
        Song
    Raises:
        ValueError: title이나 file_path가 없는 경우, 또는 rating이 1-5 범위를 벗어난 경우
    """

    if not title or title.isspace():
        raise ValueError("Title must be a valid string")

    if not file_path or file_path.isspace():
        raise ValueError("File path is required")

    if rating is not None and not (1 <= rating <= 5):
        raise ValueError("Rating must be between 1 and 5")

    song = Song(
        title=title,
        file_path=file_path,
        artist_id=artist_id,
        album_id=album_id,
        genre=genre,
        duration=duration,
        play_count=play_count,
        favorite=favorite,
        rating=rating,
    )
    db.add(song)
    db.commit()
    db.refresh(song)
    return song


def get_song_by_id(db: Session, song_id: int) -> Song | None:
    """노래 ID로 조회한다.

    Args:
        db (Session)
        song_id (int)
    Returns:
        Song | None
    """
    return db.query(Song).filter(Song.id == song_id).first()


def get_songs_by_artist_id(db: Session, artist_id: int) -> list[Song]:
    """아티스트 ID로 노래 목록 조회

    Args:
        db (Session)
        artist_id (int)
    Returns:
        list[Song]
    """
    return db.query(Song).filter(Song.artist_id == artist_id).all()


def get_songs_by_album_id(db: Session, album_id: int) -> list[Song]:
    """앨범 ID로 노래 목록 조회

    Args:
        db (Session)
        album_id (int)
    Returns:
        list[Song]
    """
    return db.query(Song).filter(Song.album_id == album_id).all()


def update_song(
    db: Session,
    song: Song,
    title: str | None = None,
    artist_id: int | None = None,
    album_id: int | None = None,
    genre: str | None = None,
    duration: int | None = None,
    play_count: int | None = None,
    favorite: bool | None = None,
    rating: int | None = None,
) -> Song:
    """노래 정보를 업데이트한다.

    Args:
        db (Session)
        song (Song)
        title (str | None)
        artist_id (int | None)
        album_id (int | None)
        genre (str | None)
        duration (int | None)
        play_count (int | None)
        favorite (bool | None)
        rating (int | None)
    Returns:
        Song
    Raises:
        ValueError: 적어도 하나의 필드는 업데이트되어야 한다.
        ValueError: rating이 1-5 범위를 벗어난 경우
    """
    if all(
        value is None
        for value in [
            title,
            artist_id,
            album_id,
            genre,
            duration,
            play_count,
            favorite,
            rating,
        ]
    ):
        raise ValueError("At least one field must be updated")

    if rating is not None and not (1 <= rating <= 5):
        raise ValueError("Rating must be between 1 and 5")

    if title is not None and (not title or title.isspace()):
        raise ValueError("Title must be a valid string")

    if title is not None:
        song.title = title
    if artist_id is not None:
        song.artist_id = artist_id
    if album_id is not None:
        song.album_id = album_id
    if genre is not None:
        song.genre = genre
    if duration is not None:
        song.duration = duration
    if play_count is not None:
        song.play_count = play_count
    if favorite is not None:
        song.favorite = favorite
    if rating is not None:
        song.rating = rating

    db.commit()
    db.refresh(song)
    return song


def delete_song(db: Session, song: Song):
    """노래를 삭제한다.

    Args:
        db (Session)
        song (Song)
    Returns:
        Song
    """
    db.delete(song)
    db.commit()
