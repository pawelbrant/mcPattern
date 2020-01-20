#GUI imports
from PyQt5.QtWidgets import QWidget, QListWidget, QFormLayout, QHBoxLayout, \
QLabel, QSpinBox, QDoubleSpinBox, QLineEdit, QTextEdit, QPushButton, \
QVBoxLayout, QListWidgetItem, QSpacerItem, QCheckBox, QStackedLayout, QGridLayout
from PyQt5.QtGui import QDoubleValidator
from PyQt5.QtCore import Qt

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

        self.__add_order.setText('Compose an order')
        self.__change_order_state.setText("Change order's state")
        self.__cancel_order.setText('Cancel an order')
        self.__add_product.setText('Add new product to menu')
        self.__remove_product.setText('Remove product from menu')

        form = QVBoxLayout()
        form.addWidget(self.__add_order)
        form.addWidget(self.__change_order_state)
        form.addWidget(self.__cancel_order)
        form.addWidget(self.__add_product)
        form.addWidget(self.__remove_product)

        self.setLayout(form)

    def add_order(self):
        self.__child = ComposeOrder()
        self.__child.execute()

    def change_order_state(self):
        self.__child = ChangeOrderState()
        self.__child.execute()

    def cancel_order(self):
        self.__child = CancelOrder()
        self.__child.execute()

    def add_product(self):
        self.__child = AddToMenu()
        self.__child.execute()

    def remove_product(self):
        self.__child = RemoveFromMenu()
        self.__child.execute()
        

class M_GUI_Model(M_A, M_B):
    pass


class StaffMonitor(QWidget, Observer, metaclass=M_GUI_Model):

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
        left_column.addItem(QSpacerItem(0, 5))
        left_column.addWidget(self.__orders)

        right_column = QVBoxLayout()
        right_column.addWidget(QLabel('Order contents:'))
        right_column.addItem(QSpacerItem(0, 5))
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
            row.setText('#{0:0>2}{1:35}{2}'.format(item.get_number(), '', str(item.get_state())))
            self.__orders.addItem(row)

    def details(self):
        self.__details.clear()
        number = self.__orders.currentRow()
        order = self._order_list[number]
        for item in order.get_product_list():
            row = QListWidgetItem()
            row.setText(str(item))
            row.setFlags(row.flags() & ~Qt.ItemIsSelectable)
            self.__details.addItem(row)

    def invalidate(self):
        super(StaffMonitor, self).invalidate()
        self.reload()


class RegisterMonitor(QWidget, Observer, metaclass=M_GUI_Model):

    def __init__(self, parent=None):
        super(RegisterMonitor, self).__init__(parent)
        self.__orders = QListWidget()

        self.start()
        self.reload()

    def start(self):
        self.setWindowTitle('Register Observer')
        self.__orders.setMaximumHeight(130)
        layout = QVBoxLayout()
        layout.addWidget(QLabel('Orders:'))
        # layout.addItem(QSpacerItem(0, 5))
        layout.addWidget(self.__orders)

        self.setLayout(layout)

    def reload(self):
        self.__orders.clear()
        for item in self._order_list:
            row = QListWidgetItem()
            row.setText('#{0:0>2}{1:35}{2}'.format(item.get_number(), '', str(item.get_state())))
            row.setFlags(row.flags() & ~Qt.ItemIsSelectable)
            self.__orders.addItem(row)

    def invalidate(self):
        super(RegisterMonitor, self).invalidate()
        self.reload()


