from abc import ABC, abstractmethod
from Model import Product


class Decorator(object):

    def __init__(self, decorated: Product):
        self.__decorated = decorated

    #@abstractmethod
    def get_name(self):
        return self.__decorated.get_name()

    #@abstractmethod
    def get_price(self):
        return self.__decorated.get_price()

    # #@abstractmethod
    # def get_decorated(self):
    #     pass


class KetchupDecorator(Decorator):

    def __init__(self, product: Product):
        super(KetchupDecorator, self).__init__(product)
        #Decorator.__init__(self, product)
        self.__product = product
        # self.__product.__name = self.get_name()
        # print(self.__product.__name)
        # self.__product.__price = self.get_price()
        # print(self.__product.__price)
        # print(self.__product)
        self.__product = self.get_decorated()

    def get_name(self):
        print("name")
        #self.__name + "with ketchup"
        #return Decorator.get_name(self) + " with ketchup "
        #print(super(KetchupDecorator, self).get_name())
        return super(KetchupDecorator, self).get_name() + " with ketchup "

    def get_price(self):
        print("price")
        #return Decorator.get_price(self) + 2.00
        return super(KetchupDecorator, self).get_price() + 2.00

    def get_decorated(self):
        #print(self.__product.__name)
        self.__product.__name = self.get_name()
        print(self.__product.__name)
        self.__product.__price = self.get_price()
        #print(self.__product.__str__())
        print(self.__product.__price)
        return self.__product


class BoxDecorator(Decorator):

    def __init__(self, product: Product):
        Decorator.__init__(self, product)

    def get_name(self):
        return Decorator.get_name(self) + " with box "

    def get_price(self):
        return Decorator.get_price(self) + 0.50


class EnlargeDecorator(Decorator):

    def __init__(self, product: Product):
        Decorator.__init__(self, product)

    def get_name(self):
        return Decorator.get_name(self) + " enlarged "

    def get_price(self):
        return Decorator.get_price(self) + 3.00
