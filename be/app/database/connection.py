"""
connection.py - DB 연결 및 세션관리를 담당

제공 기능:
- SQLAlchemy 엔진 생성
- 세션 팩토리(sessionmaker) 생성
- 엔진, 세션 팩토리를 전달하는 메서드

예외 발생:
- DB 연결을 초기화 하기 전에 engine, get_session 호출시 RuntimeError 발생
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from .config import DATABASE_URL


class DatabaseConnectionManager:
    """DB 연결(engine)과 세션을 singleton으로 관리하는 클래스

    Attributes:
    - _instance: DatabaseConnectionManager Singleton Instance
    - _engine: SQLAlchemy engine 객체
    - _session: sessionmaker로 만든 세션 팩토리

    Example:
        from database import database_connection_manager

        database_connection_manager.init_database_connection()

        engine = database_connection_manager.engine()
        session database_connection_manager.get_session()
    """

    _instance = None
    _engine = None
    _session = None

    def __new__(cls):
        """Singleton 패턴을 구현하기 위한 __new__ 메서드 오버라이드

        Returns:
            DatabaseConnectionManager: 이 클래스의 Singleton Instance
        """

        if cls._instance is None:
            cls._instance = super().__new__(cls)

        return cls._instance

    def init_database_connection(
        self, url: str = DATABASE_URL, echo: bool = True
    ):
        """DB 연결을 초기화. 이미 초기화 되어 있으면 아무런 추가 동작을 하지 않는다.

        Args:
            url (str, optional): DB 접속용 URL. Defaults to DATABASE_URL.
            echo (bool, optional): SQL문 로깅 여부. Defaults to True.
        """

        if self._engine is None:
            self._engine = create_engine(url=url, echo=echo)

        if self._session is None:
            self._session = sessionmaker(
                autocommit=False, autoflush=False, bind=self._engine
            )

    @property
    def engine(self):
        """SQLAlchemy engine 객체

        Returns:
            sqlalchemy.engine.Engine

        Raises:
            RuntimeError: raised if accessed when _engine is not initialzed.
        """

        if self._engine is None:
            # TODO: Custom Excpetion Layer 도입
            raise RuntimeError(
                "Database connection has not been initialized. Call init_database_connection() first"  # noqa
            )

        return self._engine

    def get_session(self):
        """세션 팩토리(sessionmaker) 객체 를 반환

        Returns:
            sqlalchemy.orm.session.sessionmaker

        Yields:
            sqlalchemy.orm.session.Session

        Raises:
            RuntimeError: raised if called when _session is not initialzed.
        """

        if self._session is None:
            raise RuntimeError(
                "Database connection has not been initialized. Call init_database_connection() first"  # noqa
            )

        return self._session


database_connection_manager = DatabaseConnectionManager()
