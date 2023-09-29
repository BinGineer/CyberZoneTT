from sqlalchemy.orm import Session

import schemas
from database import User
import database
import main
def create_user(db: Session, user: schemas.user):
    hashed = user.hashed_password+'hash'
    db_user = database.User(
                            username=user.username,
                            hashed_password=hashed
                            )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def reg_booking(db: Session, booking: schemas.booking, user_id: int):
    db_bookig = database.Booking(
                                user_id=user_id,
                                comment=booking.comment,
                                start_time=booking.start_time,
                                end_time=booking.end_time,
                                owner=user_id
                                )
    db.add(db_bookig)
    db.commit()
    db.refresh(db_bookig)
    return db_bookig

def get_bookings(db: Session, skip: int = 0, limit: int = 100):
    return db.query(database.Booking).offset(skip).limit(limit).all

def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(database.User).offset(skip).limit(limit).all()

def get_user(db: Session, user_id: int):
    return db.query(database.User).filter(database.User.id == user_id).first()

def delete_booking(db: Session, booking_id: int):
    book = db.query(database.Booking).filter(database.Booking.Booking_id == booking_id).delete()
    db.commit()
    return book

def delete_user(db: Session, user_id: int):
    delete_book = db.query(database.Booking).filter(database.Booking.owner == user_id).first()
    while delete_book is not None:
        delete_book = db.query(database.Booking).filter(database.Booking.owner == user_id).delete()
        db.commit()
        db.refresh()
        delete_book = db.query(database.Booking).filter(database.Booking.owner == user_id).first()
    delete_user = db.query(database.User).filter(database.User.user_id == user_id).delete()
    db.commit()
    return delete_user

