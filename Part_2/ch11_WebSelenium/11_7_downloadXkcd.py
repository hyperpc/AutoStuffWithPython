#! python3
# downloadXkcd.py - Download every single XKCD comic.

import requests, bs4, sys, os

currentPath = os.path.dirname(sys.argv[0])

url = 'http://xkcd.com'             # starting url
os.makedirs(os.path.join(currentPath, 'xkcd'), exist_ok=True)  # store comics in ./xkcd
exit_condition = 0
while not url.endswith('#'):
    if exit_condition == 10:
        break

    # download the page.
    print('Downloading page %s...' % url)
    res = requests.get(url)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, features="html.parser")

    # find the URL of the comic image.
    comicElem = soup.select('#comic img')
    if comicElem == []:
        print('Could not find comic image.')
    else:
        comicUrl = comicElem[0].get('src')
        if not comicUrl.startswith('http:'):
            comicUrl = 'http:' + comicUrl
        # download the image.
        print('Downloading image %s...' % (comicUrl))
        res = requests.get(comicUrl)
        res.raise_for_status()
        # save the imge to ./xkcd.
        imageFile = open(os.path.join(currentPath, 'xkcd', os.path.basename(comicUrl)), 'wb')
        for chunk in res.iter_content(100000):
            imageFile.write(chunk)
        imageFile.close()

    # get the Prev button's url.
    prevLink = soup.select('a[rel="prev"]')[0]
    url = 'http://xkcd.com' + prevLink.get('href')

    exit_condition += 1

print('Done!')