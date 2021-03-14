# -- coding: utf-8 --
# @File : basepage.py

from appium.webdriver.webdriver import WebDriver
import yaml

from project.lagouPY.Homework.delete_member.conftest import logger
from project.lagouPY.Homework.delete_member.pages.black_list import blacklist
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:

    def __init__(self,driver:WebDriver=None):
        self.driver=driver
    @blacklist #这里用黑名单装饰器
    def find(self,by,locator):#定义一个find_element方法
        logger.info(f"Find: by={by} , locator = {locator}")
        return self.driver.find_element(by,locator)

    def finds(self,by,locator): #定义一个find_elements方法
        logger.info(f"Finds: by={by} , locator = {locator}")
        return self.driver.find_elements(by,locator)

    def save_photo(self,filename):
        return self.driver.get_screenshot_as_file(filename)

    def visibility_wait(self,timeout,by,locator):#定义一个显示等待方法
        wait_time = WebDriverWait(self.driver,timeout).until(EC.visibility_of_element_located((by,locator)))
        return wait_time

    def clickable_wait(self,timeout,by,locator):
        wait_time = WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable((by, locator)))
        return wait_time

    def data_driven(self,path,key,info=None): #定义一个数据驱动的方法
        with open(path,encoding='utf-8') as q:
            data = yaml.safe_load(q)
            ele = self.find(data[key]['by'],data[key]['locator'])

            if data[key]['action'] == 'click':
                ele.click()

            elif data[key]['action'] == 'send':
                content:str = data[key]['keys']
                for k in info:
                    content = content.replace('${%s}'%k,info[k]) #对yaml文件的变量替换成我们传入的参数
                ele.send_keys(content)

            elif data[key]['action'] == 'text':
                return  ele.text

    def datas_driven(self,path,key):
        with open(path,encoding='utf-8') as q:
            data = yaml.safe_load(q)
            eles = self.finds(data[key]['by'],data[key]['locator'])
            return eles