class ComposeOrder(QWidget, Command, metaclass=M_GUI_Model):

    def __init__(self, parent=None):
        super(ComposeOrder, self).__init__(parent)
        self.__builder = None

        self.__ketchup = QCheckBox()
        self.__enlarged = QCheckBox()
        self.__add_button = QPushButton()
        self.__remove_button = QPushButton()
        self.__save_button = QPushButton()
        self.__exit_button = QPushButton()
        self.__menu_widget = QListWidget()
        self.__products_widget = QListWidget()
        self.__label_1 = QLabel('Order contents:')
        self.__label_2 = QLabel('Current menu:')

        self.__main = QWidget()
        self.__helper = QWidget()

        self.__takeaway_button = QPushButton()
        self.__regular_button = QPushButton()

        self.start()

    def regular(self):
        self.setWindowTitle('Compose an order')
        self.__builder = OrderBuilderRegular()
        self.__main.show()
        self.__helper.hide()
        self.reload()

    def takeaway(self):
        self.setWindowTitle('Compose an order')
        self.__builder = OrderBuilderTakeaway()
        self.__main.show()
        self.__helper.hide()
        self.reload()

    def build_first(self):
        self.__regular_button.setText('Regular')
        self.__regular_button.clicked.connect(self.regular)
        self.__regular_button.setMinimumHeight(180)
        self.__takeaway_button.setText('Takeaway')
        self.__takeaway_button.clicked.connect(self.takeaway)
        self.__takeaway_button.setMinimumHeight(180)

        self.__helper.setFixedWidth(727)
        self.__helper.setFixedHeight(237)

        layout = QHBoxLayout()
        layout.addWidget(self.__regular_button)
        layout.addWidget(self.__takeaway_button)

        self.__helper.setLayout(layout)

    def build_second(self):
        self.__ketchup.setText('Ketchup')
        self.__enlarged.setText('Enlarged')
        self.__add_button.setText('Add')
        self.__add_button.clicked.connect(self.add)
        self.__add_button.setMinimumWidth(100)
        self.__remove_button.setText('Remove')
        self.__remove_button.clicked.connect(self.remove)
        self.__remove_button.setMinimumWidth(100)
        self.__save_button.setText('Save')
        self.__save_button.clicked.connect(self.save)
        self.__save_button.setMinimumWidth(100)
        self.__exit_button.setText('Close')
        self.__exit_button.clicked.connect(self.close)
        self.__exit_button.setMinimumWidth(100)

        self.__main.setFixedWidth(727)
        self.__main.setFixedHeight(237)

        buttons = QVBoxLayout()
        buttons.addItem(QSpacerItem(0, 20))
        buttons.addWidget(self.__ketchup)
        buttons.addItem(QSpacerItem(0, 10))
        buttons.addWidget(self.__enlarged)
        buttons.addItem(QSpacerItem(0, 10))
        buttons.addWidget(self.__add_button)
        buttons.addItem(QSpacerItem(0, 10))
        buttons.addWidget(self.__remove_button)
        buttons.addItem(QSpacerItem(0, 10))
        buttons.addWidget(self.__save_button)
        buttons.addItem(QSpacerItem(0, 20))
        buttons.addWidget(self.__exit_button)

        left_column = QVBoxLayout()
        left_column.addWidget(self.__label_1)
        left_column.addItem(QSpacerItem(0, 5))
        left_column.addWidget(self.__products_widget)

        middle_column = QVBoxLayout()
        middle_column.addItem(buttons)

        right_column = QVBoxLayout()
        right_column.addWidget(self.__label_2)
        right_column.addItem(QSpacerItem(0, 5))
        right_column.addWidget(self.__menu_widget)

        layout = QHBoxLayout()
        layout.addItem(left_column)
        layout.addSpacing(30)
        layout.addItem(middle_column)
        layout.addSpacing(30)
        layout.addItem(right_column)

        self.__main.setLayout(layout)


    def start(self):
        self.setWindowTitle('Regular or Takeaway')

        self.build_first()
        self.build_second()

        layout = QStackedLayout()
        layout.addWidget(self.__helper)
        layout.addWidget(self.__main)

        self.setLayout(layout)

    def reload(self):
        self.__products_widget.clear()
        self.__menu_widget.clear()
        for item in self.__builder.get_products():
            row = QListWidgetItem()
            row.setText('{0:20}{1:5}'.format(str(item), item.get_price()))
            self.__products_widget.addItem(row)
        for item in self._storage.get_menu():
            row = QListWidgetItem()
            row.setText('{0:20}{1:5}'.format(str(item), item.get_price()))
            self.__menu_widget.addItem(row)

    def add(self):
        number = self.__menu_widget.currentRow()
        if number == -1:
            return
        product = self._storage.get_menu()[number]
        if self.__ketchup.isChecked():
            product = KetchupDecorator(product)
            self.__ketchup.setChecked(False)
        if self.__enlarged.isChecked():
            product = EnlargeDecorator(product)
            self.__enlarged.setChecked(False)
        self.__builder.add_product(product)
        self.reload()

    def remove(self):
        number = self.__products_widget.currentRow()
        if number == -1:
            return
        self.__builder.remove_product(self.__builder.get_products()[number])
        self.reload()

    def save(self):
        if not self.__builder.get_products():
            return
        self._storage.add_order(self.__builder.build())
        self.close()

    def execute(self):
        self.move(600, 430)
        self.show()


