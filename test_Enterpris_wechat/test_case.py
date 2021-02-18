# -- coding: utf-8 --
# @File : test_case.py
import time
from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestMailList:
    def setup(self):
        condition = {
            "platformName": "android",
            "deviceName": "127.0.0.1",
            "appPackage": "com.tencent.wework",
            "appActivity": ".launch.WwMainActivity",
            "settings[waitForIdleTimeout]": 0,  # 把动态网页，当作静态处理，减少元素定位时间
            "noReset": "true",  # 记录之前的操作或登录信息，不清除缓存
            "skipDeviceInitialization": "true"  # 跳过设备初始化
        }
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", condition)
        self.driver.implicitly_wait(5)

    def test_add_members(self):
        self.driver.find_element_by_xpath("//*[@text='通讯录']").click()
        #注意当前页面可能会存在，通讯录人员过多，需要定位的元素不在页面显示范围内，所以选择滚动定位最为保险
        self.driver.find_element_by_android_uiautomator('new UiScrollable(new UiSelector().'
                                                        'scrollable(true).instance(0)).'
                                                        'scrollIntoView(new UiSelector().'
                                                        'text("添加成员").'
                                                        'instance(0));').click()
        self.driver.find_element_by_xpath("//*[@text='手动输入添加']").click()
        #这里特别要注意text的空格，是特殊空格去复制，不要手打空格，坑！！！！
        #通过父子层级关系进行元素定位，因为需要定位的元素属性不唯一
        self.driver.find_element_by_xpath("//*[@text='姓名　']/..//*[@resource-id='com.tencent.wework:id/b7m']").send_keys('张三')
        self.driver.find_element_by_xpath("//*[@text='帐号　']/..//*[@resource-id='com.tencent.wework:id/b7m']").send_keys('127678964')
        self.driver.find_element_by_id('com.tencent.wework:id/fwi').send_keys('18256765244')
        self.driver.find_element_by_xpath("//*[@text='性别']/..//*[@resource-id='com.tencent.wework:id/b8h']").click()
        #这里要注意最好用显示等待，虽然直接定位运行也是passed
        # self.driver.find_element_by_xpath("//*[@text='女']").click()
        WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((By.XPATH,"//*[@text='男']")))
        self.driver.find_element_by_xpath("//*[@text='女']").click()
        self.driver.find_element_by_id('com.tencent.wework:id/aj_').click()
        print(self.driver.page_source)  # 获取并打印当前页面的 dom树,找到Toast属性
        #定位Toast只能通过xpath定位,获取Toast的文本属性
        ele1=self.driver.find_element_by_xpath('//*[@class="android.widget.TextView"]').text
        #进行断言
        assert "处理中…" == ele1
        #这里有页面跳转，需要时间等待页面跳转过去，然后再进行后续操作
        time.sleep(1)
        print(self.driver.page_source)
        ele2 = self.driver.find_element_by_xpath('//*[@class="android.widget.Toast"]').text
        assert "添加成功" == ele2

