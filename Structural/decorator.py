"""
DECORATOR
To modify the behaviour of a third party object
* Attach new behaviour to an object
* Without altering existing code
* Overriding behaviour
"""

from abc import ABC, abstractmethod


# Third party library
class CoffeeMachine(ABC):
    """Abstract Coffee Machine class"""
    @abstractmethod
    def make_small_coffee(self):
        """Abstract make small coffee method"""
        pass

    @abstractmethod
    def make_large_coffee(self):
        """Abstract make large coffee method"""
        pass


class BasicCoffeeMachine(CoffeeMachine):
    """Basic Coffee Machine class"""

    def make_small_coffee(self):
        """Make a small coffee"""
        print("Basic Coffee Machine: Making small coffee")

    def make_large_coffee(self):
        """Make a large coffee"""
        print("Basic Coffee Machine: Making large coffee")


# Our modification
class EnhancedCoffeeMachine(CoffeeMachine):
    """Enhanced Coffee Machine class"""
    def __init__(self, basic_machine: BasicCoffeeMachine):
        self.basic_machine = basic_machine

    def make_small_coffee(self):
        """Make a small coffee method"""
        self.basic_machine.make_small_coffee()

    def make_large_coffee(self):
        """Make a large coffee method"""
        print("Enhanced Coffee Machine: Making large coffee")

    def make_milk_coffee(self):
        """Make a milk coffee method"""
        print("Enhanced Coffee Machine: Making milk coffee")
        self.basic_machine.make_small_coffee()
        print("Enhanced Coffee Machine: adding milk")


if __name__ == '__main__':
    # Create Coffees
    basic_machine = BasicCoffeeMachine()
    enhanced_machine = EnhancedCoffeeMachine(basic_machine)

    enhanced_machine.make_small_coffee()
    print()
    enhanced_machine.make_large_coffee()
    print()
    enhanced_machine.make_milk_coffee()

