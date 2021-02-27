# -- coding: utf-8 --
# @File : member_info.py
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from project.lagouPY.Homework.web_po_homework.page.basepage import BasePage

class Memberinfo(BasePage):
    def member_info(self,name,account,phone_number):
        """
        被添加成员的信息填写
        加入一个显示等待，然分别输入成员的name,account,phone_number，并点击保存
        :param name:
        :param account:
        :param phone_number:
        :return:
        """
        WebDriverWait(self.driver,5).until(EC.visibility_of_element_located((By.ID,'username')))
        self.date_driven('../page/data.yml','by2','value2','action2',name)
        self.date_driven('../page/data.yml','by3','value3','action3',account)
        self.date_driven('../page/data.yml','by4','value4','action4',phone_number)
        self.date_driven('../page/data.yml', 'by5', 'value5', 'action5', None)
        pass

    def get_member_info(self):
        """
        成员信息一共有两页
        被添加保存的成员的查询
        首先查看是否在第一页，不在第一页则点击下一页在进行查找
        :return:
        """
        member_list = self.finds_ele(By.XPATH,'//*[@class="member_colRight_memberTable_tr  member_colRight_memberTable_tr_Inactive"]')
        member_info = []
        for i in member_list:
            member_info.append(i.text)
        print(member_info)

        if "A-23" in member_info:
            assert True

        elif "A-23" not in member_info:
            self.find_ele(By.XPATH,"//*[@class='ww_pageNav js_page_container']/div/a[2]").click()
            member_list1 = self.finds_ele(By.XPATH,'//*[@class="member_colRight_memberTable_tr  member_colRight_memberTable_tr_Inactive"]')
            member_info1 = []
            for i in member_list1:
                member_info1.append(i.text)
            print(member_info1)
            if "A-23" in member_info1:
                assert True

        else:
            assert False






