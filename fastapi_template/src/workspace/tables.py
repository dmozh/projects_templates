from .settings import settings


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


engine = create_engine(
    settings.database_url_dev,
    connect_args={'check_same_thread': False},
)

Session = sessionmaker(
    engine,
    autocommit=False,
    autoflush=False,
)


def get_session() -> Session:
    session = Session()
    try:
        yield session
    finally:
        session.close()