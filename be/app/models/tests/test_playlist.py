from app.models.playlist import Playlist


def test_create_playlist(test_db_session):
    """Playlist 테이블 데이터 삽입 테스트"""
    playlist = Playlist(name="test_playlist", user_id=1)
    test_db_session.add(playlist)
    test_db_session.commit()

    created_playlist = (
        test_db_session.query(Playlist).filter_by(name="test_playlist").first()
    )
    assert created_playlist is not None
    assert created_playlist.name == "test_playlist"
    assert created_playlist.user_id == 1


def test_read_playlist(test_db_session):
    """Playlist 테이블 데이터를 조회 테스트"""
    playlist = Playlist(name="test_playlist2", user_id=2)
    test_db_session.add(playlist)
    test_db_session.commit()

    read_playlist = (
        test_db_session.query(Playlist)
        .filter_by(name="test_playlist2")
        .first()
    )
    assert read_playlist is not None
    assert read_playlist.name == "test_playlist2"
    assert read_playlist.user_id == 2


def test_update_playlist(test_db_session):
    """Playlist 테이블 데이터 수정 테스트"""
    playlist = Playlist(name="test_playlist3", user_id=3)
    test_db_session.add(playlist)
    test_db_session.commit()

    playlist.name = "new_playlist"
    test_db_session.commit()

    updated_playlist = (
        test_db_session.query(Playlist).filter_by(name="new_playlist").first()
    )
    assert updated_playlist is not None
    assert updated_playlist.name == "new_playlist"


def test_delete_playlist(test_db_session):
    """Playlist 테이블 데이터 삭제 테스트"""
    playlist = Playlist(name="test_playlist4", user_id=4)
    test_db_session.add(playlist)
    test_db_session.commit()

    test_db_session.delete(playlist)
    test_db_session.commit()

    deleted_playlist = (
        test_db_session.query(Playlist)
        .filter_by(name="test_playlist4")
        .first()
    )
    assert deleted_playlist is None
