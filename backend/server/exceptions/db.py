from server.exceptions.base import InternalException


class DBException(InternalException):
    def __init__(self, message, title=None, status_code=510):
        super().__init__(message)
        self.message = message
        self.title = title
        self.status_code = status_code
