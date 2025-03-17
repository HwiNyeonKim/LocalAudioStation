import os
import sqlite3

import pytest

from app.database.config import reset_engine
from app.database.init_db import init_db


@pytest.fixture(scope="function")
def temp_db(monkeypatch):
    """테스트용 데이터베이스 파일을 생성/삭제하는 Fixture"""
    test_db_path = "test_local_audio_station.db"
    test_db_url = f"sqlite:///{test_db_path}"

    monkeypatch.setenv("DATABASE_URL", test_db_url)

    # 테스트 DB 파일이 이미 존재하면 삭제
    if os.path.exists(test_db_path):
        os.remove(test_db_path)

    engine, _ = reset_engine()

    init_db(engine)

    yield test_db_path  # 테스트 실행

    # 테스트 종료 후 Cleanup
    if os.path.exists(test_db_path):
        os.remove(test_db_path)


def test_init_db(temp_db):
    """init_db() 실행 후 테이블이 정상적으로 생성되는지 확인"""
    init_db()

    # SQLite 연결
    conn = sqlite3.connect(temp_db)
    cursor = conn.cursor()

    # 데이터베이스 내 테이블 목록 가져오기
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = {row[0] for row in cursor.fetchall()}

    expected_tables = {
        "Users",
        "Albums",
        "Artists",
        "Playlists",
        "Playlist_Songs",
        "Songs",
    }

    conn.close()

    assert expected_tables.issubset(
        tables
    ), f"Missing tables: {expected_tables - tables}"
