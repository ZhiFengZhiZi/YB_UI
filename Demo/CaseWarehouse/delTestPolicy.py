from selenium import webdriver
import pytesseract
from PIL import Image
from time import  sleep
driver = webdriver.Firefox()
#driver.get('http://www.datoubao.com')
first_url ='http://www.datoubao.com'
driver.get(first_url)
sleep(3)
driver.find_element_by_xpath('//*[@id="content"]/div[1]/ul/li[1]').click()
sleep(2)
driver.find_element_by_xpath('//*[@id="loginPage"]/div/div/ul/li[2]').click()
driver.find_element_by_id('pusername').send_keys('wangsiyuan001')
driver.find_element_by_xpath('//*[@id="comuserpass"]').send_keys('abcd1234')
driver.find_element_by_xpath('//*[@id="comCode"]').send_keys('0000')
driver.find_element_by_xpath('//*[@id="comLoginBtn"]').click()
sleep(2)
try:
     rowCount = len(driver.find_elements_by_xpath('//*[@id="policy-content1"]/div/table/tbody/tr'))
     global j
     j=0
     for i in range(0,rowCount):
        j+=1
     driver.find_element_by_xpath('//*[@id="policy-content1"]/div/table/tbody/tr['+str(j)+']/td[7]/a[2]').click()
     sleep(2)
     driver.back()
     print(rowCount)

     sleep(2)


except Exception as e:
    print('左侧菜单栏入口错误'+str(e))
else:
    print('左侧菜单栏入口正确')
