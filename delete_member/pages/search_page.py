# -- coding: utf-8 --
# @File : search_page.py
import allure

from project.lagouPY.Homework.delete_member.pages.basepage import BasePage
from project.lagouPY.Homework.delete_member.pages.delete_page import DeleteMember


class Search(BasePage):
    @allure.story('输入想删除成员的名字')
    def search_info(self,info):
        self.data_driven('../pages/data.yml','search_info',info)
        return DeleteMember(self.driver)