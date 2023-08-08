"""
FACADE
Provide a simple interface to a complex functionality
* Removes the need for complex object/memory management
* Simplifies client implementation
* Separation of concerns
"""
from dataclasses import dataclass


# Complex Data Store
class ComplexDataStorage:
    """Complex Data Storage class"""
    def __init__(self, filepath: str):
        self.filepath = filepath
        self.cache = {}
        print(f"Reading data from file: {filepath}")

    def store(self, key: str, value: str):
        """Store the key value pair method"""
        self.cache[key] = value

    def read(self, key: str):
        """Read the key value method"""
        return self.cache[key]

    def commit(self):
        """Commit the data method"""
        print(f"Storing cached data to file {self.filepath}")


@dataclass
class User:
    """User dataclass"""
    login: str


# Facade
class UserRepository:
    """User Repository class"""
    def __init__(self):
        self.system_preferences = ComplexDataStorage("data/default.prefs")

    def save(self, user: User):
        """Save User data"""
        self.system_preferences.store("USER_KEY", user.login)
        self.system_preferences.commit()

    def find_first(self):
        """Retrieve User data"""
        return User(self.system_preferences.read("USER_KEY"))


if __name__ == '__main__':
    # Use only Facade to perform the complex operation in the backend
    user_repo = UserRepository()
    user = User("Bob")

    user_repo.save(user)
    ret_user = user_repo.find_first()
    print(ret_user.login)
