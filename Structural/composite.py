"""
COMPOSITE
Composes of other components
* Compose objects into tree structures
* Works when the core functionality can be represented as a tree
* Manipulate many objects as a single one
"""


class Device:
    """Device class"""
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price


class CompositeDevice:
    """Composite Device class"""
    def __init__(self, name: str):
        self.name = name
        self.items = []

    def add(self, device: Device):
        """Add a device to the composite"""
        self.items.append(device)
        return self

    @property
    def price(self):
        """Calculate the total price of the composite"""
        return sum(x.price for x in self.items)

    @price.setter
    def price(self, value):
        """Set the price of the composite"""
        self.price = value


if __name__ == '__main__':
    # Compose a Laptop
    computer = CompositeDevice("Laptop")
    processor = Device("Processor", 1205.05)
    hard_drive = Device("Hard Drive", 1009.96)
    memory = CompositeDevice("Memory")
    rom = Device("ROM", 496.8)
    ram = Device("RAM", 524.38)
    io = Device("Input/Output", 736.87)

    memory.add(rom)
    memory.add(ram)

    computer.add(processor)
    computer.add(hard_drive)
    computer.add(memory)
    computer.add(io)

    total_price = computer.price
    print(f"Total Device Cost: ${total_price}")

