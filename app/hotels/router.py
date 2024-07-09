from datetime import date
from fastapi import APIRouter

from app.hotels.dao import HotelDAO

router = APIRouter(prefix="/hotels", tags=["Hotels"])


@router.get("")
async def all_hotels():
    return await HotelDAO.find_all()


@router.get("/{location}")
async def get_hotel(
    location: str,
    date_from: date,
    date_to: date,
):
    return await HotelDAO.get_by_location(location, date_from, date_to)
