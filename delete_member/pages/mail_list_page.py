# -- coding: utf-8 --
# @File : mail_list_page.py

from project.lagouPY.Homework.delete_member.pages.basepage import BasePage
from project.lagouPY.Homework.delete_member.pages.search_page import Search


class MailListPage(BasePage):
    def goto_search(self):
        self.data_driven('../pages/data.yml','goto_search')
        return Search(self.driver)

