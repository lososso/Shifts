import read_PDF as RPDF
import sys
from PyQt4.QtGui import *


def main():
    loc2020 = "Operation2020-convertido.xlsx"
    loc2019 = "Operation2019-convertido.xlsx"
    calendar_dict = RPDF.main(loc2019)

    #print calendar_dict
    year_list = ('January', 'February', 'March',
                 'April', 'May', 'June',
                 'July', 'August', 'September',
                 'October', 'November','December')


    create_gui(year_list,calendar_dict)

def setButtonColor(button,shift_type):
    if shift_type == 'BL':
        button.setStyleSheet("background-color: orange")
    if shift_type == 'M':
        button.setStyleSheet("background-color: green")
    if shift_type == 'W':
        button.setStyleSheet("background-color: cyan")
    if shift_type == 'OFF':
        button.setStyleSheet("background-color: yellow")

def create_gui(year_list,calendar_dict):
    a = QApplication(sys.argv)
    # The QWidget widget is the base class of all user interface objects in PyQt4.
    w = QWidget()
    main_layout = QGridLayout()
    w.setLayout(main_layout)
    # Set window title
    w.setWindowTitle("Shift Gui V0.1")
    for index, element in enumerate(year_list):
        group = QGroupBox(element)
        group_layout = QGridLayout()
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
            setButtonColor(morning_label,morning)
            evening_label = QPushButton(evening)
            setButtonColor(evening_label,evening)
            night_label = QPushButton(night)
            setButtonColor(night_label,night)
            group_layout.addLayout(shift_layout,day,index + 1)
            shift_layout.addWidget(day_label,0,1)
            shift_layout.addWidget(morning_label,0,2)
            shift_layout.addWidget(evening_label,0,3)
            shift_layout.addWidget(night_label,0,4)


    # Show window
    w.show()
    sys.exit(a.exec_())


if __name__ == '__main__':
    main()
