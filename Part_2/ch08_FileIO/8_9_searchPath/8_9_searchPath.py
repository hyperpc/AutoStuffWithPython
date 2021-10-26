#! python3
#
# please input 'C#' to search file content

import re, os, sys

print(os.getcwd())
print(sys.argv)
currentPath = os.path.dirname(sys.argv[0])
print(currentPath)

print('Enter regrex expression that you want to search in file folder:')
myRegex = input()
fileNameList = os.listdir(currentPath)
if fileNameList != None:
    filecontentRegex = re.compile(myRegex)
    fileNameRegex = re.compile(r'.txt$')
    for filename in fileNameList:
        if fileNameRegex.search(filename) == None:
            continue
        if fileNameRegex.search(filename).group() == None:
            continue
        print('=====' + filename)
        filepath = os.path.join(currentPath, filename)
        fileObj = open(filepath)
        #content = fileObj.read()
        contentLines = fileObj.readlines()
        if contentLines == None:
            continue
        
        for line in contentLines:
            if filecontentRegex.search(line) == None:
                continue
            if filecontentRegex.search(line).group() == None:
                continue            
            print(line)

        fileObj.close()
