from fastapi import FastAPI
import uvicorn
from app.bookings.router import router as booking_router


app = FastAPI()
app.include_router(booking_router)

if __name__ == "__main__":
    uvicorn.run('main:app', reload=True)
