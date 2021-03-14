# -- coding: utf-8 --
# @File : testcase.py
import allure

from project.lagouPY.Homework.delete_member.pages.app_start import AppStart


class TestDelete:
    member_info={'name':'A-12'}
    def setup(self):
        self.start=AppStart()
    @allure.story('成员删除测试')
    def test_delete(self):
        info = self.member_info
        self.start.start_app().goto_mail_list().goto_search().search_info(info).goto_delete()