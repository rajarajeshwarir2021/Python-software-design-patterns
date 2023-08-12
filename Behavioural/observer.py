"""
OBSERVER
The most useful and common
* Define a subscription mechanism - where users get notified to their subscribed event
* Notify multiple objects simultaneously
* One to many relationship
"""

from abc import ABC, abstractmethod


class EventListener(ABC):
    """Abstract Event Listener class"""
    @abstractmethod
    def update(self, event_type: str, file):
        """Abstract update method"""
        pass


class EventManager:
    """Event Manager class"""
    def __init__(self, operations):
        self.operations = operations
        self.listeners = {}
        for op in operations:
            self.listeners[op] = []

    def subscribe(self, event_type: str, listener:EventListener):
        """Subscribe method"""
        users = self.listeners[event_type]
        users.append(listener)

    def unsubscribe(self, event_type: str, listener:EventListener):
        """Unsubscribe method"""
        users = self.listeners[event_type]
        users.remove(listener)

    def notify(self, event_type, file):
        """Notify method"""
        users = self.listeners[event_type]
        [u.update(event_type, file) for u in users]


class Editor:
    """Editor class"""
    events = EventManager(["open", "save"])
    file = None

    def open_file(self, file):
        """Open file method"""
        self.file = file
        print(f"Editor: opening file {file}")
        self.events.notify("open", file)

    def save_file(self):
        """Save file method"""
        print(f"Editor: saving file {self.file}")
        self.events.notify("save", self.file)


class EmailNotificationListener(EventListener):
    """Email Notification Listener class"""
    def __init__(self, email):
        self.email = email

    def update(self, event_type: str, file):
        """Update method"""
        print(f"Email to {self.email}: Someone has performed {event_type} operation on the file {file}")


class LogOpenListener(EventListener):
    """Log Open Listener class"""
    def __init__(self, log_file):
        self.log_file = log_file

    def update(self, event_type: str, file):
        """Update method"""
        print(f"Save to log {self.log_file}: Someone has performed {event_type} operation on the file {file}")


if __name__ == '__main__':
    # Observer
    editor = Editor()

    email_listener = EmailNotificationListener("test@gmail.com")
    log_listener = LogOpenListener("path/to/log/file.txt")

    editor.events.subscribe("open", log_listener)
    editor.events.subscribe("save", log_listener)
    editor.events.subscribe("save", log_listener)

    editor.open_file("test.txt")
    editor.save_file()
