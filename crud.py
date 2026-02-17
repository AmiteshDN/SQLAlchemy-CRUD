from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from models import User


def create_user(session: Session, username: str, email: str, full_name: str | None = None) -> User:
    user = User(username=username, email=email, full_name=full_name)
    session.add(user)
    try:
        session.commit()
        session.refresh(user)
        return user
    except IntegrityError:
        session.rollback()
        raise


def get_user(session: Session, user_id: int) -> User | None:
    return session.get(User, user_id)


def get_user_by_username(session: Session, username: str) -> User | None:
    return session.query(User).filter_by(username=username).first()


def list_users(session: Session) -> list[User]:
    return session.query(User).order_by(User.id).all()


def update_user(session: Session, user_id: int, **kwargs) -> User | None:
    user = session.get(User, user_id)
    if not user:
        return None
    for k, v in kwargs.items():
        if hasattr(user, k):
            setattr(user, k, v)
    session.add(user)
    session.commit()
    session.refresh(user)
    return user


def delete_user(session: Session, user_id: int) -> bool:
    user = session.get(User, user_id)
    if not user:
        return False
    session.delete(user)
    session.commit()
    return True
