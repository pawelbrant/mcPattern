from abc import ABC, abstractmethod

from Strategy import StrategyRegularPrice, StrategySmallPromotion, StrategyBigPromotion

class Product(object):
    """docstring for Product."""

    def __init__(self, name, price):
        super(Product, self).__init__()
        self.__name = name
        self.__price = price

    def get_name(self):
        return self.__name

    def get_price(self):
        return self.__price

    def __str__(self):
        return self.__name


class Order(ABC):
    """docstring for Order."""

    __number = 0

    @abstractmethod
    def __init__(self, product_list, strategy):
        super(Order, self).__init__()
        self._product_list = product_list
        self._id = Order._Order__number
        Order._Order__number = (Order._Order__number + 1) % 100
        self._price_total = 0
        # self._state = StatePending()
        self._strategy = strategy

    def __str__(self):
        string = 'Zamównienie nr {:>2}: '.format(self._id)
        for product in self._product_list:
            string += ' {}'.format(product)
        if self._price_total == 0:
            self._price_total = self._strategy.calculate(self._product_list)
        string += '; Cena wynosi: {}'.format(self._price_total)
        return string

    def get_product_list(self):
        return self._product_list

class OrderRegular(Order):
    """docstring for OrderRegular."""

    def __init__(self, product_list, strategy):
        super(OrderRegular, self).__init__(product_list, strategy)

class OrderTakeaway(Order):
    """docstring for OrderRegular."""

    def __init__(self, product_list, strategy):
        super(OrderTakeaway, self).__init__(product_list, strategy)


class OrderBuilder(ABC):
    """docstring for Builder."""

    @abstractmethod
    def __init__(self):
        super(OrderBuilder, self).__init__()
        self._product_list = []

    @abstractmethod
    def add_product(self, product):
        pass

    def build(self):
        print("hehe")
        return OrderRegular(self._product_list, self._get_strategy())

    def _get_strategy(self):
        if len(self._product_list) > 9:
            strategy = StrategyBigPromotion()
        elif len(self._product_list) > 5:
            strategy = StrategySmallPromotion()
        else:
            strategy = StrategyRegularPrice()
        return strategy

class OrderBuilderRegular(OrderBuilder):
    """docstring for OrderBuilderTakeaway."""

    def __init__(self):
        super(OrderBuilderRegular, self).__init__()

    def add_product(self, product):
        self._product_list.append(product)
        return self


class OrderBuilderTakeaway(OrderBuilder):
    """docstring for OrderBuilderTakeaway."""

    def __init__(self):
        super(OrderBuilderTakeaway, self).__init__()

    def add_product(self, product):
        self._product_list.append(product)
        return self
