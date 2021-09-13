class Animal:
    def __init__(self, name_):
        self.__name = name_

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value_):
        self.__name = value_


class WalkableAnimal(Animal):
    def __init__(self, name_):
        super().__init__(name_)

    def walk(self):
        return f"{self.name} is walking"


class FlyableAnimal(Animal):
    def __init__(self, name_):
        super().__init__(name_)

    def fly(self):
        return f"{self.name} is flying"


class Dog(WalkableAnimal):
    def __init__(self, name_):
        super().__init__(name_)

    def bark(self):
        return f"{self.name} is barking"


class Bird(FlyableAnimal):
    def __init__(self, name_):
        super().__init__(name_)

    def migrate(self):
        return f"{self.name} is migrating to Southern"


if __name__ == "__main__":
    dog = Dog("Spike")
    print(dog.bark())
    print(dog.walk())

    bird = Bird("Elise")
    print(bird.fly())
    print(bird.migrate())
