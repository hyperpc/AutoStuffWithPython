#！ python3
# lucky.py - Opens several Google search results.

import requests, sys, webbrowser, bs4

print('Bing') # display text while downloading the Google page
res = requests.get('https://cn.bing.com/search?q=' + ' '.join(sys.argv[1:]))
res.raise_for_status()

# Retrieve top search result links.
soup = bs4.BeautifulSoup(res.text, features='html.parser')

# Open a browser tab for each result.
linkElems = soup.select('ol#b_results> li.b_algo > div.b_title > h2 > a')
numOpen = min(5, len(linkElems))
for i in range(numOpen):
    #webbrowser.open('https://cn.bing.com' + linkElems[i].get('href'))
    webbrowser.open(linkElems[i].get('href'))