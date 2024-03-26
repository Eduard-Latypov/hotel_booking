import datetime
from typing import Annotated

import uvicorn
from fastapi import Depends, FastAPI
from fastapi.responses import FileResponse

from src.models import HotelData, SBooking

app = FastAPI()


@app.get("/")
async def home():
    return {"message": "Крутецкий Сайтец"}


@app.get("/hotels")
async def get_hotels(query_args: HotelData = Depends()):
    return query_args


@app.post("/bookings", response_model=SBooking)
def add_booking(data: SBooking):
    return data


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True, host="127.0.0.1", port=8000)
