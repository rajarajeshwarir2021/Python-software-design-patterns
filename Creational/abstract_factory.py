"""
ABSTRACT FACTORY
One level of abstraction above the factory method design pattern
* A factory that creates factories
* Provides a way to access functionality without caring about implementation
* Separation of concerns
* Allows for testability
"""

from abc import ABC, abstractmethod


class DataSourceType:
    """DataSource types class"""
    database = 1
    network = 2
    fileStorage = 3


class DataSource(ABC):
    """Abstract DataSource class"""
    @abstractmethod
    def make_connection(self):
        """Abstract make connection method"""
        pass


class Database(DataSource):
    """Database class"""
    def make_connection(self):
        """Make connection to database method"""
        print("Connecting Database...")


class Network(DataSource):
    """Network class"""
    def make_connection(self):
        """Make connection to network method"""
        print("Connecting Network...")


class FileStorage(DataSource):
    """FileStorage class"""
    def make_connection(self):
        """Make connection to file storage method"""
        print("Connecting File Storage...")


class DataSourceFactory:
    """DataSource Factory class"""
    @staticmethod
    def connection_types(d_type: DataSourceType):
        """Connection types method"""
        if d_type == DataSourceType.database:
            return Database()
        elif d_type == DataSourceType.network:
            return Network()
        else:
            return FileStorage()


def connect_to(connection: DataSource):
    """Connect to a DataSource"""
    print("We are connecting to: ")
    connection.make_connection()


if __name__ == '__main__':
    conn_1 = DataSourceFactory.connection_types(DataSourceType.network)
    conn_2 = DataSourceFactory.connection_types(DataSourceType.fileStorage)

    connect_to(conn_1)
    connect_to(conn_2)




