from sqlalchemy.orm import Session

from app.models import User


def create_user(db: Session, email: str, password_hash: str):
    """새로운 유저를 생성하고 데이터베이스에 저장한다.

    Args:
        db (Session)
        email (str)
        password (str): 해시된 비밀번호. 프론트쪽에서 해싱을 해서 보내는 것을 가정한다.
    """
    # 중복된 이메일이 있는지 확인
    if db.query(User).filter(User.email == email).first():
        raise ValueError("이미 존재하는 이메일")

    user = User(email=email, password_hash=password_hash)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


def get_user_by_email(db: Session, email: str):
    """이메일로 유저를 조회한다.

    Args:
        db (Session)
        email (str)
    Returns:
        User
    """
    return db.query(User).filter(User.email == email).first()


def update_user_email(db: Session, user: User, email: str):
    """유저의 이메일을 업데이트한다. 단, 중복이 있는 경우 Error를 발생시킨다.

    Args:
        db (Session)
        user (User)
        email (str)
    Returns:
        User
    """
    # 중복된 이메일이 있는지 확인
    if db.query(User).filter(User.email == email).first():
        raise ValueError("이미 존재하는 이메일")

    user.email = email
    db.commit()
    db.refresh(user)
    return user


def update_user_password(db: Session, user: User, password_hash: str):
    """유저의 비밀번호를 업데이트한다

    Args:
        db (Session)
        user (User)
        password (str)
    Returns:
        User
    """
    user.password_hash = password_hash
    db.commit()
    db.refresh(user)
    return user


def delete_user(db: Session, user: User):
    """유저를 삭제한다.

    Args:
        db (Session)
        user (User)
    """
    db.delete(user)
    db.commit()
