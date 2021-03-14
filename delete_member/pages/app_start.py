# -- coding: utf-8 --
# @File : app_start.py
import allure
from appium import webdriver

from project.lagouPY.Homework.delete_member.pages.basepage import BasePage
from project.lagouPY.Homework.delete_member.pages.mian_page import MainPage

class AppStart(BasePage):
    def start_app(self):
        caps={
            "platformName": "android",
            "deviceName": "127.0.0.1",
            "appPackage": "com.tencent.wework",
            "appActivity": ".launch.WwMainActivity",
            "noReset": "true", #记录之前的操作或登录信息，不清除缓存
            "unicodeKeyBoard": "true",  # 需要输入非英文之外的语言
            "resetKeyBoard": "true",  # 重置回默认英文语言
            "skipDeviceInitialization": "true"  # 跳过设备初始化
        }
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub',caps)
        self.driver.implicitly_wait(5)
        return MainPage(self.driver)
