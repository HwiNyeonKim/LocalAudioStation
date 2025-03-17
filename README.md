# Local Audio Staiton

## 프로젝트 정보

로컬(기기 또는 네트워크 내) 음악 파일들을 웹에서 쉽게 스트리밍 및 관리할 수 있도록 하는 프로젝트

- Synology NAS 사용 중단에 따른 Synology Audio Station의 대체재를 만들어 본다

## 주요 기능 (예정)

- **🎧 음악 스트리밍**: 로컬(기기 또는 네트워크)에 있는 음악 파일들을 웹에서 바로 재생
- **📋 음악 관리**: 음악의 확인/추가/제거 및 아티스트, 앨범, 장르 등의 분류에 맞추어 음악을 관리
  - 실행환경의 로컬 디렉토리에 저장되어 있는 음악을 자동으로 스캔하여 DB에 저장
- **🥰 즐겨찾기 & 평가**: 음악의 Favorite 및 Rating 관리
- **🎶 플레이리스트**: 플레이리스트 생성/편집/삭제
- **▶️ 다양한 재생 방식**: 순차 재생, 랜덤 재생, Top 100 재생, 즐겨찾기만 재생, 특정 Rating 이상만 재생 등 다양한 방식으로 음악을 재생

## 기술 스택

- **FE**: 추후 결정
- **BE**: FastAPI, SQLite, SQLAlchemy
- **Deployment**: Docker (별도의 배포는 하지 않고 로컬에서 직접 실행)

## 설치 및 실행 방법 (예정)

1. Clone Project

    ```bash
    git clone https://github.com/HwiNyeonKim/LocalAudioStation.git
    cd LocalAudioStation
    ```

2. Run BE

    ```bash
    cd ../be
    poetry install
    poetry run uvicorn app.main:app --reload
    ```

3. Run FE

    **TBD**
