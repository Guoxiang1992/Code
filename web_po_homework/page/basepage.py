# -- coding: utf-8 --
# @File : basepage.py
import yaml
from selenium.webdriver.remote.webdriver import WebDriver
from selenium import webdriver

class BasePage:

    def __init__(self,driver:WebDriver=None):
        """
        定义一个变量driver，并指明它的类型为WebDriver
        如果不传入webdriver，使用复用浏览器，端口为9222，如果传入webdriver则使用传入的webdriver进行测试
        :param driver:
        """
        if driver == None:
            option = webdriver.ChromeOptions()
            option.debugger_address='localhost:9222'
            self.driver = webdriver.Chrome(options=option)
            self.driver.implicitly_wait(5)
        else:
            self.driver = driver
            self.driver.implicitly_wait(5)

    def get_url(self,url):
        """
            定义一个打开网页的方法
            :param url:
        """
        self.driver.get(url)

    def find_ele(self,by,location):
        """
        定义一个find_element方法
        :param by:
        :param location:
        :return:
        """
        return self.driver.find_element(by, location)

    def finds_ele(self, by, location):
        return self.driver.find_elements(by, location)

    def date_driven(self,path,key,value,action,send_info):
        """
        定义一个数据驱动的方法
        """
        with open(path) as f:
            data = yaml.safe_load(f)
            ele = self.find_ele(data[key],data[value])
            if 'click' in data[action]:
                ele.click()
            if 'send_keys' in data[action]:
                ele.send_keys(send_info)