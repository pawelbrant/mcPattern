#GUI imports
from PyQt5.QtWidgets import QWidget, QListWidget, QFormLayout, QHBoxLayout, \
QLabel, QSpinBox, QDoubleSpinBox, QLineEdit, QTextEdit, QPushButton, \
QVBoxLayout, QListWidgetItem
from PyQt5.QtGui import QDoubleValidator

from sip import wrappertype as M_A
from abc import ABCMeta as M_B

from Model import *


class ControlPanel(QWidget):
    """docstring for ControlPanel."""

    def __init__(self, parent=None):
        super(ControlPanel, self).__init__(parent)
        # self.facade = facade

        self.__add_order = QPushButton()
        self.__change_order_state = QPushButton()
        self.__cancel_order = QPushButton()
        self.__add_product = QPushButton()
        self.__remove_product = QPushButton()
        self.__child = None

        self.start()

    def start(self):
        self.setWindowTitle('Mac Pattern')
        self.__add_order.clicked.connect(self.add_order)
        self.__change_order_state.clicked.connect(self.change_order_state)
        self.__cancel_order.clicked.connect(self.cancel_order)
        self.__add_product.clicked.connect(self.add_product)
        self.__remove_product.clicked.connect(self.remove_product)

        form = QFormLayout()
        form.addRow('Compose an order:', self.__add_order)
        form.addRow("Change order's state:", self.__change_order_state)
        form.addRow('Cancel an order:', self.__cancel_order)
        form.addRow('Add new product to menu:', self.__add_product)
        form.addRow('Remove product from menu:', self.__remove_product)

        self.setLayout(form)

    def delete(self):
        s = Storage()
        s.cancel_order(s.get_orders()[0])

    def add_order(self):
        self.__child = ComposeOrder()
        self.__child.execute()

    def change_order_state(self):
        self.__child = ComposeOrder()
        self.__child.execute()

    def cancel_order(self):
        self.__child = ComposeOrder()
        self.__child.execute()

    def add_product(self):
        self.__child = AddToMenu()
        self.__child.execute()

    def remove_product(self):
        self.__child = ComposeOrder()
        self.__child.execute()
        

class M_GUI_Observer(M_A, M_B):
    pass


class StaffMonitor(QWidget, Observer, metaclass=M_GUI_Observer):

    def __init__(self, parent=None):
        super(StaffMonitor, self).__init__(parent)    
        self.__orders = QListWidget()
        self.__details = QListWidget()

        self.start()
        self.reload()
        
    def start(self):
        self.setWindowTitle('Staff Observer')

        self.__orders.itemSelectionChanged.connect(self.details)

        left_column = QVBoxLayout()
        left_column.addWidget(QLabel('Orders:'))
        left_column.addWidget(self.__orders)

        right_column = QVBoxLayout()
        right_column.addWidget(QLabel('Order contents:'))
        right_column.addWidget(self.__details)

        layout = QHBoxLayout()
        layout.addItem(left_column)
        layout.addSpacing(30)
        layout.addItem(right_column)

        self.setLayout(layout)

    def reload(self):
        self.__orders.clear()
        for item in self._order_list:
            row = QListWidgetItem()
            row.setText('#{:0>2}'.format(item.get_number()))
            self.__orders.addItem(row)

    def details(self):
        self.__details.clear()
        id = self.__orders.currentRow()
        order = self._order_list[id]
        for item in order.get_product_list():
            self.__details.addItem(str(item))

    def invalidate(self):
        super(StaffMonitor, self).invalidate()
        self.reload()


class RegisterMonitor(QWidget, Observer, metaclass=M_GUI_Observer):

    def __init__(self, parent=None):
        super(RegisterMonitor, self).__init__(parent)
        self.__orders = QListWidget()

        self.start()
        self.reload()

    def start(self):
        self.setWindowTitle('Register Observer')
        layout = QHBoxLayout()
        self.__orders.setMaximumHeight(150)
        layout.addWidget(self.__orders)

        self.setLayout(layout)

    def reload(self):
        self.__orders.clear()
        for item in self._order_list:
            row = QListWidgetItem()
            row.setText('#{:0>2}'.format(item.get_number()))
            self.__orders.addItem(row)

    def invalidate(self):
        super(RegisterMonitor, self).invalidate()
        self.reload()

class ComposeOrder(QWidget):

    def __init__(self, parent=None):
        super(ComposeOrder, self).__init__(parent)

        self.start()

    def start(self):
        self.setWindowTitle('Compose Order')
        self.setLayout(QFormLayout())

    def execute(self):
        self.show()


class AddToMenu(QWidget):

    def __init__(self, parent=None):
        super(AddToMenu, self).__init__(parent)

        self.__name = QLineEdit()
        self.__price = QLineEdit()
        self.__add_button = QPushButton()
        self.__exit_button = QPushButton()
        self.__list_widget = QListWidget()

        self.start()
        # self.load()

    def start(self):
        self.setWindowTitle('Add New Product')

        left_column = QFormLayout()
        left_column.addRow('Nazwa:', self.__name)
        left_column.addRow('Cena:', self.__price)

        layout = QHBoxLayout()
        layout.addItem(left_column)
        layout.addSpacing(30)
        layout.addWidget(self.__list_widget)

        self.setLayout(layout)

    def execute(self):
        self.move(600, 430)
        self.show()