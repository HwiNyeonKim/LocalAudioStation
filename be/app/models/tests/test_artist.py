from ..artist import Artist


def test_create_artist(test_db_session):
    """Artist 테이블 데이터 삽입 테스트"""
    artist = Artist(name="test_artist")
    test_db_session.add(artist)
    test_db_session.commit()

    created_artist = (
        test_db_session.query(Artist).filter_by(name="test_artist").first()
    )
    assert created_artist is not None
    assert created_artist.name == "test_artist"


def test_read_artist(test_db_session):
    """Artist 테이블 데이터 조회 테스트"""
    artist = Artist(name="test_artist2")
    test_db_session.add(artist)
    test_db_session.commit()

    read_artist = (
        test_db_session.query(Artist).filter_by(name="test_artist2").first()
    )
    assert read_artist is not None
    assert read_artist.name == "test_artist2"


def test_update_artist(test_db_session):
    """Artist 테이블 데이터 수정 테스트"""
    artist = Artist(name="test_artist3")
    test_db_session.add(artist)
    test_db_session.commit()

    artist.name = "new_artist"
    test_db_session.commit()

    updated_artist = (
        test_db_session.query(Artist).filter_by(name="new_artist").first()
    )
    assert updated_artist is not None
    assert updated_artist.name == "new_artist"


def test_delete_artist(test_db_session):
    """Artist 테이블 데이터 삭제 테스트"""
    artist = Artist(name="test_artist4")
    test_db_session.add(artist)
    test_db_session.commit()

    test_db_session.delete(artist)
    test_db_session.commit()

    deleted_artist = (
        test_db_session.query(Artist).filter_by(name="test_artist4").first()
    )
    assert deleted_artist is None
