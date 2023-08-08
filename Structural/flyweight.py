"""
FLYWEIGHT
Reduce the load or requirements on a system
Use:
    Lots of similar objects
    Share functionality
* Reduce memory and processing footprint
* Improves efficiency
"""

import random
from abc import ABC,abstractmethod


class GameSprite(ABC):
    """Abstract Game Sprite class"""
    @abstractmethod
    def draw(self):
        """Abstract draw method"""
        pass

    @abstractmethod
    def move(self, x: int, y: int):
        """Abstract move method"""
        pass


class FighterRank:
    """Fighter Rank class"""
    pawn = 0
    sergeant = 1
    major = 2


class Fighter(GameSprite):
    """Fighter class"""
    def __init__(self, rank: FighterRank):
        self.rank = rank

    def draw(self):
        """Draw fighter method"""
        print(f"Drawing fighter {self}")

    def move(self, x: int, y: int):
        """Move fighter method"""
        print(f"Moving fighter {self} to position {x}, {y}")


class FighterFactory:
    """Fighter factory class"""
    def __init__(self):
        self.fighters = []

    def get_fighter(self, rank: FighterRank):
        """Get fighter method"""
        f = self.fighters[rank]
        if not f:
            f = Fighter(rank)
            self.fighters[rank] = f
        return f


class Army:
    """Army class"""
    army = []

    def spawn_fighter(self, rank: FighterRank):
        """Spawn a fighter method"""
        self.army.append(Fighter(rank))

    def draw_army(self):
        """Draw the army method"""
        for fighter in self.army:
            if fighter.rank == FighterRank.major:
                print("M ", end="")
            elif fighter.rank == FighterRank.sergeant:
                print("S ", end="")
            else:
                print("P ", end="")


if __name__ == '__main__':
    # Create an Army
    army_size = 500
    army = Army()

    for i in range(army_size):
        r = random.randrange(3)
        army.spawn_fighter(r)

    army.draw_army()
