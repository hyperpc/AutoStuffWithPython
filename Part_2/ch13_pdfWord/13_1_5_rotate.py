import PyPDF2, sys, os

def rotatePage():
    currentPath = os.path.dirname(sys.argv[0])
    orgFilepath = os.path.join(currentPath, 'meetingminutes.pdf')
    rotateFilepath = os.path.join(currentPath, 'rotatePage.pdf')
    minutesFile = open(orgFilepath, 'rb')
    reader = PyPDF2.PdfFileReader(minutesFile)
    page = reader.getPage(0)
    print(page.rotateClockwise(90))
    writer = PyPDF2.PdfFileWriter()
    writer.addPage(page)
    resultPdfFile = open(rotateFilepath, 'wb')
    writer.write(resultPdfFile)
    resultPdfFile.close()
    minutesFile.close()

def main():
    rotatePage()

if __name__ == '__main__':
    main()