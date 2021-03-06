# -- coding: utf-8 --
# @File : mail_list_page.py
from appium.webdriver.common.mobileby import MobileBy

from project.lagouPY.Homework.app_po.pages.add_member_page import AddMember
from project.lagouPY.Homework.app_po.pages.basepage import BasePage


class MailListPage(BasePage):
    def goto_add_member(self):
        self.find_ele(MobileBy.ANDROID_UIAUTOMATOR,'new UiScrollable(new UiSelector().'
                                                   'scrollable(true).instance(0)).'
                                                   'scrollIntoView(new UiSelector().'
                                                   'text("添加成员").instance(0));').click()
        return AddMember(self.driver)