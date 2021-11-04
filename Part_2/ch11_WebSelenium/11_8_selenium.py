from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.keys import Keys

edgeService = Service('C:\Program Files\Python310\msedgedriver.exe')
browser = webdriver.Edge(service=edgeService)
print(type(browser))

browser.get('http://inventwithpython.com')

try:
    #elem = browser.find_element_by_class_name('.cover-thumb')
    elem = browser.find_element_by_css_selector('div > img.cover-thumb')
    print('Found <%s> element with that class name!' % (elem.tag_name))

    linkElem = browser.find_element_by_link_text('Read Online for Free')
    print(type(linkElem))
    linkElem.click()

    browser.get('http://gmail.com')
    emailElem = browser.find_element_by_id('Email')
    emailElem.send_keys('not_my_real_email@gmail.com')
    passwordElem = browser.find_element_by_id('Password')
    passwordElem.send_keys('12345')
    passwordElem.submit()

    browser.get('http://nostarch.com')
    htmlElem = browser.find_element_by_tag_name('html')
    htmlElem.send_keys(Keys.END)    # scrolls to bottom
    htmlElem.send_keys(Keys.HOME)   # scrolls to top
except:
    print('Wat not able to find an element with that name.')
