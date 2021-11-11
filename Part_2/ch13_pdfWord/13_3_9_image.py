import docx, sys, os

def addImage():
    currentPath = os.path.dirname(sys.argv[0])
    imgFilePath = os.path.join(currentPath, 'zophie.png')
    docFilePath = os.path.join(currentPath, 'img_my.docx')
    doc = docx.Document()
    doc.add_picture(imgFilePath, width = docx.shared.Inches(4), height = docx.shared.Cm(16))
    doc.save(docFilePath)

def main():
    addImage()

if __name__ == '__main__':
    main()
