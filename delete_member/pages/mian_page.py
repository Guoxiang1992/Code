# -- coding: utf-8 --
# @File : mian_page.py
import allure

from project.lagouPY.Homework.delete_member.pages.basepage import BasePage
from project.lagouPY.Homework.delete_member.pages.mail_list_page import MailListPage

class MainPage(BasePage):
    def goto_mail_list(self):
        self.data_driven('../pages/data.yml','alert')
        with allure.step('点击通讯录按钮，进入通讯录页面'):
            self.data_driven('../pages/data.yml','goto_maillist')
        return MailListPage(self.driver)