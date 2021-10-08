from PySide6 import QtWidgets
from cases.demo_ihm.pyside_examples import form_widgets

class BaseWidget(QtWidgets.QWidget):
    """
    Base d'un widget
    """
    def __init__(self):
        super().__init__()


class BaseDialog(QtWidgets.QDialog):
    """
    Base d'un dialog
    """
    def __init__(self):
        super().__init__()

class DemoMainWindow(QtWidgets.QMainWindow):
    """
    Main Window Widget
    """
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Main app")
        self.setCentralWidget(form_widgets.MainWindget())



class MessageDialog(QtWidgets.QDialog):
    """
    Un dialog avec message
    """
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Dialog Widget")

        QBn = QtWidgets.QDialogButtonBox.Cancel | QtWidgets.QDialogButtonBox.Ok

        self.buttonsBox = QtWidgets.QDialogButtonBox(QBn)
        self.buttonsBox.accepted.connect(self.accept)
        self.buttonsBox.rejected.connect(self.reject)

        self.layout = QtWidgets.QVBoxLayout()
        message = QtWidgets.QLabel("Something happened, is that OK?")
        self.layout.addWidget(message)
        self.layout.addWidget(self.buttonsBox)
        self.setLayout(self.layout)



class SimpleButton(QtWidgets.QWidget):
    """
    Widget avec un bouton
    """
    def __init__(self):
        super().__init__()

        self.button = QtWidgets.QPushButton("Click Me")
        # self.button.setCheckable(True) #  Pour le rendre "checkable"

        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.button)

class SimpleLogButton(QtWidgets.QDialog):
    """
    Bouton avec une action
    """
    def __init__(self):
        super().__init__()

        self.button = QtWidgets.QPushButton("Click Me")
        self.button.clicked.connect(self.log_something)

        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.button)

    def log_something(self):
        print("Something logged")
        dlg = MessageDialog()
        dlg.exec()

class MultipleSignalsButton(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.button = QtWidgets.QPushButton("Click Me")
        self.button.setCheckable(True)
        self.button.clicked.connect(self.log_something)
        self.button.clicked.connect(self.log_checked)

        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.button)

    def log_something(self):
        print("Something logged")

    def log_checked(self, checked):
        if checked:
            self.button.setText("Unclick me")
        else:
            self.button.setText("Click me")


class LayoutWidget(QtWidgets.QWidget):
    def __init__(self):
        super(LayoutWidget, self).__init__()

        ok_button = QtWidgets.QPushButton('Ok')
        ok_button.clicked.connect(self.display_text_field)
        cancel_button = QtWidgets.QPushButton("Cancel")
        cancel_button.clicked.connect(self.cancel_text_field)

        b_layout = QtWidgets.QHBoxLayout()
        b_layout.addStretch(1)
        b_layout.addWidget(ok_button)
        b_layout.addWidget(cancel_button)

        self.text_field = QtWidgets.QLineEdit()
        self.text_field.textChanged[str].connect(self.on_changed)

        self.cb = QtWidgets.QCheckBox("A checkbox", self)
        self.cb.toggle()
        self.cb.stateChanged.connect(self.state_change_action)

        f_layout = QtWidgets.QVBoxLayout()
        f_layout.addStretch(1)
        f_layout.addWidget(self.text_field)
        f_layout.addWidget(self.cb)
        f_layout.addLayout(b_layout)

        self.setLayout(f_layout)
        self.setGeometry(300, 300, 300, 150)

    def state_change_action(self):
        print(self.cb.isChecked())

    def on_changed(self, text):
        print(text)

    def display_text_field(self):
        print(self.text_field.text())

    def cancel_text_field(self):
        self.text_field.setText("")

class CalculatorWidget(QtWidgets.QWidget):
    def __init__(self):
        super(CalculatorWidget, self).__init__()

        grid = QtWidgets.QGridLayout(self)

        value = 1
        for i in range(3, 0, -1):
            for j in range(3):
                button = QtWidgets.QPushButton(str(value))
                grid.addWidget(button, i, j)
                value += 1
