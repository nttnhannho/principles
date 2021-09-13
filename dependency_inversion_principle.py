from abc import ABC, abstractmethod


class IFood(ABC):
    @abstractmethod
    def bake(self):
        pass

    @abstractmethod
    def eat(self):
        pass


class Pizza(IFood):
    def __init__(self, name_):
        self.__name = name_

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value_):
        self.__name = value_

    def bake(self):
        return f"Pizza is being baked"

    def eat(self):
        return f"Pizza is being eaten"


class Bread(IFood):
    def __init__(self, name_):
        self.__name = name_

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value_):
        self.__name = value_

    def bake(self):
        return f"Bread is being baked"

    def eat(self):
        return f"Bread is being eaten"


class Production:
    def __init__(self, food_):
        self.__food = food_

    @property
    def food(self):
        return self.__food

    @food.setter
    def food(self, value_):
        self.__food = value_

    def produce(self):
        return self.__food.bake()

    def consume(self):
        return self.__food.eat()


if __name__ == "__main__":
    pizza = Pizza("p1")
    p = Production(pizza)
    print(p.produce())
    print(p.consume())

    bread = Bread("b1")
    b = Production(bread)
    print(b.produce())
    print(b.consume())
