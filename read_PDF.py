# Reading an excel file using Python
import xlrd

def main():
    # Give the location of the file
    loc = "Operation2020-convertido.xlsx"
    [numrows,numcolumns,sheet] = readExcel(loc)
    year_dict = getMonths(sheet,numcolumns)
    year_list = ('January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October',
                 'November', 'December')
    # For row 0 and column 0
    for months in year_list:
        shifts = getShifts(year_dict,months,numrows,sheet)
        year_dict[months] = shifts
    print year_dict


def decodeUnicode(data):
    if data == u'BL' or data == u'bl':
        data = 'BL'
    if data == u'M':
        data = 'M'
    if data == u'W' or data == u'  SPR ':
        data = 'W'
    if data == u'Off':
        data = 'OFF'
    return data


def readExcel(path):
    # To open Workbook
    wb = xlrd.open_workbook(path)
    sheet = wb.sheet_by_index(3)
    numrows = sheet.nrows
    numcolumns = sheet.ncols
    return numrows, numcolumns, sheet


def getMonths(sheet, numcolumns):
    count = 0
    Year = {}
    for i in range(0,numcolumns):
        A = sheet.cell_value(0, i)
        month = str(A.split('\n'))
        if len(month)> 12:
            count = count + 1
            if count == 1:
                month = "January"
            if count == 2:
                month = "February"
            if count == 3:
                month = "March"
            if count == 4:
                month = "April"
            if count == 5:
                month = "May"
            if count == 6:
                month = "June"
            if count == 7:
                month = "July"
            if count == 8:
                month = "August"
            if count == 9:
                month = "September"
            if count == 10:
                month = "October"
            if count == 11:
                month = "November"
            if count == 12:
                month = "December"
            if count > 12:
                break
            Year[month] = i
    return Year

def getShifts(year_dict,month,numrows,sheet):
    index = year_dict[month]
    day = 1
    morning = 2
    evening = 3
    night = 4
    monthday = []
    morningShifts = []
    eveningShifts = []
    nightShifts = []
    for i in range(1,numrows):
        A = sheet.cell_value(i, index + day)
        if A != u'':
            date = int(A)
            monthday.append(date)
    for i in range(1,numrows):
        A = sheet.cell_value(i, index + morning)
        if A != u'':
            result = decodeUnicode(A)
            morningShifts.append(result)
    for i in range(1,numrows):
        A = sheet.cell_value(i, index + evening)
        if A != u'':
            result = decodeUnicode(A)
            eveningShifts.append(result)
    for i in range(1,numrows):
        A = sheet.cell_value(i, index + night)
        if A != u'':
            result = decodeUnicode(A)
            nightShifts.append(result)
    shifts = zip(monthday,morningShifts,eveningShifts,nightShifts)
    return shifts


if __name__ == '__main__':
    main()
