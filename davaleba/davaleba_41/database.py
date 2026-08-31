from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker


engine = create_engine("postgresql://postgres:1810@localhost:5432/pp-38")


class Base(DeclarativeBase):
    pass


SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False
)


def get_session():
    session = SessionLocal()

    try:
        yield session
    finally:
        session.close()