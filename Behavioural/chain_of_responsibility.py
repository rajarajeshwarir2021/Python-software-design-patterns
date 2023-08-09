"""
CHAIN OF RESPONSIBILITY
* Define a chain of handlers to process a request
* Each handler contains a reference to the next handler
* Each handler decides to process/consume the request and/or pass it on
* Requests can be of different types
"""

from __future__ import annotations
from abc import ABC, abstractmethod


class HandlerChain(ABC):
    """Abstract Handler chain class"""
    def __init__(self, input_header: HandlerChain):
        self.next_header = input_header

    @abstractmethod
    def add_header(self, input_header: str):
        """Abstract add header method"""
        pass

    def do_next(self, input_header: str):
        """Abstract consume  or pass on method"""
        if self.next_header:
            return self.next_header.add_header(input_header)
        return input_header


class AuthenticationHeader(HandlerChain):
    """Authentication Handler class"""
    def __init__(self, token: str, next_header: HandlerChain = None):
        super().__init__(next_header)
        self.token = token

    def add_header(self, input_header: str):
        """Add header method"""
        h = f"{input_header}\nAuthorization: {self.token}"
        return self.do_next(h)


class ContentTypeHeader(HandlerChain):
    """Content Type Handler class"""
    def __init__(self, content_type: str, next_header: HandlerChain = None):
        super().__init__(next_header)
        self.content_type = content_type

    def add_header(self, input_header: str):
        """Add content method"""
        h = f"{input_header}\nContentType: {self.content_type}"
        return self.do_next(h)


class PayloadHeader(HandlerChain):
    """Payload Handler class"""
    def __init__(self, body: str, next_header: HandlerChain = None):
        super().__init__(next_header)
        self.body = body

    def add_header(self, input_header: str):
        """Add payload method"""
        h = f"{input_header}\n{self.body}"
        return self.do_next(h)


if __name__ == '__main__':
    # Chain of handlers
    auth_header = AuthenticationHeader("12345")
    content_type_header = ContentTypeHeader("json")
    payload_header = PayloadHeader("Body:{\"username\" = \"bob\"}")

    auth_header.next_header = content_type_header
    content_type_header.next_header = payload_header

    # Request goes through entire chain
    msg_with_auth = auth_header.add_header("Header with authentication")
    # Request goes from middle of the chain
    msg_without_auth = content_type_header.add_header("Header without authentication")

    print(msg_with_auth)
    print()
    print(msg_without_auth)