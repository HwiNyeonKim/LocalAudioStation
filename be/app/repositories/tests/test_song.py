import pytest

from app.models.song import Song

from ..song import (
    create_song,
    delete_song,
    get_song_by_id,
    get_songs_by_album_id,
    get_songs_by_artist_id,
    update_song,
)


def test_create_song(test_db_session):
    """노래 생성 테스트"""
    test_title = "test_song"
    test_file_path = "test_file_path"
    test_artist_id = 1
    test_album_id = 1
    test_genre = "test_genre"
    test_duration = 100
    test_play_count = 100
    test_favorite = True
    test_rating = 5

    song = create_song(
        test_db_session,
        title=test_title,
        file_path=test_file_path,
        artist_id=test_artist_id,
        album_id=test_album_id,
        genre=test_genre,
        duration=test_duration,
        play_count=test_play_count,
        favorite=test_favorite,
        rating=test_rating,
    )
    assert song is not None
    assert song.title == test_title
    assert song.file_path == test_file_path
    assert song.artist_id == test_artist_id
    assert song.album_id == test_album_id
    assert song.genre == test_genre
    assert song.duration == test_duration
    assert song.play_count == test_play_count
    assert song.favorite == test_favorite
    assert song.rating == test_rating

    created_song = (
        test_db_session.query(Song).filter_by(title=test_title).first()
    )
    assert created_song is not None
    assert created_song == song


@pytest.mark.parametrize("invalid_title", ["", " ", "  ", None])
def test_create_song_failure_invalid_name(test_db_session, invalid_title):
    """노래 생성 실패 테스트 - 유효하지 않은 이름

    빈 문자열, 공백, 또는 None은 유효하지 않은 이름으로 간주된다.
    """
    with pytest.raises(ValueError):
        create_song(test_db_session, title=invalid_title, file_path="test")


def test_get_song_by_id(test_db_session):
    """노래 ID로 조회 테스트"""
    test_title = "test_song"
    test_file_path = "test_file_path"
    test_artist_id = 1
    test_album_id = 1
    test_genre = "test_genre"
    test_duration = 100
    test_play_count = 100
    test_favorite = True
    test_rating = 5

    song = create_song(
        test_db_session,
        title=test_title,
        file_path=test_file_path,
        artist_id=test_artist_id,
        album_id=test_album_id,
        genre=test_genre,
        duration=test_duration,
        play_count=test_play_count,
        favorite=test_favorite,
        rating=test_rating,
    )
    assert song is not None
    assert song.title == test_title
    assert song.file_path == test_file_path
    assert song.artist_id == test_artist_id
    assert song.album_id == test_album_id
    assert song.genre == test_genre
    assert song.duration == test_duration
    assert song.play_count == test_play_count
    assert song.favorite == test_favorite
    assert song.rating == test_rating

    found_song = get_song_by_id(test_db_session, song.id)
    assert found_song is not None
    assert found_song == song


def test_get_songs_by_artist_id(test_db_session):
    """아티스트 ID로 노래 목록 조회 테스트"""
    test_title = "test_song"
    test_file_path = "test_file_path"
    test_artist_id = 1
    test_album_id = 1
    test_genre = "test_genre"
    test_duration = 100
    test_play_count = 100
    test_favorite = True
    test_rating = 5

    song = create_song(
        test_db_session,
        title=test_title,
        file_path=test_file_path,
        artist_id=test_artist_id,
        album_id=test_album_id,
        genre=test_genre,
        duration=test_duration,
        play_count=test_play_count,
        favorite=test_favorite,
        rating=test_rating,
    )
    assert song is not None
    assert song.title == test_title
    assert song.file_path == test_file_path
    assert song.artist_id == test_artist_id
    assert song.album_id == test_album_id
    assert song.genre == test_genre
    assert song.duration == test_duration
    assert song.play_count == test_play_count
    assert song.favorite == test_favorite
    assert song.rating == test_rating

    songs = get_songs_by_artist_id(test_db_session, test_artist_id)
    assert len(songs) == 1
    assert songs[0] == song


