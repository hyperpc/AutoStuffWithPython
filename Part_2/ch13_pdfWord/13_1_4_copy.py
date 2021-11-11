import PyPDF2, sys, os

def copyPdfs():
    currentPath = os.path.dirname(sys.argv[0])
    filepath1 = os.path.join(currentPath, 'meetingminutes.pdf')
    filepath2 = os.path.join(currentPath, 'meetingminutes2.pdf')
    pdf1File = open(filepath1, 'rb')
    pdf2File = open(filepath2, 'rb')
    pdf1Reader = PyPDF2.PdfFileReader(pdf1File)
    pdf2Reader = PyPDF2.PdfFileReader(pdf2File)
    pdfWriter = PyPDF2.PdfFileWriter()

    for pageNum in range(pdf1Reader.numPages):
        pageObj = pdf1Reader.getPage(pageNum)
        pdfWriter.addPage(pageObj)
    
    for pageNum in range(pdf2Reader.numPages):
        pageObj = pdf2Reader.getPage(pageNum)
        pdfWriter.addPage(pageObj)

    filepath3 = os.path.join(currentPath, 'combinedminutes.pdf')
    pdfOutputFile = open(filepath3, 'wb')
    pdfWriter.write(pdfOutputFile)
    pdfOutputFile.close()
    pdf1File.close()
    pdf2File.close()

def main():
    copyPdfs()

if __name__ == '__main__':
    main()