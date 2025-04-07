import os

import pytest

from app.database.config import reset_engine
from app.database.init_db import init_db


@pytest.fixture(scope="function")
def test_db(monkeypatch):
    test_db_path = "test_local_audio_station.db"
    test_db_url = f"sqlite:///{test_db_path}"

    monkeypatch.setenv("DATABASE_URL", test_db_url)

    # 테스트 DB 파일이 이미 존재하면 삭제
    if os.path.exists(test_db_path):
        os.remove(test_db_path)

    engine, session = reset_engine()

    init_db(engine)

    yield test_db_path, session  # 테스트 실행

    # 테스트 종료 후 Cleanup
    if os.path.exists(test_db_path):
        os.remove(test_db_path)


@pytest.fixture(scope="function")
def test_db_session(test_db):
    _, sessionmaker = test_db
    db_session = sessionmaker()
    yield db_session
    db_session.close()
