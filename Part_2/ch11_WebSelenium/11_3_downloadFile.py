#! python

import sys, os, requests

currentpath = os.path.dirname(sys.argv[0])
print(currentpath)

res = requests.get('http://www.gutenberg.org/cache/epub/1112/pg1112.txt')
try:
    res.raise_for_status()
    playFile = open(os.path.join(currentpath, '11_3_RomeoAndJuliet.txt'), 'wb')
    for chunk in res.iter_content(100000):
        playFile.write(chunk)
    
    playFile.close()
except Exception as ex:
    print('There was a problem: %s' % (ex))
