from app.core.database import SessionLocal
from app.core.security import hash_password
from app.models.enums import Role
from app.models.user import User


def seed() -> None:
    db = SessionLocal()
    try:
        if not db.query(User).filter(User.email == "admin@screener.local").first():
            db.add(User(email="admin@screener.local", hashed_password=hash_password("admin123"), role=Role.ADMIN))
            db.commit()
    finally:
        db.close()


if __name__ == "__main__":
    seed()
