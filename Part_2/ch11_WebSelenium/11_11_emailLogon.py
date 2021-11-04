from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def logon(username, password, toEmail, content):
    edgeService = Service('C:\Program Files\Python310\msedgedriver.exe')
    browser = webdriver.Edge(service=edgeService)
    browser.implicitly_wait(10) # 隐式等待
    browser.get('http://www.126.com')
    wait = WebDriverWait(browser, 10, 0.2) # 显示等待
    # waiting page loading
    browser.implicitly_wait(10)
    try:
        # switch frame
        browser.find_element_by_id('switchAccountLogin').click()
    except Exception as ex:
        print("Exception: ", ex.__context__)
        pass
    # account login frame is 0
    browser.switch_to.frame(0)
    # textbox of username
    browser.find_element_by_name('email').send_keys(username)
    # textbox of password
    browser.find_element_by_name('password').send_keys(password)
    # logon button
    browser.find_element_by_id('dologin').click()
    '''
    # check logout button
    #logout = wait.until(EC.element_to_be_clickable((By.XPATH, '//a[.="退出"]')))
    logout = wait.until(browser.find_element_by_id('_mail_component_80_80'))
    if logout:
        print('Logon successfully!')
    '''
    # write email
    wait.until(EC.element_to_be_clickable((By.XPATH, '//li[contains(@id,"_mail_component_")]//span[.="写信"]'))).click()
    #wait.until(browser.find_element_by_css_selector('li[contains(@id,"_mail_component")]>span[.="写信"]')).click()
    #wait.until(browser.find_element(By.XPATH, '//li[contains(@id,"_mail_component")]//span[.="写信"]')).click()
    #wait.until(browser.find_element(By.CSS_SELECTOR, 'ul.js-component-component.tJ0>li:nth(1)>span:eq(1)')).click()
    #wait.until(browser.find_element(By.CSS_SELECTOR, 'span.oz0')).click()
    # receiver
    address = wait.until(EC.visibility_of(browser.find_element_by_xpath('//input[@class="nui-editableAddr-ipt"]')))
    address.send_keys(toEmail)
    # subject
    subject = wait.until(EC.visibility_of(browser.find_element_by_xpath('//input[contains(@id,"subjectInput")]')))
    subject.send_keys("Testing email")
    # upload attachment
    attachments = browser.find_element_by_xpath('//input[@type="file"]')
    attachments.send_keys("D:\Workspace\AutoStuffWithPython\Part_2\ch11_WebSelenium\11_3_RomeoAndJuliet.txt")
    # switch frame, and then write content
    browser.switch_to_frame(browser.find_element_by_xpath('//iframe[@class="APP-editor-iframe"]'))
    browser.find_element_by_xpath('//body[@class="nui-scroll"]').send_keys(content)
    browser.switch_to.default_content()
    # send
    browser.find_element_by_xpath('//footer[contains(@class,"jp0")]/div[@role="button"]/span[.="发送"]').click()
    # assert to send successful
    assert "发送成功" in browser.page_source,"发送失败"
    print("邮件发送成功！")
    # force to check result
    time.sleep(2)
    browser.find_element_by_id('_mail_component_80_80').click()
    # close browser
    browser.quit()

def main():
    logon("song_icefire", "G@me@Throne", "houtong_an@163.com", "This is one testing email, plz have fun~")

if __name__ == '__main__':
    main()
