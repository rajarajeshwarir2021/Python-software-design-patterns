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
    database = 1
    network = 2
    fileStorage = 3


class DataSource(ABC):
    @abstractmethod
    def make_connection(self):
        pass


class Database(DataSource):
    def make_connection(self):
        print("Connecting Database...")


class Network(DataSource):
    def make_connection(self):
        print("Connecting Network...")


class FileStorage(DataSource):
    def make_connection(self):
        print("Connecting File Storage...")


class DataSourceFactory:
    @staticmethod
    def connection_types(d_type: DataSourceType):
        if d_type == DataSourceType.database:
            return Database()
        elif d_type == DataSourceType.network:
            return Network()
        else:
            return FileStorage()


def connect_to(connection: Database):
    print("We are connecting to: ")
    connection.make_connection()


if __name__ == '__main__':
    conn_1 = DataSourceFactory.connection_types(DataSourceType.network)
    conn_2 = DataSourceFactory.connection_types(DataSourceType.fileStorage)

    connect_to(conn_1)
    connect_to(conn_2)




