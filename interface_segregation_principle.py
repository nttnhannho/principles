from abc import ABC, abstractmethod


class IDatabaseConnection(ABC):
    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def close(self):
        pass


class IDatabaseUpdate(ABC):
    @abstractmethod
    def add(self):
        pass

    @abstractmethod
    def delete(self):
        pass

    @abstractmethod
    def modify(self):
        pass


class IDatabaseDisplay(ABC):
    @abstractmethod
    def show_info(self):
        pass


class SQLDatabase(IDatabaseConnection, IDatabaseUpdate, IDatabaseDisplay):
    def connect(self):
        return "Connected by using SQL Database"

    def close(self):
        return "Closed by using SQL Database"

    def add(self):
        return "Added by using SQL Database"

    def delete(self):
        return "Deleted by using SQL Database"

    def modify(self):
        return "Modified by using SQL Database"

    def show_info(self):
        return "Showed info by using SQL Database"


class PostgreDatabase(IDatabaseConnection, IDatabaseUpdate):  # Assume that Postgre can not show database info
    def connect(self):
        return "Connected by using Postgre Database"

    def close(self):
        return "Closed by using Postgre Database"

    def add(self):
        return "Added by using Postgre Database"

    def delete(self):
        return "Deleted by using Postgre Database"

    def modify(self):
        return "Modified by using Postgre Database"


class DatabaseCreator:
    def __init__(self, db):
        self.db = db

    @property
    def database(self):
        return self.db

    @database.setter
    def database(self, db):
        self.db = db

    def connect(self):
        try:
            return self.db.connect()
        except AttributeError:
            raise Exception("Unable to connect")

    def close(self):
        try:
            return self.db.close()
        except AttributeError:
            raise Exception("Unable to disconnect")

    def add(self):
        try:
            return self.db.add()
        except AttributeError:
            raise Exception("Unable to add")

    def modify(self):
        try:
            return self.db.modify()
        except AttributeError:
            raise Exception("Unable to modify")

    def delete(self):
        try:
            return self.db.delete()
        except AttributeError:
            raise Exception("Unable to delete")

    def show_info(self):
        try:
            return self.db.show_info()
        except AttributeError:
            raise Exception("Unable to show info")


if __name__ == "__main__":
    sqlserver = SQLDatabase()
    postgresql = PostgreDatabase()

    db = DatabaseCreator(sqlserver)
    print(db.connect())
    print(db.add())
    print(db.modify())
    print(db.delete())
    print(db.close())
    print(db.show_info())

    print("*" * 20)
    
    db.database = postgresql
    print(db.connect())
    print(db.add())
    print(db.modify())
    print(db.delete())
    print(db.close())
    print(db.show_info())
