"""
database 패키지: DB 연결 및 설정을 관리

제공 기능:
- 데이터베이스 관련 설정(환경변수)
- 데이터베이스 연결

구성 요소:
- `config.py`: .env 파일에 설정된 DB 관련 환경변수를 로드
- `connection.py`: Singleton DB Connection Manager 제공
"""

from .connection import database_connection_manager

__all__ = ["database_connection_manager"]
