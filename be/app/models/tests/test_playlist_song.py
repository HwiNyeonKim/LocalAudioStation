from ..playlist_song import PlaylistSong


def test_create_playlist_song(test_db_session):
    """PlaylistSong 테이블 데이터 삽입 테스트"""
    playlist_song = PlaylistSong(playlist_id=1, song_id=1)
    test_db_session.add(playlist_song)
    test_db_session.commit()

    created_playlist_song = (
        test_db_session.query(PlaylistSong)
        .filter_by(playlist_id=1, song_id=1)
        .first()
    )
    assert created_playlist_song is not None
    assert created_playlist_song.playlist_id == 1
    assert created_playlist_song.song_id == 1


def test_read_playlist_song(test_db_session):
    """PlaylistSong 테이블 데이터 조회 테스트"""
    playlist_song = PlaylistSong(playlist_id=2, song_id=2)
    test_db_session.add(playlist_song)
    test_db_session.commit()

    read_playlist_song = (
        test_db_session.query(PlaylistSong)
        .filter_by(playlist_id=2, song_id=2)
        .first()
    )
    assert read_playlist_song is not None
    assert read_playlist_song.playlist_id == 2
    assert read_playlist_song.song_id == 2


def test_update_playlist_song(test_db_session):
    """PlaylistSong 테이블 데이터 수정 테스트"""
    playlist_song = PlaylistSong(playlist_id=3, song_id=3)
    test_db_session.add(playlist_song)
    test_db_session.commit()

    playlist_song.song_id = 4
    test_db_session.commit()

    updated_playlist_song = (
        test_db_session.query(PlaylistSong)
        .filter_by(playlist_id=3, song_id=4)
        .first()
    )
    assert updated_playlist_song is not None
    assert updated_playlist_song.playlist_id == 3
    assert updated_playlist_song.song_id == 4


def test_delete_playlist_song(test_db_session):
    """PlaylistSong 테이블 데이터 삭제 테스트"""
    playlist_song = PlaylistSong(playlist_id=3, song_id=3)
    test_db_session.add(playlist_song)
    test_db_session.commit()

    test_db_session.delete(playlist_song)
    test_db_session.commit()

    deleted_playlist_song = (
        test_db_session.query(PlaylistSong)
        .filter_by(playlist_id=3, song_id=3)
        .first()
    )
    assert deleted_playlist_song is None
