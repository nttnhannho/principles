from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self, name_):
        self.__name = name_

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value_):
        self.__name = value_

    def eat(self):
        return f"{self.__name} is eating"

    @abstractmethod
    def talk(self):
        pass


class Dog(Animal):
    def __init__(self, name_):
        super().__init__(name_)

    def talk(self):
        return f"{self.name} is barking"

    def guard(self):
        return f"{self.name} is guarding"


class Cat(Animal):
    def __init__(self, name_):
        super().__init__(name_)

    def talk(self):
        return f"{self.name} is meow-ing"

    def catch_mouse(self):
        return f"{self.name} is catching mouse"


class Robot(ABC):
    def __init__(self, name_):
        self.__name = name_

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value_):
        self.__name = value_

    def charge(self):
        return f"{self.__name} is charging"


class CleanerRobot(Robot):
    def __init__(self, name_):
        super().__init__(name_)

    def clean(self):
        return f"{self.name} is cleaning"


class KillerRobot(Robot):
    def __init__(self, name_):
        super().__init__(name_)

    def kill_insect(self):
        return f"{self.name} is killing insect"


class UltraSuperAnimalRobot:
    def __init__(self, name_):
        self.__name = name_
        self.__dog = Dog(name_)
        self.__cat = Cat(name_)
        self.__cleaner_robot = CleanerRobot(name_)
        self.__killer_robot = KillerRobot(name_)

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value_):
        self.__name = value_

    def talk(self):
        return self.__cat.talk()

    def guard(self):
        return self.__dog.guard()

    def charge(self):
        return self.__cleaner_robot.charge()

    def clean(self):
        return self.__cleaner_robot.clean()

    def kill(self):
        return self.__killer_robot.kill_insect()


if __name__ == "__main__":
    super_robot = UltraSuperAnimalRobot("Tom")
    print(super_robot.talk())
    print(super_robot.guard())
    print(super_robot.charge())
    print(super_robot.clean())
    print(super_robot.kill())
