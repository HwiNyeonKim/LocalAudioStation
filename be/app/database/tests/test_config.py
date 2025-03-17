from sqlalchemy import text

from ..config import SessionLocal, engine


def test_database_connection():
    """데이터베이스 연결이 정상적으로 이루어지는지 테스트"""
    try:
        with engine.connect() as connection:
            result = connection.execute(text("SELECT 1"))
            assert result.fetchone() == (1,)
    except Exception as e:
        assert False, f"Database connection failed: {e}"


def test_session_creation():
    """데이터베이스 세션이 정상적으로 생성되고 닫히는지 테스트"""
    db = SessionLocal()
    try:
        assert db is not None
    finally:
        db.close()
