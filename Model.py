import jsonpickle
from abc import ABC, abstractmethod

from Strategy import StrategyRegularPrice, StrategySmallPromotion, StrategyBigPromotion


class IProduct(ABC):
    """docstring for IProduct."""

    @abstractmethod
    def __init__(self):
        super(IProduct, self).__init__()

    @abstractmethod
    def get_price(self):
        pass

    @abstractmethod
    def __str__(self):
        pass


class Product(IProduct):
    """docstring for Product."""

    def __init__(self, name, price):
        super(Product, self).__init__()
        self.__name = name
        self.__price = price

    def get_price(self):
        return self.__price

    def __str__(self):
        return self.__name


class Decorator(IProduct):

    @abstractmethod
    def __init__(self, decorated: IProduct):
        super(Decorator, self).__init__()
        self._decorated = decorated

    @abstractmethod
    def get_price(self):
        return self._decorated.get_price()

    def get_decorated(self):
        return self._decorated

    @abstractmethod
    def __str__(self):
        return str(self._decorated)


class KetchupDecorator(Decorator):

    def __init__(self, product: IProduct):
        super(KetchupDecorator, self).__init__(product)

    def get_price(self):
        return super(KetchupDecorator, self).get_price() + 2.00

    def __str__(self):
        return super(KetchupDecorator, self).__str__() + " with ketchup"


class BoxDecorator(Decorator):

    def __init__(self, product: IProduct):
        super(BoxDecorator, self).__init__(product)

    def get_price(self):
        return super(BoxDecorator, self).get_price() + 0.50

    def __str__(self):
        return super(BoxDecorator, self).__str__() + " in a box"


class EnlargeDecorator(Decorator):

    def __init__(self, product: IProduct):
        super(EnlargeDecorator, self).__init__(product)

    def get_price(self):
        return super(EnlargeDecorator, self).get_price() + 3.00

    def __str__(self):
        return "Enlarged " + super(EnlargeDecorator, self).__str__()


class Order(ABC):
    """docstring for Order."""

    @abstractmethod
    def __init__(self, product_list, strategy):
        super(Order, self).__init__()
        self._product_list = product_list
        self._id = Storage().get_number()
        self._price_total = 0
        # self._state = StatePending()
        self._strategy = strategy

    def __str__(self):
        string = 'Order #{:0>2}: '.format(self._id)
        for product in self._product_list:
            string += ' {}'.format(product)
        if self._price_total == 0:
            self._price_total = self._strategy.calculate(self._product_list)
        string += '; Total price: {}'.format(self._price_total)
        return string

    def get_number(self):
        return self._id

    def get_product_list(self):
        return self._product_list

    def get_total(self):
        return self._price_total


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

    def add_product(self, product):
        self._product_list.append(product)
        return self

    def get_products(self):
        return self._product_list

    def remove_product(self, product):
        if product in self._product_list:
            self._product_list.remove(product)

    @abstractmethod
    def build(self):
        pass

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
        super(OrderBuilderRegular, self).add_product(product)
        return self

    def build(self):
        return OrderRegular(self._product_list, self._get_strategy())


class OrderBuilderTakeaway(OrderBuilder):
    """docstring for OrderBuilderTakeaway."""

    def __init__(self):
        super(OrderBuilderTakeaway, self).__init__()

    def add_product(self, product):
        super(OrderBuilderTakeaway, self).add_product(BoxDecorator(product))
        return self

    def build(self):
        return OrderTakeaway(self._product_list, self._get_strategy())


class Observer(ABC):

    @abstractmethod
    def __init__(self):
        super(Observer, self).__init__()
        self._storage = Storage()
        self._storage.add_observer(self)
        self._order_list = self._storage.get_orders()
    
    def invalidate(self):
        self._order_list = self._storage.get_orders()


class Observable(ABC):

    @abstractmethod
    def __init__(self):
        super(Observable, self).__init__()
        self._observer_list = []

    def add_observer(self, observer: Observer):
        if observer in self._observer_list:
            return
        self._observer_list.append(observer)

    def remove_observer(self, observer: Observer):
        if observer in self._observer_list:
            self._observer_list.remove(observer)

    def notify(self, observer: Observer):
        if observer in self._observer_list:
            observer.invalidate()
    
    def notify_all(self):
        [x.invalidate() for x in self._observer_list]


class Storage(object):
    
    class __Storage(Observable):

        def __init__(self):
            super(Storage.__Storage, self).__init__()
            try:
                with open('backup.json', 'r') as f:
                    data = jsonpickle.decode(f.read())
                (self.__current_number, self.__menu, self.__order_list) = data
            except:
                print('Could not load data')
                self.__current_number = 1
                self.__menu = []
                self.__order_list = []

        def get_number(self):
            return self.__current_number

        def add_to_menu(self, product: Product):
            if product in self.__menu:
                return
            self.__menu.append(product)
            # self.notify_all()
            self.serialize()

        def remove_from_menu(self, product: Product):
            if product in self.__menu:
                self.__menu.remove(product)
                # self.notify_all()
                self.serialize()

        def add_order(self, order: Order):
            self.__order_list.append(order)
            self.__current_number = (order.get_number() % 10) + 1
            self.notify_all()
            self.serialize()

        def order_received(self, order: Order):
            self.notify_all()

        def cancel_order(self, order: Order):
            if order in self.__order_list:
                self.__order_list.remove(order)
                self.notify_all()
                self.serialize()

        def get_menu(self):
            return self.__menu

        def get_orders(self):
            return self.__order_list

        def serialize(self):
            data = (self.__current_number, self.__menu, self.__order_list)
            try:
                with open('backup.json', 'w') as f:
                    f.write(jsonpickle.encode(data))
            except:
                print('Could not backup data')

    __instance = None

    def __init__(self):
        if not Storage.__instance:
            Storage.__instance = Storage.__Storage()

    def __getattribute__(self, attr):
        return getattr(Storage.__instance, attr)

class Command(ABC):

    @abstractmethod
    def __init__(self):
        super(Command, self).__init__()
        self._storage = Storage()

    @abstractmethod
    def execute(self):
        pass