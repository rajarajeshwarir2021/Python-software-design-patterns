"""
PROTOTYPE
Need to copy an existing object, but we cannot just copy it like that as:
* We cannot access the Private/ not visible fields
* We might only have the Interfaces to the object and not a reference
* It requires Tight coupling, we need to know the structure of it
Advantages:
    Lets copy existing objects
    Without depending on their classes
    Only reliant on interface
    The copy object must provide the copy functionality
    Useful in testing and pre-production
"""

import copy
from abc import ABC, abstractmethod


class Shape(ABC):
    """Abstract Shapes class"""
    @abstractmethod
    def draw(self):
        """Abstract Draw method"""
        pass


class Square(Shape):
    """Square shape class"""
    def __init__(self, size):
        self.size = size

    def draw(self):
        """Draw a square method"""
        print(f"Drawing a square of size {self.size}")


class Circle(Shape):
    """Circle shape class"""
    def __init__(self, radius):
        self.radius = radius

    def draw(self):
        """Draw a circle method"""
        print(f"Drawing a circle of radius {self.radius}")


class AbstractArt:
    """AbstractArt class"""
    def __init__(self, bg_color, shapes):
        self.bg_color = bg_color
        self.shapes = shapes

    def draw(self):
        """Draw the given shapes on a canvas of given background color"""
        print(f"Background color is {self.bg_color}")
        [x.draw() for x in self.shapes]


if __name__ == '__main__':
    # Create an art and its copy
    shapes = [Square(2), Circle(3), Square(5)]
    art_1 = AbstractArt("red", shapes)
    art_2 = copy.copy(art_1)

    art_1.draw()
    art_2.draw()
