from abc import ABC, abstractmethod

class IStrategy(ABC):
    """docstring for IStrategy."""

    @abstractmethod
    def __init__(self):
        super(IStrategy, self).__init__()

    @abstractmethod
    def calculate(self, product_list):
        pass

class StrategyRegularPrice(IStrategy):
    """docstring for StrategyRegulaPrice."""

    def __init__(self):
        super(StrategyRegularPrice, self).__init__()

    def calculate(self, product_list):
        total = 0
        for product in product_list:
            total += product.get_price()
        total = round(total, 2)
        return total

class StrategySmallPromotion(object):
    """docstring for StrategySmallPromotion."""

    def __init__(self):
        super(StrategySmallPromotion, self).__init__()

    def calculate(self, product_list):
        total = 0
        cheapest_price = product_list[0].get_price()
        for product in product_list:
            price = product.get_price()
            if price < cheapest_price:
                cheapest_price = product.get_price()
            total += price
        total = total - cheapest_price
        total = total * 0.9
        total = round(total, 2)
        return total


class StrategyBigPromotion(object):
    """docstring for StrategySmallPromotion."""

    def __init__(self):
        super(StrategyBigPromotion, self).__init__()

    def calculate(self, product_list):
        total = 0
        most_expensive_price = product_list[0].get_price()
        for product in product_list:
            price = product.get_price()
            if price > most_expensive_price:
                most_expensive_price = product.get_price()
            total += price
        total = total - most_expensive_price
        total = total * 0.85
        total = round(total, 2)
        return total
