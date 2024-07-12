from datetime import date

from pydantic import BaseModel, ConfigDict


class SBooking(BaseModel):
    id: int
    room_id: int
    user_id: int
    date_from: date
    date_to: date
    price: int
    total_cost: int
    totals_days: int

    model_config = ConfigDict(from_attributes=True)


class SBookingRoom(SBooking):
    image_id: int
    name: str
    description: str | None
    services: list[str]

    model_config = ConfigDict(from_attributes=True)


class SNewBooking(BaseModel):
    room_id: int
    date_from: date
    date_to: date
