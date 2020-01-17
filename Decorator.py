from abc import ABC, abstractmethod
from Model import IProduct


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
        return super(EnlargeDecorator, self).__str__() + " enlarged"
