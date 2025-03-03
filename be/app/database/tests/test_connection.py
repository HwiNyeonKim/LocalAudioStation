"""
test_connection.py - connection.py에 대한 단위 테스트.

주요 테스트:
- init_database_connection()이 create_engine, sessionmaker를 호출하는지 확인
- singleton 확인 (동일 인스턴스 여부)
- 엔진/세션 초기화가 안 됐을 때 RuntimeError 발생 여부 확인
"""

import re
from unittest.mock import MagicMock, patch

import pytest

from app.database.config import DATABASE_URL
from app.database.connection import DatabaseConnectionManager


@patch("app.database.connection.create_engine")
def test_database_connection_manager_init(create_engine_mock):
    """init_database_connection()이 create_engine을 적절히 호출하는지 테스트"""
    database_connection_manager = DatabaseConnectionManager()
    database_connection_manager._engine = None

    database_connection_manager.init_database_connection()

    create_engine_mock.assert_called_once_with(url=DATABASE_URL, echo=True)


@patch("app.database.connection.create_engine")
@patch("app.database.connection.sessionmaker")
def test_session(sessionmaker_mock, create_engine_mock):
    """
    - sessionmaker가 올바르게 bind=mock_engine으로 호출되는지 테스트
    - get_session()이 해당 sessionmaker 결과를 반환하는지 테스트
    """
    engine_mock = MagicMock()
    create_engine_mock.return_value = engine_mock

    session_mock = MagicMock()
    sessionmaker_mock.return_value = session_mock

    database_connection_manager = DatabaseConnectionManager()
    database_connection_manager._engine = None
    database_connection_manager._session = None

    database_connection_manager.init_database_connection()

    sessionmaker_mock.assert_called_once_with(
        autocommit=False, autoflush=False, bind=engine_mock
    )

    session = database_connection_manager.get_session()
    assert session == session_mock


def test_singleton():
    """DatabaseConnectionManager가 정말로 singleton으로 동작하는지 테스트"""
    manager_1 = DatabaseConnectionManager()
    manager_2 = DatabaseConnectionManager()

    assert manager_1 is manager_2


def test_engine_before_init():
    """init_database_connection() 호출 이전 engine 접근시 RuntimeError 발생 테스트"""
    manager = DatabaseConnectionManager()
    manager._engine = None
    msg = "Database connection has not been initialized. Call init_database_connection() first"  # noqa
    with pytest.raises(RuntimeError, match=re.escape(msg)):
        _ = manager.engine


def test_get_session_before_init():
    """
    init_database_connection() 호출 이전 get_session 접근시 RuntimeError 발생 테스트
    """
    manager = DatabaseConnectionManager()
    manager._session = None
    msg = "Database connection has not been initialized. Call init_database_connection() first"  # noqa
    with pytest.raises(RuntimeError, match=re.escape(msg)):
        _ = manager.get_session()
