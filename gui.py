#GUI imports
from PyQt5.QtWidgets import QWidget, QListWidget, QFormLayout, QHBoxLayout, \
QLabel, QSpinBox, QDoubleSpinBox, QLineEdit, QTextEdit, QPushButton
from PyQt5.QtGui import QDoubleValidator

class ControlPanel(QWidget):
    """docstring for ControlPanel."""

    def __init__(self, facade, parent=None):
        super(ControlPanel, self).__init__(parent)
        self.facade = facade

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

        self.setLayout(form)
