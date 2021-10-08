from PySide6 import QtWidgets, QtGui, QtCore

class EpisodeForm(QtWidgets.QWidget):
    def __init__(self):
        super(EpisodeForm, self).__init__()

        self._title_field = QtWidgets.QLineEdit()
        self._number_field = QtWidgets.QSpinBox()
        self._season_field = QtWidgets.QSpinBox()

        self._number_field.setMinimum(1)
        self._number_field.setMaximum(100)
        self._season_field.setMaximum(100)

        _form_layout = QtWidgets.QGridLayout()
        _form_layout.addWidget(QtWidgets.QLabel("Title"), 0, 0)
        _form_layout.addWidget(QtWidgets.QLabel("Number"), 1, 0)
        _form_layout.addWidget(QtWidgets.QLabel("Season"), 2, 0)
        _form_layout.addWidget(self._title_field, 0, 1)
        _form_layout.addWidget(self._number_field, 1, 1)
        _form_layout.addWidget(self._season_field, 2, 1)

        self.setLayout(_form_layout)

    def set_values(self, title, season, number):
        self._title_field.setText(title)
        self._season_field.setValue(int(season))
        self._number_field.setValue(int(number))

    def collect_items(self):
        return self._title_field.text(),\
               self._season_field.text(), self._number_field.text()

class EpisodesChooser(QtWidgets.QWidget):
    def __init__(self):
        super(EpisodesChooser, self).__init__()
        self._shows_display = QtWidgets.QTreeWidget()
        self._shows_display.setColumnCount(2)
        self._shows_display.setHeaderLabels(["Episodes", "Infos"])

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self._shows_display)
        self.setLayout(layout)

    def load_data(self, shows):
        show_items = []
        for show in shows:
            show_item = QtWidgets.QTreeWidgetItem([show.name])
            for episode in show.episodes:
                episode_item = QtWidgets.QTreeWidgetItem([episode.title, f"s{episode.season_number}e{episode.number}"])
                show_item.addChild(episode_item)
            show_items.append(show_item)
        self._shows_display.insertTopLevelItems(0, show_items)



class ControlPanel(QtWidgets.QWidget):
    def __init__(self):
        super(ControlPanel, self).__init__()

        self.button_add = QtWidgets.QPushButton("Add")
        self.button_cancel = QtWidgets.QPushButton("Cancel")
        self.button_exit = QtWidgets.QPushButton("Quit")

        buttons_layout = QtWidgets.QHBoxLayout()
        buttons_layout.addWidget(self.button_add)
        buttons_layout.addWidget(self.button_cancel)
        buttons_layout.addWidget(self.button_exit)

        self.setLayout(buttons_layout)

class MainWindget(QtWidgets.QWidget):
    def __init__(self):
        super(MainWindget, self).__init__()
        self.episodes = EpisodesChooser()
        control = ControlPanel()
        self.form = EpisodeForm()

        control.button_add.clicked.connect(self.display_elements)
        control.button_exit.clicked.connect(QtCore.QCoreApplication.instance().quit)

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(EpisodesChooser())
        layout.addWidget(self.form)
        layout.addWidget(control)

        self.setLayout(layout)


    def display_elements(self):
        print(self.form.collect_items())
