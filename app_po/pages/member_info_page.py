# -- coding: utf-8 --
# @File : member_info_page.py
from selenium.webdriver.common.by import By

from project.lagouPY.Homework.app_po.pages.basepage import BasePage
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class MemberInfo(BasePage):
    def add_member_info(self):
        self.data_driven('../pages/data.yml','by3','locator3','action3','王五1')
        self.data_driven('../pages/data.yml','by4','locator4','action4','wangwu1')
        self.data_driven('../pages/data.yml','by5','locator5','action5','12012345679')
        self.data_driven('../pages/data.yml','by6','locator6','action6')

        WebDriverWait(self.driver,5).until(EC.visibility_of_element_located((By.ID,"com.tencent.wework:id/ipb")))
        print(self.driver.page_source)
        ele = self.data_driven('../pages/data.yml','by7','locator7','action7')
        assert ele == '添加成功'

