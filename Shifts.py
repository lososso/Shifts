import PyPDF2


# Object creation

pdfFileObj = open('Z:\Calendars\Operation2020.pdf','rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
pageObj = pdfReader.getPage(0)
Raw_Calendar = (pageObj.extractText())