class ChangeOrderState(QWidget, Command, metaclass=M_GUI_Model):

    def __init__(self, parent=None):
        super(ChangeOrderState, self).__init__(parent)

        self.__next_state_button = QPushButton()
        self.__previous_state_button = QPushButton()
        self.__exit_button = QPushButton()
        self.__list_widget = QListWidget()

        self.start()
        self.reload()

    def start(self):
        self.setWindowTitle("Change order's state")

        self.__next_state_button.setText('Next state')
        self.__next_state_button.clicked.connect(self.next)
        self.__next_state_button.setMinimumWidth(100)
        self.__previous_state_button.setText('Previous state')
        self.__previous_state_button.clicked.connect(self.previous)
        self.__previous_state_button.setMinimumWidth(100)
        self.__exit_button.setText('Close')
        self.__exit_button.clicked.connect(self.close)
        self.__exit_button.setMinimumWidth(100)

        buttons = QGridLayout()
        buttons.setSpacing(5)
        buttons.addWidget(self.__previous_state_button, 0, 0)
        buttons.addWidget(self.__next_state_button, 0, 1)
        buttons.addWidget(self.__exit_button, 1, 0, 1, 2)

        layout = QVBoxLayout()
        layout.addWidget(QLabel('Orders:'))
        layout.addWidget(self.__list_widget)
        layout.addItem(buttons)

        self.setLayout(layout)

    def reload(self):
        self.__list_widget.clear()
        for item in self._storage.get_orders():
            row = QListWidgetItem()
            row.setText('#{0:0>2}{1:35}{2}'.format(item.get_number(), '', str(item.get_state())))
            self.__list_widget.addItem(row)

    def next(self):
        number = self.__list_widget.currentRow()
        if number == -1:
            return
        self._storage.next_state(self._storage.get_orders()[number])
        self.reload()

    def previous(self):
        number = self.__list_widget.currentRow()
        if number == -1:
            return
        self._storage.previous_state(self._storage.get_orders()[number])
        self.reload()

    def execute(self):
        self.move(600, 430)
        self.show()


class CancelOrder(QWidget, Command, metaclass=M_GUI_Model):

    def __init__(self, parent=None):
        super(CancelOrder, self).__init__(parent)

        self.__canel_button = QPushButton()
        self.__exit_button = QPushButton()
        self.__list_widget = QListWidget()

        self.start()
        self.reload()

    def start(self):
        self.setWindowTitle('Cancel an order')

        self.__canel_button.setText('Cancel')
        self.__canel_button.clicked.connect(self.cancel)
        self.__canel_button.setMinimumWidth(100)
        self.__exit_button.setText('Close')
        self.__exit_button.clicked.connect(self.close)
        self.__exit_button.setMinimumWidth(100)

        buttons = QVBoxLayout()
        buttons.setSpacing(5)
        buttons.addWidget(self.__canel_button)
        buttons.addWidget(self.__exit_button)

        layout = QVBoxLayout()
        layout.addWidget(QLabel('Orders:'))
        layout.addWidget(self.__list_widget)
        layout.addItem(buttons)

        self.setLayout(layout)

    def reload(self):
        self.__list_widget.clear()
        for item in self._storage.get_orders():
            row = QListWidgetItem()
            row.setText('#{0:0>2}{1:35}{2}'.format(item.get_number(), '', str(item.get_state())))
            self.__list_widget.addItem(row)

    def cancel(self):
        number = self.__list_widget.currentRow()
        if number == -1:
            return
        self._storage.cancel_order(self._storage.get_orders()[number])
        self.reload()

    def execute(self):
        self.move(600, 430)
        self.show()

        
