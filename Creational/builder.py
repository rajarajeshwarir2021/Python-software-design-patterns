"""
BUILDER
Useful in many situations, when we have multiple parameters to initialize
* For many parameters, it's impractical to build all the constructors as
    5 parameter combinations -> 120 constructors
* Can have some default and some optional parameters
* Should be easy to read
"""


class ClassicDatabaseService:
    """A Classic Database Service class"""
    def __init__(self):
        self.components = {}

    def add(self, key: str, value: str):
        """Add a key value pair component to the instance variable"""
        self.components[key] = value

    def show(self):
        """Display the instance variable components"""
        print(self.components)


class ClassicDatabaseServiceBuilder:
    """A Classic Database Service Builder class"""
    def __init__(self):
        self._service = ClassicDatabaseService()

    def add_target_database(self, target: str):
        """Add a target database"""
        self._service.add("TARGET", target)

    def add_auth(self, auth: str):
        """Add an authorization"""
        self._service.add("Authorization", auth)

    def build(self) -> ClassicDatabaseService:
        """Build the Classic Database Service"""
        service = self._service
        self._service = ClassicDatabaseService()
        return service


class DatabaseService:
    """A Database Service class"""
    def __init__(self, target: str = "", auth: str = ""):
        self.components = {}
        if target:
            self.components["TARGET"] = target
        if auth:
            self.components["Authorization"] = auth

    def show(self):
        """Display the instance variable components"""
        print(self.components)


if __name__ == '__main__':
    # Build a Classic Database
    builder = ClassicDatabaseServiceBuilder()
    builder.add_target_database("PostgreSQL")
    builder.add_auth("123456")

    db_service_1 = builder.build()
    db_service_1.show()

    # Build a Database using mint parameters of Python
    db_service_2 = DatabaseService(target="MySQL", auth="78910")
    db_service_2.show()

