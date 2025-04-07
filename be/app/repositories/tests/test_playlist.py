import pytest

from app.repositories.playlist import (
    create_playlist,
    delete_playlist,
    get_playlist_by_id,
    get_playlists_by_user_id,
    update_playlist,
)


def test_create_playlist(test_db_session):
    """플레이리스트 생성 테스트"""
    # 새로운 플레이리스트 생성
    user_id = 1
    name = "My Playlist"
    playlist = create_playlist(test_db_session, user_id=user_id, name=name)

    # 생성된 플레이리스트 검증
    assert playlist.user_id == user_id
    assert playlist.name == name


def test_create_playlist_with_empty_name(test_db_session):
    """빈 이름으로 플레이리스트 생성 시 예외 발생 테스트"""
    # 빈 이름으로 플레이리스트 생성 시도
    with pytest.raises(ValueError):
        create_playlist(test_db_session, user_id=1, name="")


def test_get_playlist_by_id(test_db_session):
    """ID로 플레이리스트 조회 테스트"""
    # 테스트용 플레이리스트 생성
    playlist = create_playlist(
        test_db_session, user_id=1, name="Test Playlist"
    )

    # ID로 플레이리스트 조회
    found = get_playlist_by_id(test_db_session, playlist.id)

    # 조회된 플레이리스트 검증
    assert found is not None
    assert found.id == playlist.id
    assert found.name == playlist.name


def test_get_playlist_by_id_not_found(test_db_session):
    """존재하지 않는 ID로 플레이리스트 조회 테스트"""
    # 존재하지 않는 ID로 조회
    found = get_playlist_by_id(test_db_session, playlist_id=999)

    # 결과가 None인지 검증
    assert found is None


def test_get_playlists_by_user_id(test_db_session):
    """사용자 ID로 플레이리스트 목록 조회 테스트"""
    # 테스트용 플레이리스트 생성
    user_id = 1
    playlist1 = create_playlist(
        test_db_session, user_id=user_id, name="Playlist 1"
    )
    playlist2 = create_playlist(
        test_db_session, user_id=user_id, name="Playlist 2"
    )

    # 사용자 ID로 플레이리스트 목록 조회
    playlists = get_playlists_by_user_id(test_db_session, user_id)

    # 조회된 플레이리스트 목록 검증
    assert len(playlists) == 2
    assert playlist1 in playlists
    assert playlist2 in playlists


def test_update_playlist(test_db_session):
    """플레이리스트 정보 업데이트 테스트"""
    # 테스트용 플레이리스트 생성
    playlist = create_playlist(
        test_db_session, user_id=1, name="Original Name"
    )
    new_name = "Updated Name"

    # 플레이리스트 정보 업데이트
    updated = update_playlist(
        test_db_session, playlist=playlist, name=new_name
    )

    # 업데이트된 정보 검증
    assert updated.name == new_name


def test_update_playlist_with_empty_name(test_db_session):
    """빈 이름으로 플레이리스트 업데이트 시 예외 발생 테스트"""
    # 테스트용 플레이리스트 생성
    playlist = create_playlist(
        test_db_session, user_id=1, name="Original Name"
    )

    with pytest.raises(ValueError):
        update_playlist(test_db_session, playlist=playlist, name="")


def test_delete_playlist(test_db_session):
    """플레이리스트 삭제 테스트"""
    # 테스트용 플레이리스트 생성
    playlist = create_playlist(
        test_db_session, user_id=1, name="To Be Deleted"
    )

    # 플레이리스트 삭제
    delete_playlist(test_db_session, playlist)
