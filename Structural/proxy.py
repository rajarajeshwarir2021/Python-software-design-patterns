"""
PROXY
Manage the lifecycle and access to the underlying object
* Provide functionality before and/or after calling an object
* Same Interface as the object
* Similar to Facade pattern, except it has the same interface
* Similar to Decorator pattern, except it manages the lifecycle of its object
"""

from abc import ABC, abstractmethod


class DataStore(ABC):
    """Abstract DataStore class"""
    @abstractmethod
    def display(self):
        """Abstract store method"""
        pass


class HardDisk(DataStore):
    """Hard Disk class"""
    def __init__(self, filename: str):
        self.filename = filename
        print(f"Real data: loading {filename}")

    def display(self):
        """Display data method"""
        print(f"Real data: displaying {self.filename}", end="\n\n")


class ProxyDataStore(DataStore):
    """Proxy DataStore class"""
    def __init__(self, filename: str):
        self.filename = filename
        self.real_data = None

    def display(self):
        """Display data method"""
        print(f"Proxy data: displaying {self.filename}", end="\n")
        if not self.real_data:
            print("From disk")
            self.real_data = HardDisk(self.filename)
        else:
            print("From cache")
        self.real_data.display()


if __name__ == '__main__':
    # Display from Proxy
    data = ProxyDataStore("test_file.txt")
    # Load data from disk
    data.display()
    # Load data from cache
    data.display()






