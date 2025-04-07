import pytest

from app.models.playlist_song import PlaylistSong

from ..playlist_song import (
    create_playlist_song,
    delete_playlist_song,
    get_playlist_songs_by_playlist_id,
)


def test_create_playlist_song(test_db_session):
    """플레이리스트에 노래 추가 테스트"""
    playlist_id = 1
    song_id = 1
    playlist_song = create_playlist_song(
        test_db_session, playlist_id=playlist_id, song_id=song_id
    )

    assert playlist_song is not None
    assert playlist_song.playlist_id == playlist_id
    assert playlist_song.song_id == song_id

    created_playlist_song = (
        test_db_session.query(PlaylistSong)
        .filter_by(playlist_id=playlist_id, song_id=song_id)
        .first()
    )
    assert created_playlist_song is not None
    assert created_playlist_song == playlist_song


def test_get_playlist_songs_by_playlist_id(test_db_session):
    """플레이리스트 ID로 노래 목록 조회 테스트"""
    playlist_id = 1
    song_id1 = 1
    song_id2 = 2

    playlist_song1 = create_playlist_song(
        test_db_session, playlist_id=playlist_id, song_id=song_id1
    )
    playlist_song2 = create_playlist_song(
        test_db_session, playlist_id=playlist_id, song_id=song_id2
    )

    playlist_songs = get_playlist_songs_by_playlist_id(
        test_db_session, playlist_id
    )

    assert len(playlist_songs) == 2
    assert playlist_song1 in playlist_songs
    assert playlist_song2 in playlist_songs


def test_delete_playlist_song(test_db_session):
    """플레이리스트에서 노래 삭제 테스트"""
    playlist_id = 1
    song_id = 1
    playlist_song = create_playlist_song(
        test_db_session, playlist_id=playlist_id, song_id=song_id
    )

    delete_playlist_song(test_db_session, playlist_song)

    found_playlist_song = (
        test_db_session.query(PlaylistSong)
        .filter_by(playlist_id=playlist_id, song_id=song_id)
        .first()
    )
    assert found_playlist_song is None
