from selenium import webdriver
from selenium.webdriver.common.by import By
from .init import BasePage
from selenium.webdriver.common.keys import Keys

#投保类
class toubao(BasePage):
    #datoubao网页部分元素定位
    woyaotoubao =(By.XPATH,'//*[@id="toubao"]')
    dianjichanpin =(By.XPATH,'//*[@id="productList-content"]/div[8]/div[2]/p/a[2]')
    xiayibi = (By.XPATH,'//*[@id="insureRemember"]/div[2]/div[4]/p/a')
    checkboxx =(By.XPATH,'//*[@id="isred"]')
    #datoubao后台登陆页部分元素定位
    yonghuming =(By.NAME,'username')
    mima = (By.XPATH,'//*[@id="login-form"]/div[2]')
    yanzhengma =(By.XPATH,'//*[@id="login-form"]/div[3]')
    dengluanniu =(By.XPATH,'//*[@id="loginBtn"]')
    wodetoubaodan =(By.XPATH,'//*[@id="myPolicy"]/div[1]/div/dl[4]/dt/a')
    viewPolicy =(By.XPATH,'//*[@id="policy-content1"]/div/table/tbody/tr[2]/td[6]/a[2]')
    toubaodanhao =(By.XPATH,'//*[@id="policy-content1"]/div/table/tbody/tr[2]/td[1]')
    toubaodanhaotwo =(By.XPATH,'//*[@id="confirmProduct"]/form/div/div[1]/div[1]/div/span')
#点击我要投保
    def click_toubaoan(self):
        toubaobtn =self.driver.find_element(*toubao.woyaotoubao)
        toubaobtn.click()
#点击投保产品
    def click_chanpin(self):
        clkchanpin = self.driver.find_element(*toubao.dianjichanpin)
        clkchanpin.click()
#点击投保产品下一步按钮，进入信息生成投保单页
    def click_tijiao(self):
        tijiaobtn = self.driver.find_element(*toubao.xiayibi)
        tijiaobtn.click()
#点击保险条款复选框
    def click_checkbox(self):
        checkbox =self.driver.find_element(*toubao.checkboxx)
        checkbox.click()
#datoubao后台登陆
#输入用户名
    def send_usename(self,yonghuming):
        name = self.driver.find_element(*toubao.yonghuming)
        name.send_keys(yonghuming+Keys.RETURN )
        #输入密码
    def send_pw(self,mima):
        pwd = self.driver.find_element(*toubao.mima)
        pwd.send_keys(mima+Keys.RETURN)
        #输入验证码
    def send_cde(self,yanzhengma):
        code = self.driver.find_element(*toubao.yanzhengma)
        code.send_keys(yanzhengma+Keys.RETURN)
        #点击登陆按钮
    def click_logn(self):
        Login = self.driver.find_element(*toubao.dengluanniu)
        Login.click()
    def click_mypolocy(self):
        policy = self.driver.find_element(*toubao.wodetoubaodan)
        policy.click()
    def click_chakan(self):
        Chakan = self.driver.find_element(*toubao.viewPolicy)
        Chakan.click()


    def zhengze(self,viewtwo):
        viewtwo =self.driver.find_element(*toubao.toubaodanhaotwo).text
        viewtwo.type(viewtwo)
        viewtwo.type('str')


    def zhengzetwo(self,view):
        view = self.driver.find_element(*toubao.toubaodanhao).text
        view.type(view)
        view.type('str')
    def bidui(self, viewtwo,view):
        if viewtwo.type==view.type:
            print('true')