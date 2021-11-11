import PyPDF2, sys, os

def readPdf():
    currentPath = os.path.dirname(sys.argv[0])
    pdfPath = os.path.join(currentPath, 'meetingminutes.pdf')
    pdfFileObj = open(pdfPath, 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    print('pdfReader.numPages = ', pdfReader.numPages)
    pageObj = pdfReader.getPage(0)
    print('page(0) = ', pageObj.extractText())

def main():
    readPdf()

if __name__ == '__main__':
    main()