class AddToMenu(QWidget, Command, metaclass=M_GUI_Model):

    def __init__(self, parent=None):
        super(AddToMenu, self).__init__(parent)

        self.__name = QLineEdit()
        self.__price = QLineEdit()
        self.__add_button = QPushButton()
        self.__exit_button = QPushButton()
        self.__list_widget = QListWidget()

        self.start()
        self.reload()

    def start(self):
        self.setWindowTitle('Add new product to menu')

        self.__add_button.setText('Add')
        self.__add_button.clicked.connect(self.add)
        self.__add_button.setMinimumWidth(100)
        self.__exit_button.setText('Close')
        self.__exit_button.clicked.connect(self.close)
        self.__exit_button.setMinimumWidth(100)

        buttons = QHBoxLayout()
        buttons.addWidget(self.__add_button)
        buttons.addItem(QSpacerItem(10, 0))
        buttons.addWidget(self.__exit_button)

        text_fields = QFormLayout()
        text_fields.addItem(QSpacerItem(0, 30))
        text_fields.addRow('Name: ', self.__name)
        text_fields.addItem(QSpacerItem(0, 30))
        text_fields.addRow('Price: ', self.__price)

        left_column = QVBoxLayout()
        left_column.addItem(text_fields)
        left_column.addItem(buttons)

        right_column = QVBoxLayout()
        right_column.addWidget(QLabel('Current menu:'))
        right_column.addItem(QSpacerItem(0, 5))
        right_column.addWidget(self.__list_widget)

        layout = QHBoxLayout()
        layout.addItem(left_column)
        layout.addSpacing(30)
        layout.addItem(right_column)

        self.setLayout(layout)

    def reload(self):
        self.__list_widget.clear()
        for item in self._storage.get_menu():
            row = QListWidgetItem()
            row.setText('{0:20}{1:5}'.format(str(item), item.get_price()))
            row.setFlags(row.flags() & ~Qt.ItemIsSelectable)
            self.__list_widget.addItem(row)

    def add(self):
        name = self.__name.text()
        price = self.__price.text()
        price = price.replace(',','.')
        price = float(price)
        # validation
        self.__name.setText('')
        self.__price.setText('')
        self._storage.add_to_menu(Product(name, price))
        self.reload()

    def execute(self):
        self.move(600, 430)
        self.show()


class RemoveFromMenu(QWidget, Command, metaclass=M_GUI_Model):

    def __init__(self, parent=None):
        super(RemoveFromMenu, self).__init__(parent)

        self.__remove_button = QPushButton()
        self.__exit_button = QPushButton()
        self.__list_widget = QListWidget()

        self.start()
        self.reload()

    def start(self):
        self.setWindowTitle('Remove product from menu')

        self.__remove_button.setText('Remove')
        self.__remove_button.clicked.connect(self.remove)
        self.__remove_button.setMinimumWidth(100)
        self.__exit_button.setText('Close')
        self.__exit_button.clicked.connect(self.close)
        self.__exit_button.setMinimumWidth(100)

        buttons = QHBoxLayout()
        buttons.addWidget(self.__remove_button)
        buttons.addItem(QSpacerItem(10, 0))
        buttons.addWidget(self.__exit_button)

        layout = QVBoxLayout()
        layout.addWidget(QLabel('Current menu:'))
        layout.addItem(QSpacerItem(0, 5))
        layout.addWidget(self.__list_widget)
        layout.addItem(buttons)

        self.setLayout(layout)

    def reload(self):
        self.__list_widget.clear()
        for item in self._storage.get_menu():
            row = QListWidgetItem()
            row.setText('{0:20}{1:5}'.format(str(item), item.get_price()))
            self.__list_widget.addItem(row)

    def remove(self):
        number = self.__list_widget.currentRow()
        if number == -1:
            return
        product = self._storage.get_menu()[number]
        self._storage.remove_from_menu(product)
        self.reload()

    def execute(self):
        self.move(600, 430)
        self.show()