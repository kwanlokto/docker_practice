class BaseException(Exception):
    def __init__(self, message, title=None, status_code=504):
        super().__init__(message)
        self.message = message
        self.title = title
        self.status_code = status_code
