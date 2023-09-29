from sqlalchemy import create_engine, Column, Integer,DateTime, func, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

SQLALCHEMY_DATABASE_URL = "postgresql://postgres:1@localhost:5432/book"
engine = create_engine(SQLALCHEMY_DATABASE_URL, pool_pre_ping=True)
SessionLocal = sessionmaker(autocommit=True, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal
    try:
        yield db
    finally:
        db.close()


class User(Base):
    __tablename__ = 'Users'
    id = Column(Integer, primary_key=True)
    username = Column(String, nullable=False)
    hashed_password = Column(String, nullable=False)
    created_time = Column(DateTime(timezone=True), server_default=func.now())
    updated_time = Column(DateTime(timezone=True), onupdate=func.now())
    bookings = relationship("Booking", back_populates="owner")


class Booking(Base):
    __tablename__ = 'Bookings'
    Booking_id = Column(Integer, primary_key=True)
    user_id = Column(ForeignKey('Users.id'))
    start_time = Column(String, nullable=False)
    end_time = Column(String, nullable=False)
    owner = relationship("User", back_populates="booking")
    comment = Column(String, default='')

