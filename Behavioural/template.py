"""
TEMPLATE
Allows to standardize an algorithm to an abstract structure
* Break down a known problem into steps
* Standardizes steps for a multitude of cases
* Put steps in a single method
"""

from abc import ABC, abstractmethod


class DataStorage(ABC):
    @abstractmethod
    def setup(self):
        pass

    def check_data(self, data):
        print(f"DataStorage: checking data {data}")

    @abstractmethod
    def write_data(self, data):
        pass

    @abstractmethod
    def commit(self):
        pass

    @abstractmethod
    def log(self):
        pass

    def template(self, data):
        self.setup()
        self.check_data(data)
        self.write_data(data)
        self.commit()
        self.log()


class DatabaseDataStorage(DataStorage):
    def setup(self):
        print("Database connection established")

    def write_data(self, data):
        print(f"Database: writing data: {data}")

    def commit(self):
        print("Database: data committed successfully")

    def log(self):
        print("Database: writing completed")


class FileSystemDataStorage(DataStorage):
    def setup(self):
        print("File system ready")

    def write_data(self, data):
        print(f"FileSystem: writing data: {data}")

    def commit(self):
        print("FileSystem: data committed successfully")

    def log(self):
        print("FileSystem: writing completed")


if __name__ == '__main__':
    storage_1 = DatabaseDataStorage()
    storage_1.template("Hello World!")

    print()

    storage_2 = FileSystemDataStorage()
    storage_2.template("Hi World!")