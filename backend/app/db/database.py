import databases

from sqlalchemy import create_engine

SQLALCHEMY_DATABASE_URL = "postgresql://postgres:123456@127.0.0.1/ecom"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={}
)
# metadata = sqlalchemy.MetaData()
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
database = databases.Database(SQLALCHEMY_DATABASE_URL)

