
class StorageConfig:
    def __init__(self, connection_string=None, file_path=None):
        self.connection_string = connection_string
        self.file_path = file_path


# Base class for all storage types
class Storage:
    def __init__(self, config: StorageConfig):
        self.config = config

    def connect(self):
        raise NotImplementedError("Subclasses should implement this method.")

    def read(self, key):
        raise NotImplementedError("Subclasses should implement this method.")

    def write(self, key, value):
        raise NotImplementedError("Subclasses should implement this method.")

class SQLStorage(Storage):
    def connect(self):
        print(f"Connecting to SQL Database with config: {self.config.connection_string}")

    def read(self, key):
        print(f"Reading '{key}' from SQL Database...")
        return f"SQL Value for {key}"

    def write(self, key, value):
        print(f"Writing '{value}' to SQL Database under key '{key}'")

class NoSQLStorage(Storage):
    def connect(self):
        print(f"Connecting to NoSQL Database with config: {self.config.connection_string}")

    def read(self, key):
        print(f"Reading '{key}' from NoSQL Database...")
        return f"NoSQL Value for {key}"

    def write(self, key, value):
        print(f"Writing '{value}' to NoSQL Database under key '{key}'")

class FileStorage(Storage):
    def connect(self):
        print(f"Connecting to File Storage System at path: {self.config.file_path}")

    def read(self, key):
        print(f"Reading '{key}' from File Storage System...")
        return f"File Value for {key}"

    def write(self, key, value):
        print(f"Writing '{value}' to File Storage System under key '{key}'")


class DependencyInjector:
    def __init__(self):
        self.configurations = {}

    def register_config(self, storage_type, config):
        self.configurations[storage_type] = config

    def get_config(self, storage_type):
        config = self.configurations.get(storage_type)
        if not config:
            raise ValueError(f"No configuration registered for storage type: {storage_type}")
        return config



class StorageFactory:
    def __init__(self, injector: DependencyInjector):
        self.injector = injector

    def create_storage(self, storage_type):
        config = self.injector.get_config(storage_type)
        if storage_type == "sql":
            return SQLStorage(config)
        elif storage_type == "nosql":
            return NoSQLStorage(config)
        elif storage_type == "file":
            return FileStorage(config)
        else:
            raise ValueError(f"Unknown storage type: {storage_type}")



def main():
    # Set up Dependency Injector with configurations
    injector = DependencyInjector()
    injector.register_config("sql", StorageConfig(connection_string="SQLServer://localhost;Database=myDB"))
    injector.register_config("nosql", StorageConfig(connection_string="NoSQLServer://localhost;Collection=myCollection"))
    injector.register_config("file", StorageConfig(file_path="/data/storage/files"))

    # Create the StorageFactory with Dependency Injection
    factory = StorageFactory(injector)

    # Create SQL storage and use it
    sql_storage = factory.create_storage("sql")
    sql_storage.connect()
    sql_storage.write("user123", "John Doe")
    print(sql_storage.read("user123"))

    print()

    # Create NoSQL storage and use it
    nosql_storage = factory.create_storage("nosql")
    nosql_storage.connect()
    nosql_storage.write("user456", "Jane Doe")
    print(nosql_storage.read("user456"))

    print()

    # Create File storage and use it
    file_storage = factory.create_storage("file")
    file_storage.connect()
    file_storage.write("file789", "Sample File Content")
    print(file_storage.read("file789"))

if __name__ == "__main__":
    main()

