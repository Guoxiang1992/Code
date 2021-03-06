# -- coding: utf-8 --
# @File : mian_page.py
from project.lagouPY.Homework.app_po.pages.basepage import BasePage
from project.lagouPY.Homework.app_po.pages.mail_list_page import MailListPage


class MainPage(BasePage):
    def goto_mail_list(self):
        self.data_driven('../pages/data1.yml','by1','locator1','action1')
        return MailListPage(self.driver)