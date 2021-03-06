# -- coding: utf-8 --
# @File : add_member_page.py
from project.lagouPY.Homework.app_po.pages.basepage import BasePage
from project.lagouPY.Homework.app_po.pages.member_info_page import MemberInfo


class AddMember(BasePage):
    def goto_member_info(self):
        self.data_driven('../pages/data.yml','by2','locator2','action2')
        return MemberInfo(self.driver)