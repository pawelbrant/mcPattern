import sys

from PyQt5.QtWidgets import QApplication

from gui import ControlPanel, StaffMonitor, RegisterMonitor


if __name__ == '__main__':
    app = QApplication(sys.argv)

    monitor1 = StaffMonitor()
    monitor1.move(0, 200)
    monitor1.show()

    monitor2 = RegisterMonitor()
    monitor2.move(845, 200)
    monitor2.show()

    window = ControlPanel()
    window.move(600, 200)
    window.show()

    sys.exit(app.exec_())
