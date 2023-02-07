class BaseApiException(Exception):
    def __init__(self, error, status_code):
        self.error = error
        self.status_code = status_code

    def __repr__(self):
        return f'<Error> {self.error}'


class EndpointNotFoundException(BaseApiException):
    ...