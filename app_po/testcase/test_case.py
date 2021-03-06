# -- coding: utf-8 --
# @File : test_case.py
from project.lagouPY.Homework.app_po.pages.app_start import AppStart


class TestCase:
    def setup(self):
        self.start = AppStart()

    def test_case(self):
        self.start.start_app().goto_mail_list().goto_add_member().goto_member_info().add_member_info()
