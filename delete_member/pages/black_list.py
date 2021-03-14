# -- coding: utf-8 --
# @File : black_list.py
import allure
from selenium.webdriver.common.by import By

from project.lagouPY.Homework.delete_member.conftest import logger

blacklists=[(By.ID,'com.tencent.wework:id/ig0')]

def blacklist(func):
    def run(*args,**kwargs):
        error_min = 0
        error_max = 5
        self=args[0]#传进来的函数带了self参数位于参数索引0的位置,这里要进行定义
        try:
            error_min = 0
            return func(*args,**kwargs)
        except Exception as e:
            logger.error('捕获到异常弹框')
            self.save_photo('blacklist.png')
            allure.attach.file('blacklist.png', name='黑名单截图', attachment_type=allure.attachment_type.PNG)
            error_min += 1
            if error_min > error_max:
             raise e
            for black in blacklists:  # 遍历黑名单
                eles = self.finds(*black)  # 用finds方法遍历黑名单所有元素
                if len(eles) > 0:  # 大于0表示找到了黑名单中的元素，并以列表形式输出
                    eles[0].click()  # 一般一个页面基本只有一个弹框，所以直接取第一个进行点击即可
                    return func(*args, **kwargs)
            raise e
    return run