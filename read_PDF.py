# Reading an excel file using Python
import xlrd

# Give the location of the file
loc = ("Operation2020-convertido.xlsx")

# To open Workbook
wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(3)
numRows = sheet.nrows
numColumns = sheet.ncols
print (numColumns, numRows)

# For row 0 and column 0
for i in range(0,numColumns):
    A = sheet.cell_value(0, i)
    month = str(A.split('\n'))
    print month

