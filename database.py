from dotenv import load_dotenv
import os
from sqlalchemy import create_engine, Column, Integer, String, DateTime
from datetime import datetime
from sqlalchemy.orm import sessionmaker, declarative_base

# Load .env from the script's directory
env_file = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(env_file)

DATABASE_URL = os.getenv("DATABASE_URL")

if not DATABASE_URL:
    raise ValueError("DATABASE_URL not found in environment variables. Check your .env file.")

# Lazy initialization - create engine only when needed
engine = None
SessionLocal = None
Base = declarative_base()

def get_engine():
    global engine
    if engine is None:
        engine = create_engine(DATABASE_URL)
    return engine

def get_session_local():
    global SessionLocal
    if SessionLocal is None:
        SessionLocal = sessionmaker(bind=get_engine())
    return SessionLocal
class Notemodel(Base):
    __tablename__ = "notes"
    id = Column(Integer, primary_key=True)
    title = Column(String, index=True)
    content = Column(String)
    summary = Column(String, nullable=True)
    created_at = Column(DateTime, default=datetime.now)

def init_db():
    Base.metadata.create_all(bind=get_engine())

def get_db():
    session_local = get_session_local()
    db = session_local()
    try:
        yield db
    finally:
        db.close()