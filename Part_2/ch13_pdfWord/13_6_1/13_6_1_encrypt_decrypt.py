#! python3
from pathlib import Path
import PyPDF2, sys
from os import path, walk

def readEncryptedPdf():
    currentPath = path.dirname(sys.argv[0])
    token = sys.argv[1]   # swordfish
    print('currentPath = ', currentPath)
    print('token = ', token)
    folder = path.abspath(currentPath) # make sure folder is absolute
    #encryptedPath = path.join(folder, 'encrypted')
    #decryptedPath = path.join(folder, 'decrypted')
    print('Starting to encrypt pdf files...')
    for foldername, subfoldername, filenames in walk(folder):
        print('foldername = ', foldername)
        print('subfoldername = ', subfoldername)
        print('filenames = ', filenames)
        for filename in filenames:
            print('Path(filename).stem = ', Path(filename).stem)
            print('Path(filename).suffix = ', Path(filename).suffix)
            currentFilePath = path.join(foldername, filename)
            if(not filename.endswith('.pdf')):
                #print('skip file: ', filename)
                continue
            if('_decrypted.pdf' in filename):
                #print('skip file: ', currentFilePath)
                continue
            print('processing file: ', currentFilePath)
            srcPdf = open(currentFilePath, 'rb')
            reader = PyPDF2.PdfFileReader(srcPdf)
            writer = PyPDF2.PdfFileWriter()
            for pageNum in range(reader.numPages):
                writer.addPage(reader.getPage(pageNum))
            writer.encrypt(token)
            encryptedFilePath = path.join(foldername, Path(filename).stem + '_encrypted.pdf')
            destPdf = open(encryptedFilePath, 'wb')
            writer.write(destPdf)
            destPdf.close()
            print('encrypted file: ', encryptedFilePath)
    print('Completed to encrypt pdf files...')

    print('Starting to decrypt pdf files...')
    for foldername, subfoldername, filenames in walk(folder):
        print('foldername = ', foldername)
        print('subfoldername = ', subfoldername)
        print('filenames = ', filenames)
        for filename in filenames:
            currentFilePath = path.join(foldername, filename)
            if(not filename.endswith('.pdf')):
                #print('skip file: ', currentFilePath)
                continue
            if(not '_encrypted.pdf' in filename):
                #print('skip file: ', currentFilePath)
                continue
            print('processing file: ', currentFilePath)
            srcPdf = open(currentFilePath, 'rb')
            reader = PyPDF2.PdfFileReader(srcPdf)
            if reader.isEncrypted:
                reader.decrypt(token)
            writer = PyPDF2.PdfFileWriter()
            for pageNum in range(reader.numPages):
                writer.addPage(reader.getPage(pageNum))
            decryptedFilePath = path.join(foldername, filename.replace('_encrypted','_decrypted'))
            destPdf = open(decryptedFilePath, 'wb')
            writer.write(destPdf)
            destPdf.close()
            print('decrypted file: ', decryptedFilePath)
    print('Completed to decrypt pdf files...')
    print('Done~')

def main():
    readEncryptedPdf()

if __name__ == '__main__':
    main()