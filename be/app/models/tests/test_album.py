from ..album import Album


def test_create_album(test_db_session):
    """Album 테이블 데이터 삽입 테스트"""
    album = Album(title="test_album", artist_id=1)
    test_db_session.add(album)
    test_db_session.commit()

    created_album = (
        test_db_session.query(Album).filter_by(title="test_album").first()
    )
    assert created_album is not None
    assert created_album.title == "test_album"
    assert created_album.artist_id == 1


def test_read_album(test_db_session):
    """Album 테이블 데이터 조회 테스트"""
    album = Album(title="test_album2", artist_id=2)
    test_db_session.add(album)
    test_db_session.commit()

    read_album = (
        test_db_session.query(Album).filter_by(title="test_album2").first()
    )
    assert read_album is not None
    assert read_album.title == "test_album2"
    assert read_album.artist_id == 2


def test_update_album(test_db_session):
    """Album 테이블 데이터 수정 테스트"""
    album = Album(title="test_album3", artist_id=3)
    test_db_session.add(album)
    test_db_session.commit()

    album.title = "new_album"
    test_db_session.commit()

    updated_album = (
        test_db_session.query(Album).filter_by(title="new_album").first()
    )
    assert updated_album is not None
    assert updated_album.title == "new_album"


def test_delete_album(test_db_session):
    """Album 테이블 데이터 삭제 테스트"""
    album = Album(title="test_album4", artist_id=4)
    test_db_session.add(album)
    test_db_session.commit()

    test_db_session.delete(album)
    test_db_session.commit()

    deleted_album = (
        test_db_session.query(Album).filter_by(title="test_album4").first()
    )
    assert deleted_album is None
