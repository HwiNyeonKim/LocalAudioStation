import os

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

load_dotenv()


def get_database_url():
    return os.getenv("DATABASE_URL")


engine = create_engine(
    get_database_url(), connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def reset_engine():
    """일단 테스트용으로만 사용한다."""
    global engine, SessionLocal
    engine.dispose()
    url = get_database_url()
    engine = create_engine(url, connect_args={"check_same_thread": False})
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    return engine, SessionLocal


Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
