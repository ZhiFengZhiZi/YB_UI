from selenium import webdriver
from selenium.webdriver.common.by import By


from .init import BasePage

from selenium.webdriver.support.ui import Select
#投保类
class lipei(BasePage):
    #理赔信息
    yonghuzhongxin=(By.XPATH,'//*[@id="header"]/div[1]/div/ul/li[2]/a')

    wodesuopei =(By.XPATH,'//*[@id="myPolicy"]/div[1]/div/dl[3]/dt/a')
    woyaobaoan =(By.XPATH,'//*[@id="myPolicy"]/div[2]/form/div/div/ul/li[1]/a')
    baoanbtn =(By.XPATH,'//*[@id="myPolicy"]/div[2]/form/div/div/div[1]/div[3]/p/a')
#事故信息元素
    #时间控件
    date =(By.XPATH,'//*[@id="accTime"]')
    #省市区详细地址
    shenfen =(By.XPATH,'//*[@id="accProvince"]')
    shi =(By.XPATH,'//*[@id="accCity"]')
    qu=(By.XPATH,'//*[@id="accCountry"]')
    xiangxi =(By.XPATH,'//*[@id="address"]')
    #出险原因
    guyuanyiwaishiguCheckBox =(By.XPATH,'//*[@id="f_report"]/div[2]/div[3]/div/div/div[1]/p/label/em')
    guyuanyiwaishiguDetail =(By.XPATH,'//*[@id="f_report"]/div[2]/div[3]/div/div/div[1]/div/label[1]/em')
    disanzhezerenshigu =(By.XPATH,'//*[@id="f_report"]/div[2]/div[3]/div/div/div[2]/p/label/em')

    gongyibushan =(By.XPATH,'//*[@id="f_report"]/div[2]/div[3]/div/div/div[2]/div/label[1]/em')
    #作业品类
    zuoyepinleianzhuang=(By.XPATH,'//*[@id="f_report"]/div[2]/div[4]/div[1]/div[2]/label[1]/em')
    #报案人信息
    baoanrenxinming =(By.XPATH,'//*[@id="reporterName"]')
    baoanrendianhua =(By.XPATH,'//*[@id="reporterMobile"]')
    lianxirenxingming =(By.XPATH,'//*[@id="contactName"]')
    lianxirendianhua =(By.XPATH,'//*[@id="contactMobile"]')
    zuizhongbaoan =(By.ID,'submit')
    select1 = (By.ID,'accProvince')
    select2 =(By.ID,'accCity')
    select3 =(By.ID,'accCountry')
    select4 =(By.ID,'address')
#点击用户中心
    def click_main(self):
        ma=self.driver.find_element(*lipei.yonghuzhongxin)
        ma.click()
#点击我的索赔
    def click_suopeii(self):
        suo =self.driver.find_element(*lipei.wodesuopei)
        suo.click()
#点击左侧我要报案
    def click_baoann(self):
        bao =self.driver.find_element(*lipei.woyaobaoan)
        bao.click()
#点击报案
    def click_baan(self):
        baoo =self.driver.find_element(*lipei.baoanbtn)
        baoo.click()
#地址方法
    def selectone(self):
        sel = Select(self.driver.find_element(*lipei.select1))
        sel.select_by_value("P001")

    def selecttwo(self):
        se = Select(self.driver.find_element(*lipei.select2))
        se.select_by_value('C001')

    def selectthree(self):
        sele = Select(self.driver.find_element(*lipei.select3))
        sele.select_by_value('1')

    def selectfour(self, select4):
        selec = self.driver.find_element(*lipei.select4)
        selec.send_keys(select4)
#出险原因
    def click_firstReason(self):
        firstReason =self.driver.find_element(*lipei.guyuanyiwaishiguCheckBox)
        firstReason.click()
    def click_firstReasonDetail(self):
        secondReasonDetail =self.driver.find_element(*lipei.guyuanyiwaishiguDetail)
        secondReasonDetail.click()
    def click_secondReason(self):
        secondReason =self.driver.find_element(*lipei.disanzhezerenshigu)
        secondReason.click()
    def click_secondReasonDetail(self):
        secondReasonDetail =self.driver.find_element(*lipei.gongyibushan)
        secondReasonDetail.click()
#作业品类
    def click_pinlei(self):
        Pinlei = self.driver.find_element(*lipei.zuoyepinleianzhuang)
        Pinlei.click()
#报案人信息
    def send_oneName(self,baoanrenxinming):
        Name =self.driver.find_element(*lipei.baoanrenxinming)
        Name.send_keys(baoanrenxinming)
    def send_onephone(self,baoanrendianhua):
        phone = self.driver.find_element(*lipei.baoanrendianhua)
        phone.send_keys(baoanrendianhua)
    def send_twoName(self,lianxirenxingming):
        name = self.driver.find_element(*lipei.lianxirenxingming)
        name.send_keys(lianxirenxingming)
    def send_twophone(self,lianxirendianhua):
        Phone =self.driver.find_element(*lipei.lianxirendianhua)
        Phone.send_keys(lianxirendianhua)
    def click_baoan(self):
        Baoan = self.driver.find_element(*lipei.zuizhongbaoan)
        Baoan.click()

    def send_date(self):
#        Date = self.driver.find_element(*lipei.date)
#        Date.send_keys(date)
        js = "document.getElementById('accTime').removeAttribute('readonly');document.getElementById('accTime').setAttribute('value','2017-05-22 00:00:00');"
        self.driver.execute_script(js)
'''
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

'''
