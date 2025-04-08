import pytest

from app.models.artist import Artist

from ..artist import (
    create_artist,
    delete_artist,
    get_artist_by_id,
    get_artist_by_name,
    update_artist,
)


def test_create_artist(test_db_session):
    """아티스트 생성 테스트"""
    test_name = "test_artist"
    artist = create_artist(test_db_session, name=test_name)

    assert artist is not None
    assert artist.name == test_name

    created_artist = (
        test_db_session.query(Artist).filter_by(name=test_name).first()
    )
    assert created_artist is not None
    assert created_artist == artist


def test_create_artist_duplicate_name_failure(test_db_session):
    """아티스트 생성 실패 테스트 - 중복된 이름

    동일한 이름의 아티스트는 생성할 수 없다.
    """
    test_name = "test_artist"
    create_artist(test_db_session, name=test_name)

    with pytest.raises(ValueError):
        create_artist(test_db_session, name=test_name)


def test_get_artist_by_id(test_db_session):
    """아티스트 ID로 조회 테스트"""
    test_name = "test_artist"
    artist = create_artist(test_db_session, name=test_name)

    found_artist = get_artist_by_id(test_db_session, artist.id)
    assert found_artist is not None
    assert found_artist == artist


def test_get_artist_by_name(test_db_session):
    """아티스트 이름으로 조회 테스트"""
    test_name = "test_artist"
    artist = create_artist(test_db_session, name=test_name)

    found_artist = get_artist_by_name(test_db_session, test_name)
    assert found_artist is not None
    assert found_artist == artist


def test_update_artist(test_db_session):
    """아티스트 정보 업데이트 테스트"""
    test_name = "test_artist"
    artist = create_artist(test_db_session, name=test_name)

    new_name = "new_test_artist"
    updated_artist = update_artist(test_db_session, artist, name=new_name)

    assert updated_artist is not None
    assert updated_artist.name == new_name

    updated_artist_in_db = (
        test_db_session.query(Artist).filter_by(name=new_name).first()
    )
    assert updated_artist_in_db is not None
    assert updated_artist_in_db == updated_artist


def test_update_artist_failure(test_db_session):
    """아티스트 정보 업데이트 실패 테스트

    - 이름은 공란으로 만들 수 없다.
    """
    test_name = "test_artist"
    artist = create_artist(test_db_session, name=test_name)

    with pytest.raises(ValueError):
        update_artist(test_db_session, artist, name="")


def test_delete_artist(test_db_session):
    """아티스트 삭제 테스트"""
    test_name = "test_artist"
    artist = create_artist(test_db_session, name=test_name)

    delete_artist(test_db_session, artist)

    found_artist = (
        test_db_session.query(Artist).filter_by(name=test_name).first()
    )
    assert found_artist is None
