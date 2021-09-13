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


if __name__ == "__main__":
    sql_server = SQLDatabase()
    print(sql_server.connect())
    print(sql_server.add())
    print(sql_server.modify())
    print(sql_server.delete())
    print(sql_server.close())
    print(sql_server.show_info())
    print("*" * 20)
    postgre = PostgreDatabase()
    print(postgre.connect())
    print(postgre.add())
    print(postgre.modify())
    print(postgre.delete())
    print(postgre.close())
