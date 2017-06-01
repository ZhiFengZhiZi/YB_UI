from selenium import webdriver
from selenium.webdriver.common.by import By
from .init import BasePage
import selenium.webdriver.common.keys


class loginpage(BasePage):
#    driver.find_element_by_xpath('//*[@id="content"]/div[1]/div[2]/p/a[1]').click()
#    driver.find_element_by_xpath('//*[@id="loginPage"]/div/div/ul/li[2]').click()
    username = (By.NAME, 'pusername')
    password = (By.NAME, 'com-userpass')
    code = (By.NAME, 'comCode')
    codebutton = (By.XPATH, '//*[@id="img1"]')
    loginbutton = (By.ID, 'comLoginBtn')



    def set_username(self, username):
        name = self.driver.find_element(*loginpage.username)
        name.send_keys(username)

        # Get password textbox and input password, then hit return

    def set_password(self, password):
        pwd = self.driver.find_element(*loginpage.password)
        pwd.send_keys(password + selenium.webdriver.common.keys.Keys.RETURN)


        # Get "cancel" button and then click

    def set_code(self,code):
        cod = self.driver.find_element(*loginpage.code)
        cod.send_keys(code)

        # click Sign in

    def click_SignIn(self):
        okbtn = self.driver.find_element(*loginpage.loginbutton)
        okbtn.click()

    def click_Authcode(self):
        authcode = self.driver.find_element(*loginpage.codebutton)
        authcode.click()

