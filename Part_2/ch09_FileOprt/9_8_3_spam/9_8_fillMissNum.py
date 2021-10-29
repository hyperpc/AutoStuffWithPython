import os, re, sys, shutil

currentPath = os.path.dirname(sys.argv[0])
print(currentPath)

srcFileDict = {}
seqRegex = re.compile('^(spam)([0-9]{3})(\.txt)$')
fileCount = 1
for filename in os.listdir(currentPath):
    if os.path.isdir(filename):
        continue
    matches = seqRegex.search(filename)
    if matches == None:
        continue
    if matches.lastindex != 3:
        continue
    srcFileDict[fileCount] = filename
    fileCount = fileCount + 1

for i in range(1, fileCount):
    dstSeqNum = str(i).rjust(3, '0')
    dstFileName = 'spam' + dstSeqNum + '.txt'
    if dstFileName in srcFileDict.items():
        continue
    else:
        #shutil.move(os.path.join(currentPath, srcFileDict[i]), os.path.join(currentPath, dstFileName))
        print('src: ' + os.path.join(currentPath, srcFileDict[i]))
        print('dst: ' + os.path.join(currentPath, dstFileName))
