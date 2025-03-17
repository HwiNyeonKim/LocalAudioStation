from app.models.song import Song


def test_create_song(test_db_session):
    """Song 테이블 데이터 삽입 테스트"""
    song = Song(title="test_song", duration=100, file_path="test_path")
    test_db_session.add(song)
    test_db_session.commit()

    created_song = (
        test_db_session.query(Song).filter_by(title="test_song").first()
    )
    assert created_song is not None
    assert created_song.title == "test_song"


def test_read_song(test_db_session):
    """Song 테이블 데이터를 조회 테스트"""
    song = Song(title="test_song2", duration=100, file_path="test_path")
    test_db_session.add(song)
    test_db_session.commit()

    read_song = (
        test_db_session.query(Song).filter_by(title="test_song2").first()
    )
    assert read_song is not None
    assert read_song.title == "test_song2"


def test_update_song(test_db_session):
    """Song 테이블 데이터 수정 테스트"""
    song = Song(title="test_song3", duration=100, file_path="test_path")
    test_db_session.add(song)
    test_db_session.commit()

    song.duration = 200
    test_db_session.commit()

    updated_song = (
        test_db_session.query(Song).filter_by(title="test_song3").first()
    )
    assert updated_song.duration == 200


def test_delete_song(test_db_session):
    """Song 테이블 데이터 삭제 테스트"""
    song = Song(title="test_song3", duration=100, file_path="test_path")
    test_db_session.add(song)
    test_db_session.commit()

    test_db_session.delete(song)
    test_db_session.commit()

    deleted_song = (
        test_db_session.query(Song).filter_by(title="test_song4").first()
    )
    assert deleted_song is None
