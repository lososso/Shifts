import read_PDF as RPDF
import sys
from PyQt4.QtGui import *


def main():
    calendar_dict = RPDF.main()
    #print calendar_dict
    year_list = ('January', 'February', 'March',
                 'April', 'May', 'June',
                 'July', 'August', 'September',
                 'October', 'November','December')


    create_gui(year_list,calendar_dict)


def create_gui(year_list,calendar_dict):
    a = QApplication(sys.argv)
    # The QWidget widget is the base class of all user interface objects in PyQt4.
    w = QWidget()
    main_layout = QGridLayout()
    w.setLayout(main_layout)
    # Set window title
    w.setWindowTitle("Shift Gui V0.1")
    for index, element in enumerate(year_list):
        label = QLabel(element)
        main_layout.addWidget(label, 0, (index))
        month = calendar_dict[element]
        for elements in month:
            day = elements[0]
            morning = elements[1]
            evening = elements[2]
            night = elements[3]
            shift_layout = QGridLayout()
            morning_label = QPushButton(morning)
            if morning == 'BL':
                morning_label.setStyleSheet("background-color: orange")
            if morning == 'M':
                morning_label.setStyleSheet("background-color: green")
            if morning == 'W':
                morning_label.setStyleSheet("background-color: cyan")
            if morning == 'OFF':
                morning_label.setStyleSheet("background-color: yellow")
            evening_label = QPushButton(evening)
            if evening == 'BL':
                evening_label.setStyleSheet("background-color: orange")
            if evening == 'M':
                evening_label.setStyleSheet("background-color: green")
            if evening == 'W':
                evening_label.setStyleSheet("background-color: cyan")
            if evening == 'OFF':
                evening_label.setStyleSheet("background-color: yellow")
            night_label = QPushButton(night)
            if night == 'BL':
                night_label.setStyleSheet("background-color: orange")
            if night == 'M':
                night_label.setStyleSheet("background-color: green")
            if night == 'W':
                night_label.setStyleSheet("background-color: cyan")
            if night == 'OFF':
                night_label.setStyleSheet("background-color: yellow")
            main_layout.addLayout(shift_layout,day,index)
            shift_layout.addWidget(morning_label,0,1)
            shift_layout.addWidget(evening_label,0,2)
            shift_layout.addWidget(night_label,0,3)

    for index in range (1,32):
        label = QLabel(str(index))
        main_layout.addWidget(label,index,0)
    # Show window
    w.show()
    sys.exit(a.exec_())


if __name__ == '__main__':
    main()
