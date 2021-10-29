
import os, re

def delBigFile(src):
    filelist = os.listdir(src)
    zipfileRegex = re.compile('^(.*)+\.(zip)$')
    for filename in filelist:
        srcfilepath = os.path.join(src, filename)
        if os.path.isdir(srcfilepath):
            delBigFile(srcfilepath)
        else:
            #zipMatches = zipfileRegex.search(srcfilepath)
            #if zipMatches != None:
            #    filesize = os.path.getsize(srcfilepath)
            filesize = os.path.getsize(srcfilepath)
            print('>> Size of ' + srcfilepath + ': ' + str(filesize))

delBigFile('D:\\pyAuto')