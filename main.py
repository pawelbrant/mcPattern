import sys

# from PyQt5.QtWidgets import QApplication, QWidget

# from gui import ControlPanel
from Model import Product, OrderRegular, OrderTakeaway, OrderBuilderRegular, OrderBuilderTakeaway
from Command import CommandRevertOrder, CommandComposeOrder, Invoker
from Decorator import KetchupDecorator


if __name__ == '__main__':
    # app = QApplication(sys.argv)

    var1 = OrderBuilderRegular()
    print(var1)
    # var2 = OrderTakeaway([], 1)
    # print(var2)

    var1.add_product(Product('Mc Mini', 14.99))
    var1.add_product(Product('Mc Big', 20.99))
    p1 = Product('Fries', 5.15)
    var1.add_product(KetchupDecorator(p1)) #.get_decorated()) #dodaje kinda poprawnie cenę, ale jebie się przy nazwie
    #order = var1.build()

    invoker = Invoker()
    order = invoker.execute_command(CommandComposeOrder(var1))
    order2 = invoker.execute_command(CommandRevertOrder(var1))

    print(order)
    print(order2)

    #CommandRevertOrder.execute(order)
    #print(order)

    # sys.exit(app.exec_())
