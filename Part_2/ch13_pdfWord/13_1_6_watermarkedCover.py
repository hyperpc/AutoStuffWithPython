import PyPDF2, sys, os

def addWatermarked():
    currentPath = os.path.dirname(sys.argv[0])
    orgFilepath = os.path.join(currentPath, 'meetingminutes.pdf')
    wmFilepath = os.path.join(currentPath, 'watermark.pdf')
    wmcFilepath = os.path.join(currentPath, 'watermarkedCover.pdf')

    minuteFile = open(orgFilepath, 'rb')
    reader = PyPDF2.PdfFileReader(minuteFile)
    minutesFirstPage = reader.getPage(0)
    wmcReader = PyPDF2.PdfFileReader(open(wmFilepath, 'rb'))
    minutesFirstPage.mergePage(wmcReader.getPage(0))
    writer = PyPDF2.PdfFileWriter()
    writer.addPage(minutesFirstPage)

    for pageNum in range(1, reader.numPages):
        pageObj = reader.getPage(pageNum)
        writer.addPage(pageObj)
    
    resultFile = open(wmcFilepath, 'wb')
    writer.write(resultFile)
    minuteFile.close()
    resultFile.close()

def main():
    addWatermarked()

if __name__ == '__main__':
    main()