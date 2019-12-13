import sys

# from PyQt5.QtWidgets import QApplication, QWidget

# from gui import ControlPanel
from Model import Product, OrderRegular, OrderTakeaway, OrderBuilderRegular, \
OrderBuilderTakeaway



if __name__ == '__main__':
    # app = QApplication(sys.argv)

    var1 = OrderBuilderRegular()
    print(var1)
    # var2 = OrderTakeaway([], 1)
    # print(var2)

    var1.add_product(Product('Mc Mini', 14.99))
    var1.add_product(Product('Mc Big', 20.99))
    order = var1.build()
    print(order)

    # sys.exit(app.exec_())
