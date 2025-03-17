from app.models.user import User


def test_create_user(test_db_session):
    """User 테이블 데이터 삽입 테스트"""
    user = User(email="test@gmail.com", password_hash="password")
    test_db_session.add(user)
    test_db_session.commit()

    created_user = (
        test_db_session.query(User).filter_by(email="test@gmail.com").first()
    )
    assert created_user is not None
    assert created_user.email == "test@gmail.com"


def test_read_user(test_db_session):
    """User 테이블 데이터를 조회 테스트"""
    user = User(email="test2@gmail.com", password_hash="password")
    test_db_session.add(user)
    test_db_session.commit()

    read_user = (
        test_db_session.query(User).filter_by(email="test2@gmail.com").first()
    )
    assert read_user is not None
    assert read_user.email == "test2@gmail.com"


def test_update_user(test_db_session):
    """User 테이블 데이터 수정 테스트"""
    user = User(email="test3@gmail.com", password_hash="password")
    test_db_session.add(user)
    test_db_session.commit()

    user.password_hash = "new_password"
    test_db_session.commit()

    updated_user = (
        test_db_session.query(User).filter_by(email="test3@gmail.com").first()
    )
    assert updated_user.password_hash == "new_password"


def test_delete_user(test_db_session):
    """User 테이블 데이터 삭제 테스트"""
    user = User(email="test4@gmail.com", password_hash="password")
    test_db_session.add(user)
    test_db_session.commit()

    test_db_session.delete(user)
    test_db_session.commit()

    deleted_user = (
        test_db_session.query(User).filter_by(email="test4@gmail.com").first()
    )
    assert deleted_user is None
