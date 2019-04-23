from enum import Enum


class HttpMethod(Enum):
    LIST = "GET"
    ADD = "POST"
    EDIT = "PUT"
    DELETE = "DELETE"
