import read_PDF
from PyQt5.QtWidgets import QApplication, QLabel, QGridLayout, QWidget, QGroupBox, QPushButton, QVBoxLayout


def main():
    loc2020 = "Operation2020-convertido.xlsx"
    loc2019 = "Operation2019-convertido.xlsx"
    calendar_dict = read_PDF.main(loc2019)
    year_list = ('January', 'February', 'March',
                 'April', 'May', 'June',
                 'July', 'August', 'September',
                 'October', 'November', 'December')
    create_gui(year_list, calendar_dict)


def set_button_color(button, shift_type):
    if shift_type == 'BL':
        button.setStyleSheet("background-color: orange")
    if shift_type == 'M':
        button.setStyleSheet("background-color: green")
    if shift_type == 'W' or shift_type == 'PSS' or shift_type == 'SPR':
        button.setStyleSheet("background-color: cyan")
    if shift_type == 'OFF':
        button.setStyleSheet("background-color: yellow")


def create_gui(year_list, calendar_dict):
    app = QApplication([])
    # The QWidget widget is the base class of all user interface objects in PyQt4.
    w = QWidget()
    main_layout = QGridLayout()
    w.setLayout(main_layout)
    # Set window title
    w.setWindowTitle("Shift Gui V0.1")
    for (index), element in enumerate(year_list):
        group = QGroupBox(element)
        group_layout = QVBoxLayout()
        group.setLayout(group_layout)
        main_layout.addWidget(group, 0, (index + 1))
        month = calendar_dict[element]
        for elements in month:
            day = elements[0]
            if day > 9:
                day_label = QLabel(str(day))
            else:
                day_label = QLabel('0' + str(day))
            morning = elements[1]
            evening = elements[2]
            night = elements[3]
            shift_layout = QGridLayout()
            morning_label = QPushButton(morning)
            set_button_color(morning_label, morning)
            evening_label = QPushButton(evening)
            set_button_color(evening_label, evening)
            night_label = QPushButton(night)
            set_button_color(night_label, night)
            group_layout.addLayout(shift_layout)
            shift_layout.addWidget(day_label, 0, 1)
            shift_layout.addWidget(morning_label, 0, 2)
            shift_layout.addWidget(evening_label, 0, 3)
            shift_layout.addWidget(night_label, 0, 4)
    w.show()
    app.exec_()


if __name__ == '__main__':
    main()