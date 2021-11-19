from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains as AC

# Python310以前：
# 如果将webdriver的实例化放在方法内，一旦方法打执行完成，浏览器就会自动关闭
# 所以可以借助option参数，将浏览器线程detach出来，不再受方法作用域的限制;
# Python310之后：
# 

edgeService = Service('C:\Program Files\Python310\msedgedriver.exe')
option = webdriver.EdgeOptions()
option.add_experimental_option('useAutomationExtension', False)
option.add_experimental_option('excludeSwitches', ['enable-automation'])
option.add_experimental_option("detach", True)
browser = webdriver.Edge(service=edgeService, options=option)

def test_selenium():
    '''
    edgeService = Service('C:\Program Files\Python310\msedgedriver.exe')
    #option = webdriver.EdgeOptions()
    option = webdriver.EdgeOptions()
    option.add_experimental_option('useAutomationExtension', False)
    option.add_experimental_option('excludeSwitches', ['enable-automation'])
    option.add_experimental_option("detach", True)
    browser = webdriver.Edge(service=edgeService, options=option)
    '''
    print(type(browser))

    #browser.get('http://inventwithpython.com')
    browser.get('https://www.u17.com/')
    '''
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
    '''
    # 强制关闭浏览器
    #browser.quit()

def main():
    test_selenium()

if __name__ == '__main__':
    main()