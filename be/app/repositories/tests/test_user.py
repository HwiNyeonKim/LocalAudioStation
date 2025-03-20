import pytest

from app.models.user import User

from ..user import (
    create_user,
    delete_user,
    get_user_by_email,
    update_user_email,
    update_user_password,
)


def test_create_user(test_db_session):
    """신규 유저 생성 테스트"""
    test_email = "test@gmail.com"
    test_password_hash = "password_hash"
    user = create_user(
        test_db_session, email=test_email, password_hash=test_password_hash
    )
    assert user is not None
    assert user.email == test_email
    assert user.password_hash == test_password_hash

    created_user = (
        test_db_session.query(User).filter_by(email=test_email).first()
    )
    assert created_user is not None
    assert created_user == user


def test_create_user_fail_email_duplicated(test_db_session):
    """이메일 중복 유저 생성 실패 테스트"""
    test_email = "duplicate@gmail.com"
    test_password_hash = "password_hash"
    create_user(
        test_db_session, email=test_email, password_hash=test_password_hash
    )

    with pytest.raises(ValueError):
        create_user(
            test_db_session, email=test_email, password_hash=test_password_hash
        )


def test_delete_user(test_db_session):
    """유저 삭제 테스트"""
    test_email = "test2@gmail.com"
    test_password_hash = "password_hash"
    user = create_user(
        test_db_session, email=test_email, password_hash=test_password_hash
    )

    created_user = (
        test_db_session.query(User).filter_by(email=test_email).first()
    )
    assert created_user is not None
    assert created_user == user

    delete_user(test_db_session, user)

    users_exist = test_db_session.query(User)
    assert user not in users_exist


def test_get_user_by_email(test_db_session):
    """이메일로 유저 조회 테스트"""
    test_email = "test3@gmail.com"
    test_password_hash = "password_hash"
    user = create_user(
        test_db_session, email=test_email, password_hash=test_password_hash
    )

    found_user = get_user_by_email(test_db_session, test_email)
    assert found_user is not None
    assert found_user == user


def test_update_user_email(test_db_session):
    """유저 이메일 변경 테스트"""
    test_email = "test4@gmail.com"
    test_password_hash = "password_hash"
    user = create_user(
        test_db_session, email=test_email, password_hash=test_password_hash
    )

    new_email = "new_test4@gmail.com"
    updated_user = update_user_email(test_db_session, user, new_email)

    assert updated_user is not None
    assert updated_user.email == new_email

    # Check database: user 테이블에 데이터가 잘 들어갔는지 확인
    updated_user_in_db = (
        test_db_session.query(User).filter_by(email=new_email).first()
    )
    assert updated_user_in_db is not None
    assert updated_user_in_db == updated_user


def test_update_user_email_fail_email_duplicated(test_db_session):
    """이메일 변경 실패 테스트(중복 이메일)"""
    test_email_1 = "test5_1@gmail.com"
    test_password_hash = "password_hash"
    user = create_user(
        test_db_session, email=test_email_1, password_hash=test_password_hash
    )

    test_email_2 = "test5_2@gmail.com"
    create_user(
        test_db_session, email=test_email_2, password_hash=test_password_hash
    )

    with pytest.raises(ValueError):
        update_user_email(test_db_session, user, test_email_2)


def test_update_user_password(test_db_session):
    """유저 비밀번호 변경 테스트"""
    test_email = "test6@gmail.com"
    test_password_hash = "password_hash"
    user = create_user(
        test_db_session, email=test_email, password_hash=test_password_hash
    )

    new_password_hash = "new_password_hash"
    updated_user = update_user_password(
        test_db_session, user, new_password_hash
    )

    assert updated_user is not None
    assert updated_user.password_hash == new_password_hash

    updated_user_in_db = (
        test_db_session.query(User).filter_by(email=test_email).first()
    )
    assert updated_user_in_db is not None
    assert updated_user_in_db.password_hash == new_password_hash
