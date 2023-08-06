"""
FACTORY METHOD
Requirements generally change in a project therefore we need to modify or refactor the code to adapt
It creates a separation between the creator and user of the object
* Can change code more easily with less impact
* Dynamic switching
* Separation of concerns
* Design logic is hidden from the client
* Many subclass types, only one instance required
* Creation is removed from client
* Useful for frequent code changes
Components required:
    Interface or abstract class that defines the common functionality
    Implementation of the interfaces
    Factory class that instantiates the right implementation
Use:
    Access different Databases
    Access different Network
    Access different User Input
    Access different File Storage
"""

from abc import ABC, abstractmethod


class SoftwareFactory(ABC):
    """Software Factory abstract class"""
    @abstractmethod
    def software_factory(self, software) -> str:
        """software factory abstract method"""
        pass


class TextSoftwareFactory(SoftwareFactory):
    """Text Software Factory implements text software"""
    def software_factory(self, software) -> str:
        """Return the relevant text software"""
        if software is Microsoft:
            return "Word"
        elif software is Apple:
            return "Pages"
        else:
            return "Writer"


class PresentationSoftwareFactory(SoftwareFactory):
    """Presentation Software Factory implements presentation software"""
    def software_factory(self, software) -> str:
        """Return the relevant presentation software"""
        if software is Microsoft:
            return "Powerpoint"
        elif software is Apple:
            return "Keynote"
        else:
            return "Impress"


class Software:
    """Software class"""
    pass


class Microsoft(Software):
    """Microsoft software class"""
    pass


class Apple(Software):
    """Apple software class"""
    pass


class Libre(Software):
    """Libre software class"""
    pass


if __name__ == '__main__':
    # Create text and presentation software factory
    d1 = TextSoftwareFactory()
    d2 = PresentationSoftwareFactory()

    # Print the relevant software
    print(d1.software_factory(Microsoft))
    print(d1.software_factory(Apple))
    print(d1.software_factory(Libre))

    print(d2.software_factory(Microsoft))
    print(d2.software_factory(Apple))
    print(d2.software_factory(Libre))