from datetime import date, datetime, timedelta

from fastapi import APIRouter, Query

from app.hotels.dao import HotelDAO
from app.hotels.schemas import SHotel, SHotelInfo

router = APIRouter(prefix="/hotels", tags=["Hotels"])


@router.get("")
async def all_hotels():
    return await HotelDAO.find_all()


@router.get("/{location}")
async def get_hotels_by_location(
    location: str,
    date_from: date = Query(
        ..., description=f"Например, {datetime.now().date()}"
    ),
    date_to: date = Query(
        ...,
        description=f"Например, {(datetime.now() + timedelta(days=14)).date()}"
    ),
) -> list[SHotelInfo]:
    return await HotelDAO.get_by_location(location, date_from, date_to)


@router.get("/id/{hotel_id}", include_in_schema=True)
async def get_hotel_by_id(
    hotel_id: int,
) -> SHotel | None:
    return await HotelDAO.find_one_or_none(id=hotel_id)
