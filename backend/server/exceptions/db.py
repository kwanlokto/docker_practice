from server.exceptions.base import BaseException

class DBException(BaseException):
    def __init__(self, message, title=None, status_code=510):
        super().__init__(message)
        self.message = message
        self.title = title
        self.status_code = status_code
