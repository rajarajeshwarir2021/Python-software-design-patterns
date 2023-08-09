"""
COMMAND
A request is wrapped in an object that contains all request info
* The command object is passed to the correct handler
* Can have more than one command object communicating to the components
* Provides decoupling
* Efficiency, ordering, priority, etc.
"""

from abc import ABC, abstractmethod


class Command(ABC):
    """Abstract command class"""
    def __init__(self, command_id: int):
        self.command_id = command_id

    @abstractmethod
    def execute(self):
        """Abstract execute method"""
        pass


class OrderAddCommand(Command):
    """Add Order class"""
    def execute(self):
        """Execute add order method"""
        print(f"Adding order with id {self.command_id}")


class OrderPayCommand(Command):
    """Pay Order class"""
    def execute(self):
        """Execute pay order method"""
        print(f"Paying for the order with id {self.command_id}")


class CommandProcessor:
    """Command Processor class"""
    queue = []

    def add_to_queue(self, command: Command):
        """Add command to queue method"""
        self.queue.append(command)

    def process_commands(self):
        """Process command from queue method"""
        [item.execute() for item in self.queue]
        self.queue = []


if __name__ == '__main__':
    # Create commands
    processor = CommandProcessor()
    processor.add_to_queue(OrderAddCommand(1))
    processor.add_to_queue(OrderAddCommand(2))
    processor.add_to_queue(OrderPayCommand(1))
    processor.add_to_queue(OrderPayCommand(2))

    # Process commands
    processor.process_commands()