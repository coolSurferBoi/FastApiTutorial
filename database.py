from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

SQLALCHEMY_DATABASE_URL = "sqlite:///./blog.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread":False}
)

SessionLocal = sessionmaker(autocommit=False, autoflush = False, bind = engine)

class Base(DeclarativeBase):
    """
    Base class for all SQLAlchemy ORM models.

    Any database table in this project should be defined by creating a class
    that inherits from this Base class.

    Example:
        class Post(Base):
            __tablename__ = "posts"
            id = Column(Integer, primary_key=True)
            title = Column(String)

    SQLAlchemy uses this Base class to:
    - Keep track of all ORM models
    - Know which tables exist
    - Create database tables when needed

    You usually do not put any code inside this class.
    """
    pass

def get_db():
    """
    Create and provide a database session for a single request.

    This function is used by FastAPI's dependency system.
    When a route asks for a database session, FastAPI will:

    1. Open a new database session
    2. Pass the session to the route function
    3. Automatically close the session after the request finishes

    The `yield` keyword allows FastAPI to safely clean up the session,
    even if an error occurs during the request.

    Returns:
        A SQLAlchemy Session object that can be used to query or modify
        the database.
    """
    with SessionLocal() as db:
        yield db