"""
ADAPTER
Converts the interface of a class into another interface the client expects
Like convert data from one format to another
Separation of concerns
"""

from dataclasses import dataclass


# 3rd party functionality
@dataclass
class ThirdPartyDataType:
    """Third party DataType class"""
    x: str
    y: str


class ThirdPartyDisplayData:
    """Third party display data"""
    def __init__(self, display_data: ThirdPartyDataType):
        self.display_data = display_data

    def show_data(self):
        print(f"3rd party functionality: {self.display_data.x} - {self.display_data.y}")


# Our code functionality
@dataclass
class DatabaseDataType:
    """Client Database DataType class"""
    latitude: float
    longitude: float


class StoreDatabaseData:
    """Client Store Database Data class"""
    def __init__(self, database_data: DatabaseDataType):
        self.database_data = database_data

    def store_data(self, data):
        """Store the data in the database method"""
        print(f"Database data stored: {self.database_data.latitude} - {self.database_data.longitude}")


# Adapter class implementation to connect the Client Database to the Third party library
class DisplayDataAdapter(StoreDatabaseData, ThirdPartyDisplayData):
    def __init__(self, data):
        self.data = data

    def store_data(self):
        print(f"Call out code but use 3rd party code")
        for item in self.data:
            ddt = ThirdPartyDataType(str(item.latitude), str(item.longitude))
            self.display_data = ddt
            self.show_data()


def generate_data():
    """Generate dummy client data for testing"""
    data = list()
    data.append(DatabaseDataType(33.3, -46.0))
    data.append(DatabaseDataType(36.5, 48.7))
    data.append(DatabaseDataType(50.8, 63.5))
    return data


if __name__ == '__main__':
    # Adapter class
    adapter = DisplayDataAdapter(generate_data())
    adapter.store_data()



