from fastapi import FastAPI
import uvicorn
from app.bookings.router import router as bookings_router
from app.users.router import router as users_router


app = FastAPI()
app.include_router(users_router)
app.include_router(bookings_router)

if __name__ == "__main__":
    uvicorn.run('main:app', reload=True)
