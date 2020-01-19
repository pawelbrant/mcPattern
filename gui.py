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

        self.name = QLineEdit()

        self.start()


    def start(self):
        self.setWindowTitle('Mac Pattern')
        form = QFormLayout()
        form.addRow('Nazwa:', self.name)
        list = QListWidget()
        list.addItem('lol')
        list.addItem('nowu')
        form.addRow('Lista', list)
        button = QPushButton()
        button.clicked.connect(self.delete)
        form.addRow('przycisk', button)

        self.setLayout(form)

    def delete(self):
        s = Storage()
        s.cancel_order(s.get_orders()[0])

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
        form = QHBoxLayout()

        left_column = QVBoxLayout()
        left_column.addWidget(QLabel('Orders:'))
        left_column.addWidget(self.__orders)

        right_column = QVBoxLayout()
        right_column.addWidget(QLabel('Order contents:'))
        right_column.addWidget(self.__details)

        form.addItem(left_column)
        form.addSpacing(30)
        form.addItem(right_column)

        self.setLayout(form)

    def reload(self):
        self.__orders.clear()
        for item in self._order_list:
            row = QListWidgetItem()
            row.setText('#{:0>2}'.format(item.get_number()))
            self.__orders.addItem(row)
        self.__orders.itemSelectionChanged.connect(self.details)

    def details(self):
        self.__details.clear()
        id = self.__orders.currentRow()
        print(id)
        order = self._order_list[id]
        for item in order.get_product_list():
            self.__details.addItem(str(item))

    def invalidate(self):
        super(StaffMonitor, self).invalidate()
        self.reload()


# class RegisterMonitor(QWidget, Observer, metaclass=M_GUI_Observer):

#     def __init__(self, parent=None):
#         super(RegisterMonitor, self).__init__(parent)

#     def start(self):
#         self.setWindowTitle('Staff Observer')
#         form = QHBoxLayout()
#         orders = QListWidget()
#         form.addWidget(orders)

#         self.setLayout(form)