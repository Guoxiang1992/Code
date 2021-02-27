# -- coding: utf-8 --
# @File : test_member_add.py
import allure
import pytest
from selenium.webdriver.common.by import By
from project.lagouPY.Homework.web_po_homework.page.main_page import MainPage

@allure.feature("测试企业微信成员的添加及查询")
class TestAdd:
    def setup(self):
        self.mainpage= MainPage() #类属性的实例化


    @allure.story("测试成员添加")
    @pytest.mark.parametrize('Name,Account,Phone_number',
                             [("A-21", "A-21", "13012345691"),
                              ("A-22", "A-22", "13012345692"),
                              ("A-23", "A-23", "13012345693")],
                             ids=['member1','member2','member3'])
    def test_add(self,Name,Account,Phone_number):
       self.mainpage.add_member().member_info(Name,Account,Phone_number)

    @allure.story("测试成员查询")
    def test_get_info(self):
        #做了个链式调用过程跳出的练习
        page = self.mainpage.add_member()
        with allure.step('点击通讯录'):
            page.find_ele(By.ID, 'menu_contacts').click()
        with allure.step('进行成员的查询'):
            page.get_member_info()
