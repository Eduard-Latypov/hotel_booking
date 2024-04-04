import uvicorn
from fastapi import Depends, FastAPI, Query

from src.users.router import router as router_register
from src.hotels.rooms.router import router as hotel_room_router
from src.bookings.router import router as router_booking

app = FastAPI()

app.include_router(router_register)
app.include_router(hotel_room_router)
app.include_router(router_booking)


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True, host="127.0.0.1", port=8000)
