import time

from selenium import webdriver

from PageObject.ToubaoANDViewPolicyDetail import toubao
from PageObject.login import loginpage
from PageObject.woyaolipei import lipei
from TestCaseInfo import TestCaseInfo
from common.time import timedata as tt
from common.url import DatoubaoLoginbaseUrl
from log import LogUtility
from report.report import TestReport

from selenium.webdriver.support.ui import Select
class login_case_F(object):
    #初始化
    def __init__(self,message='',Rid='',Rname=''):

            self.driver = webdriver.Firefox()
            self.base_url = DatoubaoLoginbaseUrl()

            #self.base_url='http://www.datoubao.com'
            self.Rid=Rid
            self.Rname=Rname
            self.testCaseInfo = TestCaseInfo(id=self.Rid, name=self.Rname, owner='zww')
            self.testResult = TestReport()
            #self.loginfo = LogInfo(filename="Test_TC_Login")
            self.log = LogUtility.LogC()
            self.message = message
            inferror=''
            self.inferror = inferror
    #执行方法
    def action(self, view=None):
        self.loginpage=loginpage(self.driver)#调用loginpage CLASS
        self.toubao=toubao(self.driver)#调用touao CLASS
        self.lipei =lipei(self.driver)#调用lipei  CLASS
    #捕获错误
        try:
            self.testCaseInfo.starttime = tt.getCurrentTime()#测试起始时间
            self.driver.get(self.base_url)#调取common里的URL
            time.sleep(3)
            self.driver.find_element_by_xpath('//*[@id="content"]/div[1]/div[2]/p/a[1]').click()#点击登陆按钮
            time.sleep(3)
            self.driver.find_element_by_xpath('//*[@id="loginPage"]/div/div/ul/li[2]').click()#点击账号登陆
            time.sleep(3)
    #输入账号信息
            self.loginpage.set_username('wangsiyuan001')
            self.loginpage.set_password('abcd1234')
            self.loginpage.set_code('0000')
            self.loginpage.click_SignIn()#点击登陆按钮
            time.sleep(5)
    #投保操作
            self.toubao.click_toubaoan()#点击我要投保
            time.sleep(1)
            self.toubao.click_chanpin()#点击投保产品
            time.sleep(2)
            self.toubao.click_checkbox()#点击保险条款复选框
            time.sleep(1)
            self.toubao.click_tijiao()#点击下一步进入付款页
            time.sleep(1)
           # self.toubao.zhengze()
            # 点击用户中心
            self.lipei.click_main()#点击用户中心
            time.sleep(1)
            self.toubao.click_mypolocy()#点击我的投保单
            time.sleep(1)
            self.toubao.click_chakan()#点击查看刚才投保的保单详情
            '''
            self.toubao.zhengzetwo()
            self.toubao.bidui()
            '''

            time.sleep(1)
     # 报案操作
            self.lipei.click_suopeii()#点击我的左侧索赔
            time.sleep(1)
            self.lipei.click_baoann() #点击我要报案
            time.sleep(1)
            self.lipei.click_baan()#点击已出险保单的报案
            time.sleep(1)
    #我的索赔报案操作
            self.lipei.send_date()#时间控件send时间
            #地址下拉框选择
            self.lipei.selectone()#出险地点省
            time.sleep(1)
            self.lipei.selecttwo()#市
            time.sleep(1)
            self.lipei.selectthree()#区
            time.sleep(1)
            self.lipei.selectfour('创智路1号')#详细地址
            time.sleep(1)
            self.lipei.click_firstReason()#出险原因一级
            time.sleep(1)
            self.lipei.click_firstReasonDetail()#出险原因一级下二级
            time.sleep(1)
            self.lipei.click_secondReason()#出险原因二级
            time.sleep(1)
            self.lipei.click_secondReasonDetail()#出险原因二级下二级
            time.sleep(1)
            self.lipei.click_pinlei()#作业品类复选框
            time.sleep(1)
        #报案人信息
            self.lipei.send_oneName('张三')#报案人姓名
            time.sleep(1)
            self.lipei.send_onephone('15852912823')#报案人电话
            time.sleep(1)
            self.lipei.send_twoName('李四')#联系人姓名
            time.sleep(1)
            self.lipei.send_twophone('15852913135')#联系人电话
            time.sleep(1)
            self.lipei.click_baoan()#最终报案按钮
            time.sleep(3)
            '''
               js = 'window.open("http://admin.datoubao.com/main/login.htm");'
            self.driver.execute_script(js)
            now_handle =self.driver.current_window_handle_handle
            print(now_handle)
            all_handles =self.driver.window_handles
            for handle in all_handles:
                print(handle)
                self.driver.switch_to_window(handle)
                time.sleep(5)
                
           # self.toubao.send_usename('admin')
            self.toubao.send_pw("222222")
            self.toubao.send_cde('0000')
            self.toubao.click_logn()

            '''



            self.testCaseInfo.result = "Pass"
        except Exception as err:#捕获错误并且输出到日志中
            self.testCaseInfo.errorinfo = str(err)
            self.inferror="Got error: " + str(err)




        finally:

            self.testCaseInfo.endtime = tt.getCurrentTime()
            self.testCaseInfo.secondsDuration = tt.timeDiff(self.testCaseInfo.starttime, self.testCaseInfo.endtime)


            self.message = self.inferror
            self.log.message = self.message


            self.testResult.WriteHTML(self.testCaseInfo)
            self.log.LoadAndRunTestCases()

            self.driver.close()



if __name__ == '__main__':

    login_case=login_case_F()
    login_case.action()


