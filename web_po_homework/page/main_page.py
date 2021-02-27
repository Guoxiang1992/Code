# -- coding: utf-8 --
# @File : main_page.py
from project.lagouPY.Homework.web_po_homework.page.basepage import BasePage
from project.lagouPY.Homework.web_po_homework.page.member_info import Memberinfo

class MainPage(BasePage):
    def add_member(self):
        """
        1.通过复用浏览器，直接进入已登录企业微信主页，调用基类数据驱动方法，查找到成员添加的元素并点击
        2.return，在点击完成后跳转到成员添加的页面进行后续操作
        :return:
        """
        self.get_url('https://work.weixin.qq.com/wework_admin/frame')
        self.date_driven('../page/data.yml','by1','value1','action1',None)
        return Memberinfo(self.driver)