import sys, os, PyPDF2, time

def timer(func):
    def wrapper(*args, **kwds):
        tstart = time.time()
        func(*args, **kwds)
        tstop = time.time()
        print('耗时%0.3f秒'%(tstop-tstart,))
    return wrapper

@timer
def readPdf():
    print('Start to read encrypted pdf...')
    currentPath = os.path.dirname(sys.argv[0])
    pdfPath = os.path.join(currentPath, 'meetingminutes_encrypted.pdf')
    pdfFileObj = open(pdfPath, 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    if pdfReader.isEncrypted:
        wordsFileObj = open(os.path.join(currentPath, 'dictionary.txt'))
        words = wordsFileObj.readlines()
        for word in words:
            if word == None:
                continue
            if word.strip() == '':
                continue
            result = pdfReader.decrypt(word.strip())
            if result == 0:
                result = pdfReader.decrypt(word.lower().strip())
                if result == 0:
                    continue
                elif result == 2:
                    print('owner password = ', word.lower().strip())
                    break
                elif result == 1:
                    print('user password = ', word.lower().strip())
                    break
                else:
                    continue
            elif result == 2:
                print('owner password = ', word)
                break
            elif result == 1:
                print('user password = ', word)
                break
            else:
                continue

    print('Completed to read encrypted pdf...')

def main():
    readPdf()

if __name__ == '__main__':
    main()