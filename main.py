import sys

from PyQt5.QtWidgets import QApplication, QWidget

from gui import ControlPanel, StaffMonitor
from Model import Product, OrderRegular, OrderTakeaway, OrderBuilderRegular, OrderBuilderTakeaway, Storage, Observer
from Command import CommandRevertOrder, CommandComposeOrder, Invoker
from Decorator import KetchupDecorator, EnlargeDecorator


if __name__ == '__main__':
    app = QApplication(sys.argv)

    # var1 = OrderBuilderRegular()
    # print(var1)
    # var2 = OrderTakeaway([], 1)
    # print(var2)

    # var1.add_product(Product('Mc Mini', 14.99))
    # var1.add_product(Product('Mc Big', 20.99))
    # p1 = Product('Fries', 5.15)
    # var1.add_product(EnlargeDecorator(KetchupDecorator(p1)))
    #order = var1.build()
    #print(var1._product_list.__getitem__(1))
    #print(var1._product_list.__getitem__(2))
    # invoker = Invoker()
    # order = invoker.execute_command(CommandComposeOrder(var1))
    # order2 = invoker.execute_command(CommandRevertOrder(var1))

    # print(order)
    # storage = Storage()
    # storage.add_order(order)
    # storage2 = Storage()
    # print(storage2.get_orders()[0])
    # print(order2)

    #CommandRevertOrder.execute(order)
    #print(order)

    for var in Storage().get_orders():
        print(var)

    window = ControlPanel()
    window.move(600, 300)
    window.show()

    monitor1 = StaffMonitor()
    monitor1.move(0, 300)
    monitor1.show()

    sys.exit(app.exec_())
