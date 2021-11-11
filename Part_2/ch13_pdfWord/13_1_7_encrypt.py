import PyPDF2, sys, os

def encryptPdf():
    currentPath = os.path.dirname(sys.argv[0])
    orgFilepath = os.path.join(currentPath, 'meetingminutes.pdf')
    encryptedFilepath = os.path.join(currentPath, 'encryptedminutes_my.pdf')
    reader = PyPDF2.PdfFileReader(open(orgFilepath, 'rb'))
    writer = PyPDF2.PdfFileWriter()

    for pageNum in range(reader.numPages):
        writer.addPage(reader.getPage(pageNum))
    
    writer.encrypt('swordfish')
    encryptedPdf = open(encryptedFilepath, 'wb')
    writer.write(encryptedPdf)
    encryptedPdf.close()

def main():
    encryptPdf()

if __name__ == '__main__':
    main()