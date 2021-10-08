from PySide6 import QtWidgets
from cases.demo_ihm.pyside_examples import demo_widgets, form_widgets
import sys

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    window = demo_widgets.DemoMainWindow()
    window.show()

    sys.exit(app.exec())