#! python3
import threading, requests, sys, os, bs4

def downloadXkcd(startComic, endComic):
    '''
    Download XKCD comics using multiple threads.
    '''
    for urlNum in range(startComic, endComic):
        # download the page
        url = 'http://xkcd.com/' + str(urlNum)
        if urlNum == 404:
            continue
        print('>>> downloading page %s\n' % (url))
        res = requests.get(url)
        res.raise_for_status()

        soup = bs4.BeautifulSoup(res.text, features="html.parser")

        # find the url of the comic image
        comicElem = soup.select('#comic img')
        if comicElem == '':
            print('>>> Could not find comic page!')
        else:
            comicUrl = comicElem[0].get('src')
            if not comicUrl.startswith('http:'):
                comicUrl = 'http:' + comicUrl
            # download the image
            print('>>> Downloading image %s...\n' % (comicUrl))
            res = requests.get(comicUrl)
            res.raise_for_status()

            # save the image to .\xkcd
            currentPath = os.path.dirname(sys.argv[0])
            xkcdPath = os.path.join(currentPath, 'xkcd')
            if not os.path.exists(xkcdPath):
                os.makedirs(xkcdPath)

            xkcdFilePath = os.path.join(xkcdPath, os.path.basename(comicUrl))    
            imageFile = open(xkcdFilePath, 'wb')
            for chunk in res.iter_content(100000):
                imageFile.write(chunk)
            imageFile.close()

def multipleDownload():
    # create and start the Thread objects
    downloadThreads = []
    for i in range(1, 1400, 100):
        downloadThread = threading.Thread(target=downloadXkcd, args=(i, i + 99))
        downloadThreads.append(downloadThread)
        downloadThread.start()
    #wait for all threads to end
    for downloadThread in downloadThreads:
        downloadThread.join()
    print('>>> Done.')

def main():
    #print('>>> current path = ', os.path.dirname(sys.argv[0]))
    multipleDownload()

if __name__ == '__main__':
    main()