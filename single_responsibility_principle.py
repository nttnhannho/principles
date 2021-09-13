class Account:
    def __init__(self, id_, name_):
        self.__id = id_
        self.__name = name_

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, value_):
        self.__id = value_

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value_):
        self.__name = value_


class AccountDB:
    def __init__(self, account_):
        self.__account = account_

    @property
    def account(self):
        return self.__account

    @account.setter
    def account(self, value_):
        self.__account = value_

    def save(self):
        return f"{self.__account.id} is saving to database"


if __name__ == "__main__":
    account = Account("ac001", "Tom")
    account_db = AccountDB(account)
    print(account_db.save())
