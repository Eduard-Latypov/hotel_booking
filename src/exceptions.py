from fastapi import HTTPException, status


class BookingException(HTTPException):
    status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
    detail = ""

    def __init__(self):
        super().__init__(self.status_code, self.detail)
