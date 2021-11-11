import PyPDF2, sys, os

def readEncryptedPdf():
    currentPath = os.path.dirname(sys.argv[0])
    pdfPath = os.path.join(currentPath, 'encrypted.pdf')
    pdfReader = PyPDF2.PdfFileReader(open(pdfPath, 'rb'))
    print('pdfReader.isEncrypted = ', pdfReader.isEncrypted)
    if pdfReader.isEncrypted:
        print('pdfReader.decrypt(\'rosebud\')')
        pdfReader.decrypt('rosebud')
        print('pdfReader.numPages = ', pdfReader.numPages)
        pageObj = pdfReader.getPage(0)
        print('page(0) = ', pageObj.extractText())
    else:
        try:
            pageObj = pdfReader.getPage(0)
            print('page(0) = ', pageObj.extractText())
        except Exception as ex:
            print(ex)

def main():
    readEncryptedPdf()

if __name__ == '__main__':
    main()