import PyPDF2, sys, os

def combinedPdfs():
    currentPath = os.path.dirname(sys.argv[0])
    # Get all the pdf filename
    pdfFiles = []
    #for filename in os.listdir('.\\Part_2\\ch13_pdfWord\\13_2\\'):
    for filename in os.listdir(os.path.join(currentPath, '13_2')):
        if filename.endswith('.pdf'):
            pdfFiles.append(filename)
    pdfFiles.sort(key=str.lower)
    writer = PyPDF2.PdfFileWriter()
    #loop through all the pdfs
    for filename in pdfFiles:
        pdfFileObj = open(os.path.join(currentPath, filename), 'rb')
        reader = PyPDF2.PdfFileReader(pdfFileObj)
        # loop through all the pages(except the first) and add them
        for pageNum in range(1, reader.numPages):
            pageObj = reader.getPage(pageNum)
            writer.addPage(pageObj)
    # save the resulting pdf to a file
    pdfOutput = open(os.path.join(currentPath, '13_2', 'allminutes.pdf'), 'wb')      
    writer.write(pdfOutput)
    pdfOutput.close()  

def main():
    combinedPdfs()

if __name__ == '__main__':
    main()