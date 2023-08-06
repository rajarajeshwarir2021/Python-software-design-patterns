"""
BRIDGE
Addresses Multiple inheritance problem
Having classes with multiple orthogonal traits exponentially increases the size of the inheritance tree
* Convert from inheritance to composition
* Split into multiple interfaces/classes
* Associate them using a "bridge" reference
"""

from abc import ABC, abstractmethod


class Device(ABC):
    """Abstract Device class"""
    volume = 0

    @abstractmethod
    def get_name(self) -> str:
        """Abstract get device name method"""
        pass


class TV(Device):
    """TV class"""
    def get_name(self) -> str:
        """Get the TV name method"""
        return f"TV {self}"


class BluetoothSpeaker(Device):
    """Bluetooth speaker class"""
    def get_name(self) -> str:
        """Get the Bluetooth Speaker name method"""
        return f"Bluetooth Speaker {self}"


class Remote(ABC):
    """Abstract Remote class"""
    @abstractmethod
    def volume_up(self):
        """Abstract volume up method"""
        pass

    @abstractmethod
    def volume_down(self):
        """Abstract volume down method"""
        pass


class BasicRemote(Remote):
    """Basic Remote class"""
    def __init__(self, device: Device):
        self.device = device

    def volume_up(self):
        """Volume up method"""
        self.device.volume += 1
        print(f"{self.device.get_name()} volume up: {self.device.volume}")

    def volume_down(self):
        """Volume down method"""
        self.device.volume -= 1
        print(f"{self.device.get_name()} volume down: {self.device.volume}")


if __name__ == '__main__':
    # Adjust Device volume
    tv = TV()
    bspeaker = BluetoothSpeaker()

    tv_remote = BasicRemote(tv)
    bspeaker_remote = BasicRemote(bspeaker)

    tv_remote.volume_up()
    tv_remote.volume_up()
    tv_remote.volume_down()

    bspeaker_remote.volume_up()
    bspeaker_remote.volume_down()
