from pydantic import BaseModel
class user(BaseModel):
    id: int
    username: str
    hashed_password: str
    created_time: str
    updated_time: str


class booking(BaseModel):
    Booking_id: int
    user_id: int
    start_time: str
    end_time: str
    comment: str

