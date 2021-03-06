# -- coding: utf-8 --
# @File : basepage.py

from appium.webdriver.webdriver import WebDriver
import yaml

class BasePage:
    def __init__(self,driver:WebDriver=None):
        self.driver=driver

    def find_ele(self,by,locator):
        return self.driver.find_element(by,locator)

    def data_driven(self,path,by_method,ele_locator,action=None,send_info=None):
        with open(path,encoding='utf-8') as q:
            datas = yaml.safe_load(q)
        ele = self.find_ele(datas[by_method],datas[ele_locator])
        if datas[action] == 'click':
            ele.click()
        elif datas[action] == 'send':
            ele.send_keys(send_info)
        elif datas[action] == 'text':
            return  ele.text