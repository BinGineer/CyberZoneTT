from fastapi import FastAPI, Depends
import uvicorn
import crud
import schemas
from database import User, Booking, SessionLocal, engine, Base, get_db
from sqlalchemy.orm import Session
app = FastAPI()
Base.metadata.create_all(bind=engine)



@app.get('/')
def hello():
    return "hello"

@app.post('/registration', response_model=schemas.user)
def create_user_f(user: schemas.user, db: Session = Depends(get_db)):
    return crud.create_user(db=db, user=user)

@app.post('/reg_booking', response_model=schemas.booking)
def reg_booking_f(db: Session, booking: schemas.booking):
    return crud.reg_booking(db=db, booking=booking)

@app.get("/users/", response_model=list[schemas.user])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users

@app.get("/users/{user_id}", response_model=schemas.user)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    return db_user

@app.get("/bookings", response_model=schemas.booking)
def get_bookings(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    db_bookings = crud.get_bookings(db, skip=skip, limit=limit)
    return db_bookings

@app.delete('/delete_booking')
def del_bookings(booking_id: int, db: Session = Depends(get_db)):
    db_bookings = crud.delete_booking(db = db, booking_id=booking_id)
    return db_bookings

@app.delete('/delete_user')
def delete_user(user_id: int, db: Session = Depends(get_db)):
    del_user = crud.delete_user(db = db, user_id = user_id)
    return del_user



if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
