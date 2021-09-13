from abc import ABC, abstractmethod


class Product:
    def __init__(self, name_, price_):
        self.__name = name_
        self.__price = price_

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value_):
        self.__name = value_

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value_):
        self.__price = value_


class Discount(ABC):
    def __init__(self, product_):
        self.__product = product_

    @property
    def product(self):
        return self.__product

    @product.setter
    def product(self, value_):
        self.__product = value_

    @abstractmethod
    def discount_price(self):
        pass


class NoDiscount(Discount):
    def __init__(self, product_):
        super().__init__(product_)

    def discount_price(self):
        return self.product.price


class OneQuarterDiscount(Discount):
    def __init__(self, product_):
        super().__init__(product_)

    def discount_price(self):
        return self.product.price * 3/4


class HalfDiscount(Discount):
    def __init__(self, product_):
        super().__init__(product_)

    def discount_price(self):
        return self.product.price * 1/2


class ThreeQuarterDiscount(Discount):
    def __init__(self, product_):
        super().__init__(product_)

    def discount_price(self):
        return self.product.price * 1/4


if __name__ == "__main__":
    product = Product("tissue", 100)
    print(f"Price before discount: {product.price}")

    no_discount = NoDiscount(product)
    print(f"No discount: {no_discount.discount_price()}")

    one_quarter_discount = OneQuarterDiscount(product)
    print(f"One quarter discount: {one_quarter_discount.discount_price()}")

    half_discount = HalfDiscount(product)
    print(f"Half discount: {half_discount.discount_price()}")

    three_quarter_discount = ThreeQuarterDiscount(product)
    print(f"Three quarter discount: {three_quarter_discount.discount_price()}")
