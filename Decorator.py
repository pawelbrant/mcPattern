from abc import ABC, abstractmethod
from Model import Product

class Decorator(Product):

    #def __init__(self, decorated: Product):
        #self.__decorated = decorated

    @abstractmethod
    def getName(self):
        pass

    @abstractmethod
    def getPrice(self):
        pass

    @abstractmethod
    def getDecorated(self):
        pass

class KetchupDecorator(Decorator):

    def __init__(self, product: Product):
        super(KetchupDecorator, self).__init__()
        self.__product = product

    def getName(self):
        #self.__name + "with ketchup"
        return self.__product.__name + "with ketchup"

    def getPrice(self):
        return self.__product.__price + 2.00

class BoxDecorator(Decorator):

    def __init__(self, product: Product):
        super(BoxDecorator, self).__init__()
        self.__product = product

    def getName(self):
        return self.__product.__name + "with box"

    def getPrice(self):
        return self.__product.__price + 0.50

class EnlargeDecorator(Decorator):

    def __init__(self, product: Product):
        super(EnlargeDecorator, self).__init__()
        self.__product = product

    def getName(self):
        return self.__product.__name + "enlarged"

    def getPrice(self):
        return self.__product.__price + 3.00
