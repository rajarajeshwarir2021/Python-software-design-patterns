"""
MEDIATOR
Aids communication between different components
* Provides a central object used for communicating between objects
* Object don't talk to each other
* Reduce dependencies between objects
"""


from __future__ import annotations


class ChatUser:
    """Chat User class"""
    mediator = None

    def __init__(self, name):
        self.name = name

    def set_mediator(self, med: Mediator):
        """Set mediator method"""
        self.mediator = med

    def send(self, msg: str):
        """Send message method"""
        print(f"{self.name}: Sending message {msg}")
        self.mediator.send_message(msg, self)

    def receive(self, msg: str):
        """Receive message method"""
        print(f"{self.name}: Receiving message {msg}")


class Mediator:
    """Mediator class"""
    users = []

    def add_user(self, user: ChatUser):
        """Add user class"""
        self.users.append(user)
        user.set_mediator(self)

    def send_message(self, msg: str, user: ChatUser):
        """Send message method"""
        for u in self.users:
            if u != user:
                u.receive(msg)


if __name__ == '__main__':
    # Mediator
    mediator = Mediator()
    alice = ChatUser("Alice")
    bob = ChatUser("Bob")
    carol = ChatUser("Carol")

    mediator.add_user(alice)
    mediator.add_user(bob)
    mediator.add_user(carol)

    # Send a message from a user
    carol.send("Hi everyone!")