from email.message import EmailMessage
from smtplib import SMTP_SSL
from email import message_from_string
from pathlib import Path
from typing import Any, Mapping

import asyncio
from pydantic import EmailStr

from src.bookings.dao import BookingsDAO

from src.config import settings
from .celery_app import celery_app


@celery_app.task()
def send_booking_confirmation_email(booking: Mapping[str, Any]):
    email_text = create_booking_confirmation_text(booking)
    with SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(settings.EMAIL_USER, settings.EMAIL_PASS)
        server.send_message(email_text)


def create_booking_confirmation_text(booking: Mapping[str, Any]) -> EmailMessage:
    email_text = EmailMessage()

    email_text["Subject"] = "Подтверждение бронирования"
    email_text["From"] = settings.EMAIL_USER
    email_text["To"] = settings.EMAIL_USER

    email_text.set_content(
        f"""
                <h1>Подтвердите бронирование</h1>
                Вы забронировали отель с {booking['date_from']} по {booking["date_to"]} число
            """,
        subtype="html",
    )
    return email_text
