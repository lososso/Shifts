import PyPDF2


# Object creation

pdfFileObj = open('Operation2020.pdf','rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
pageObj = pdfReader.getPage(0)
Raw_Calendar = (pageObj.extractText())
Raw_Calendar = str(Raw_Calendar)
print (Raw_Calendar.split('\n'))

