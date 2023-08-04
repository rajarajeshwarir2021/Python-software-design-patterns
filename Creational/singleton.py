"""
SINGLETON
The most well-known design pattern with its own positives and negatives.
Put a central resource in a single instance of a component
* Only one instance
* Single point of access for a resource
Use:
    Network Manager
    Database access
    Logging
    Utility classes
Disadvantage:
    Breaks Single Responsibility Principle
    Testability issues - cannot mock it easily
    State for life
"""

import time
from threading import Thread, Lock


class NaiveSingleton(type):
    """Naive Singleton implementation which does not work in multi-thread environment"""
    _instance = {}

    def __call__(self, *args, **kwargs):
        """Override __call__ method to create an instance if it does not exist"""
        if self not in self._instance:
            instance = super().__call__(*args, **kwargs)
            time.sleep(1)
            self._instance[self] = instance
        return self._instance[self]


class NaiveNetworkDriver(metaclass=NaiveSingleton):
    """Naive Network Driver"""
    def log(self):
        """Print the instance"""
        print(f"{self}\n")


def create_naive_singleton():
    """Create a naive singleton and return the instance"""
    n_singleton = NaiveNetworkDriver()
    n_singleton.log()
    return n_singleton


class ThreadSafeSingleton(type):
    """Thread safe Singleton implementation which works even in multi-thread environment"""
    _instance = {}
    _lock = Lock()

    def __call__(self, *args, **kwargs):
        """Override __call__ method to create an instance if not locked and it does not exist"""
        with self._lock:
            if self not in self._instance:
                instance = super().__call__(*args, **kwargs)
                time.sleep(1)
                self._instance[self] = instance
        return self._instance[self]


class ThreadSafeNetworkDriver(metaclass=ThreadSafeSingleton):
    """Thread safe Network Driver"""
    def log(self):
        """Print the instance"""
        print(f"{self}\n")


def create_thread_safe_singleton():
    """Create a thread safe Singleton and return the instance"""
    n_singleton = ThreadSafeNetworkDriver()
    n_singleton.log()
    return n_singleton


if __name__ == '__main__':
    # Single Thread
    #s1 = create_naive_singleton()
    #s2 = create_naive_singleton()

    # Multi Thread PROBLEM!!! Two different objects created
    p1 = Thread(target=create_naive_singleton)
    p2 = Thread(target=create_naive_singleton)
    p1.start()
    p2.start()

    # Multi Thread safe
    p3 = Thread(target=create_thread_safe_singleton)
    p4 = Thread(target=create_thread_safe_singleton)
    p3.start()
    p4.start()
