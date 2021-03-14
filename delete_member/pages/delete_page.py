# -- coding: utf-8 --
# @File : delete_page.py
import time

import allure

from project.lagouPY.Homework.delete_member.pages.basepage import BasePage

class DeleteMember(BasePage):
    def goto_delete(self):
        with allure.step('查看即将删除成员的同名人数'):
            eles = self.datas_driven('../pages/data.yml','delete_members')

        if len(eles) > 0:
            for ele in eles:
                self.clickable_wait(5,'id','com.tencent.wework:id/dtv')
                ele.click()
                with allure.step('点击选项'):
                    self.data_driven('../pages/data.yml','delete_selection')
                with allure.step('点击编辑成员'):
                    self.data_driven('../pages/data.yml','member_edit')
                with allure.step('点击删除成员'):
                    self.data_driven('../pages/data.yml','member_delete')
                self.visibility_wait(5,'id','com.tencent.wework:id/bpc')
                with allure.step('点击确定删除'):
                    self.data_driven('../pages/data.yml','delete_confirm')
                # print(self.driver.page_source
        else:
            with allure.step('该成员无搜索结果'):
                ele_text = self.data_driven('../pages/data.yml','assert_result')
            assert ele_text == '无搜索结果'

