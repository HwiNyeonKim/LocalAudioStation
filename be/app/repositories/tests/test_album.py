import pytest

from app.models.album import Album
from app.models.artist import Artist

from ..album import (
    create_album,
    delete_album,
    get_album_by_artist_id,
    get_album_by_id,
    update_album,
)


@pytest.fixture
def test_artist(test_db_session):
    artist = Artist(name="test_artist")
    test_db_session.add(artist)
    test_db_session.commit()
    test_db_session.refresh(artist)
    return artist


def test_create_album_with_artist_id(test_db_session, test_artist):
    """앨범 생성 테스트 with artist_id"""
    test_title = "test_album"
    test_release_year = 2025
    album = create_album(
        test_db_session,
        title=test_title,
        artist_id=test_artist.id,
        release_year=test_release_year,
    )
    assert album is not None
    assert album.title == test_title
    assert album.artist_id == test_artist.id
    assert album.release_year == test_release_year

    created_album = (
        test_db_session.query(Album).filter_by(title=test_title).first()
    )
    assert created_album is not None
    assert created_album == album


def test_create_album_without_artist_id(test_db_session):
    """앨범 생성 테스트 without artist_id"""
    test_title = "test_album"
    test_release_year = 2025
    album = create_album(
        test_db_session,
        title=test_title,
        artist_id=None,
        release_year=test_release_year,
    )
    assert album is not None
    assert album.title == test_title
    assert album.artist_id is None
    assert album.release_year == test_release_year

    created_album = (
        test_db_session.query(Album).filter_by(title=test_title).first()
    )
    assert created_album is not None
    assert created_album == album


def test_get_album_by_id(test_db_session, test_artist):
    """앨범 조회 테스트"""
    test_title_1 = "test_album_1"
    test_release_year = 2025
    album_1 = create_album(
        test_db_session,
        title=test_title_1,
        artist_id=test_artist.id,
        release_year=test_release_year,
    )

    test_title_2 = "test_album_2"
    test_release_year = 2024
    album_2 = create_album(
        test_db_session,
        title=test_title_2,
        artist_id=None,
        release_year=test_release_year,
    )

    found_album_1 = get_album_by_id(test_db_session, album_1.id)
    assert found_album_1 is not None
    assert found_album_1 == album_1

    found_album_2 = get_album_by_id(test_db_session, album_2.id)
    assert found_album_2 is not None
    assert found_album_2 == album_2


def test_get_album_by_artist_id(test_db_session, test_artist):
    """아티스트의 앨범 조회 테스트"""
    test_title_1 = "test_album_1"
    test_release_year = 2025
    album_1 = create_album(
        test_db_session,
        title=test_title_1,
        artist_id=test_artist.id,
        release_year=test_release_year,
    )

    test_title_2 = "test_album_2"
    test_release_year = 2024
    album_2 = create_album(
        test_db_session,
        title=test_title_2,
        artist_id=test_artist.id,
        release_year=test_release_year,
    )

    test_title_3 = "test_album_3"
    test_release_year = 2023
    album_3 = create_album(
        test_db_session,
        title=test_title_3,
        artist_id=None,
        release_year=test_release_year,
    )

    found_albums = get_album_by_artist_id(test_db_session, test_artist.id)
    assert found_albums is not None
    assert len(found_albums) == 2
    assert album_1 in found_albums
    assert album_2 in found_albums
    assert album_3 not in found_albums


def test_update_album(test_db_session, test_artist):
    """앨범 정보 업데이트 테스트"""
    test_title = "test_album"
    test_release_year = 2025
    album = create_album(
        test_db_session,
        title=test_title,
        artist_id=test_artist.id,
        release_year=test_release_year,
    )

    new_title = "new_test_album"
    new_artist_id = None
    updated_album = update_album(
        test_db_session,
        album,
        title=new_title,
        artist_id=new_artist_id,
        release_year=None,
    )

    assert updated_album is not None
    assert updated_album.title == new_title
    assert updated_album.artist_id == new_artist_id
    assert updated_album.release_year == album.release_year

    updated_album_in_db = (
        test_db_session.query(Album).filter_by(title=new_title).first()
    )
    assert updated_album_in_db is not None
    assert updated_album_in_db == updated_album


def test_update_album_failure(test_db_session, test_artist):
    """앨범 정보 업데이트 실패 테스트

    - title, artist_id, release_year 중 적어도 하나는 존재해야 한다.
    """
    test_title = "test_album"
    test_release_year = 2025
    album = create_album(
        test_db_session,
        title=test_title,
        artist_id=test_artist.id,
        release_year=test_release_year,
    )

    with pytest.raises(ValueError):
        update_album(
            test_db_session,
            album,
            title=None,
            artist_id=None,
            release_year=None,
        )


def test_delete_album(test_db_session, test_artist):
    """앨범 삭제 테스트"""
    test_title = "test_album"
    test_release_year = 2025
    album = create_album(
        test_db_session,
        title=test_title,
        artist_id=test_artist.id,
        release_year=test_release_year,
    )

    delete_album(test_db_session, album)

    albums_exist = test_db_session.query(Album)
    assert album not in albums_exist
