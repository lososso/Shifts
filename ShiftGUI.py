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
        main_layout.addWidget(label, 0, (index * 3))
        month = calendar_dict[element]
        for elements in month:
            day = elements[0]
            morning = elements[1]
            evening = elements[2]
            night = elements[3]
            morning_label = QLabel(morning)
            evening_label = QLabel(evening)
            night_label = QLabel(night)
            main_layout.addWidget(morning_label,day,(index))
            main_layout.addWidget(evening_label,day,(index * 2))
            main_layout.addWidget(night_label,day,(index*3))

    for index in range (1,32):
        label = QLabel(str(index))
        main_layout.addWidget(label,index,0)
    # Show window
    w.show()
    sys.exit(a.exec_())


if __name__ == '__main__':
    main()
