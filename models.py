from datetime import datetime
from sqlalchemy import Boolean, Column, Integer, String, DateTime, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URI = 'sqlite:///database.db'
Base = declarative_base()

class PhoneLog(Base):
    __tablename__ = 'phone_logs'
    
    id = Column(Integer, primary_key=True)
    input_number = Column(String, nullable=False)  # Store original input number
    sanitized_number = Column(String, nullable=False)  # Store sanitized number
    validated = Column(Boolean, nullable=False)  # Store validation status
    timestamp = Column(DateTime, default=datetime.utcnow)  # Automatically set the timestamp

def init_db(uri=DATABASE_URI):
    """Initialize the database and create tables."""
    engine = create_engine(uri)
    Base.metadata.create_all(engine)
    return sessionmaker(bind=engine)

# Create a session factory
Session = init_db()