def test_get_songs_by_album_id(test_db_session):
    """앨범 ID로 노래 목록 조회 테스트"""
    test_title = "test_song"
    test_file_path = "test_file_path"
    test_artist_id = 1
    test_album_id = 1
    test_genre = "test_genre"
    test_duration = 100
    test_play_count = 100
    test_favorite = True
    test_rating = 5

    song = create_song(
        test_db_session,
        title=test_title,
        file_path=test_file_path,
        artist_id=test_artist_id,
        album_id=test_album_id,
        genre=test_genre,
        duration=test_duration,
        play_count=test_play_count,
        favorite=test_favorite,
        rating=test_rating,
    )
    assert song is not None
    assert song.title == test_title
    assert song.file_path == test_file_path
    assert song.artist_id == test_artist_id
    assert song.album_id == test_album_id
    assert song.genre == test_genre
    assert song.duration == test_duration
    assert song.play_count == test_play_count
    assert song.favorite == test_favorite
    assert song.rating == test_rating

    songs = get_songs_by_album_id(test_db_session, test_album_id)
    assert len(songs) == 1
    assert songs[0] == song


def test_update_song(test_db_session):
    """노래 업데이트 테스트"""
    test_title = "test_song"
    test_file_path = "test_file_path"
    test_artist_id = 1
    test_album_id = 1
    test_genre = "test_genre"
    test_duration = 100
    test_play_count = 100
    test_favorite = True
    test_rating = 5

    song = create_song(
        test_db_session,
        title=test_title,
        file_path=test_file_path,
        artist_id=test_artist_id,
        album_id=test_album_id,
        genre=test_genre,
        duration=test_duration,
        play_count=test_play_count,
        favorite=test_favorite,
        rating=test_rating,
    )
    assert song is not None
    assert song.title == test_title
    assert song.file_path == test_file_path
    assert song.artist_id == test_artist_id
    assert song.album_id == test_album_id
    assert song.genre == test_genre
    assert song.duration == test_duration
    assert song.play_count == test_play_count
    assert song.favorite == test_favorite
    assert song.rating == test_rating

    new_title = "new_test_song"
    new_artist_id = 2
    new_album_id = 2
    new_genre = "new_test_genre"
    new_duration = 200
    new_play_count = 200
    new_favorite = False
    new_rating = 4

    updated_song = update_song(
        test_db_session,
        song,
        title=new_title,
        artist_id=new_artist_id,
        album_id=new_album_id,
        genre=new_genre,
        duration=new_duration,
        play_count=new_play_count,
        favorite=new_favorite,
        rating=new_rating,
    )
    assert updated_song is not None
    assert updated_song.title == new_title
    assert updated_song.artist_id == new_artist_id
    assert updated_song.album_id == new_album_id
    assert updated_song.genre == new_genre
    assert updated_song.duration == new_duration
    assert updated_song.play_count == new_play_count
    assert updated_song.favorite == new_favorite
    assert updated_song.rating == new_rating

    updated_song_in_db = (
        test_db_session.query(Song).filter_by(title=new_title).first()
    )
    assert updated_song_in_db is not None
    assert updated_song_in_db == updated_song


def test_update_song_failure(test_db_session):
    """노래 업데이트 실패 테스트"""
    test_title = "test_song"
    test_file_path = "test_file_path"
    test_artist_id = 1
    test_album_id = 1
    test_genre = "test_genre"
    test_duration = 100
    test_play_count = 100
    test_favorite = True
    test_rating = 5

    song = create_song(
        test_db_session,
        title=test_title,
        file_path=test_file_path,
        artist_id=test_artist_id,
        album_id=test_album_id,
        genre=test_genre,
        duration=test_duration,
        play_count=test_play_count,
        favorite=test_favorite,
        rating=test_rating,
    )

    with pytest.raises(ValueError):
        update_song(test_db_session, song, title="")

    with pytest.raises(ValueError):
        update_song(test_db_session, song, rating=6)

    with pytest.raises(ValueError):
        update_song(test_db_session, song, rating=0)


def test_delete_song(test_db_session):
    """노래 삭제 테스트"""
    test_title = "test_song"
    test_file_path = "test_file_path"
    test_artist_id = 1
    test_album_id = 1
    test_genre = "test_genre"
    test_duration = 100
    test_play_count = 100
    test_favorite = True
    test_rating = 5

    song = create_song(
        test_db_session,
        title=test_title,
        file_path=test_file_path,
        artist_id=test_artist_id,
        album_id=test_album_id,
        genre=test_genre,
        duration=test_duration,
        play_count=test_play_count,
        favorite=test_favorite,
        rating=test_rating,
    )
    assert song is not None
    assert song.title == test_title
    assert song.file_path == test_file_path
    assert song.artist_id == test_artist_id
    assert song.album_id == test_album_id
    assert song.genre == test_genre
    assert song.duration == test_duration
    assert song.play_count == test_play_count
    assert song.favorite == test_favorite
    assert song.rating == test_rating

    delete_song(test_db_session, song)

    found_song = (
        test_db_session.query(Song).filter_by(title=test_title).first()
    )
    assert found_song is None
