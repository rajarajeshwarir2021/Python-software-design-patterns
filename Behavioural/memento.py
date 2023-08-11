"""
MEMENTO
State monitoring and tracing system that enables going back and forth
* Save and restore previous state without revealing implementation details
* Three components
    - Memento: stores the state
    - Originator: creates the state
    - Caretaker: decides to save or restore the state
"""

from dataclasses import dataclass


@dataclass
class Memento:
    """Memento dataclass"""
    state: str


class Originator:
    """Originator class"""
    def __init__(self, state):
        self.state = state

    def create_memento(self):
        """Create memento method"""
        return Memento(self.state)

    def restore_memento(self, memento: Memento):
        """Restore memento method"""
        self.state = memento.state


class Caretaker:
    """Caretaker class"""
    memento_list = []

    def save_state(self, state: Memento):
        """Save state method"""
        self.memento_list.append(state)

    def restore(self, index: int):
        """Restore method"""
        return self.memento_list[index]


if __name__ == '__main__':
    # Memento
    originator = Originator("Initial state")
    care_taker = Caretaker()

    care_taker.save_state(originator.create_memento())
    print(f"Current state is {originator.state}")

    originator.state = "state_1"
    care_taker.save_state(originator.create_memento())
    print(f"Current state is {originator.state}")

    originator.state = "state_2"
    care_taker.save_state(originator.create_memento())
    print(f"Current state is {originator.state}")

    originator.restore_memento(care_taker.restore(1))
    print(f"Current state is {originator.state}")

    originator.restore_memento(care_taker.restore(0))
    print(f"Current state is {originator.state}")

    originator.restore_memento(care_taker.restore(2))
    print(f"Current state is {originator.state}")