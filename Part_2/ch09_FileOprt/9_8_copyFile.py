
import os, re, shutil

def backupScripts(src, dest):
    zipfileRegex = re.compile('^(.*)+\.(zip)$')
    pyfileRegex = re.compile('^(.*)+\.(py)$')
    pywfileRegex = re.compile('^(.*)+\.(pyw)$')
    batfileRegex = re.compile('^(.*)+\.(bat)$')
    filelist = os.listdir(src)
    for filename in filelist:
        print(filename)
        srcfilepath = os.path.join(src, filename)
        if os.path.isdir(srcfilepath):
            backupScripts(srcfilepath, dest)
        else:
            zipMatches = zipfileRegex.search(filename)
            if zipMatches != None:
                continue
            
            destfilepath = os.path.join(dest, filename)
            pyMatches = pyfileRegex.search(filename)
            if pyMatches != None:
                shutil.copyfile(srcfilepath, destfilepath)
                continue

            pywMatches = pywfileRegex.search(filename)
            if pywMatches != None:
                shutil.copyfile(srcfilepath, destfilepath)
                continue

            batMatches = batfileRegex.search(filename)
            if batMatches != None:
                shutil.copyfile(srcfilepath, destfilepath)
                continue

backupScripts('D:\\pyAuto', 'D:\\pyAuto_bk')
