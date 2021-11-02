import sys, os, requests, bs4

currentpath = os.path.dirname(sys.argv[0])

print('###### 11.5.1')
exampleFile = open(os.path.join(currentpath, 'example.html'))
exampleSoup = bs4.BeautifulSoup(exampleFile)
print(type(exampleSoup))

print('###### 11.5.2')
exampleFile = open(os.path.join(currentpath, 'example.html'))
exampleSoup = bs4.BeautifulSoup(exampleFile, features="html.parser")
elems = exampleSoup.select('#author')
print(type(elems))
print(len(elems))
print(type(elems[0]))
print(elems[0].getText())
print(str(elems[0]))
print(elems[0].attrs)

print('###### 11.5.3')
soup = bs4.BeautifulSoup(open(os.path.join(currentpath, 'example.html')), features="html.parser")
spanElem = soup.select('span')[0]
print(str(spanElem))
print(spanElem.get('id'))
print(spanElem.get('some_nonexistent_addr') == None)
print(spanElem.attrs)