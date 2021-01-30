# -*- coding: utf-8 -*- 
# @File : test_calculator.py
import pytest
import allure

@allure.feature('测试计算器算法')
class TestCalc: #定义测试算法的类
    @allure.story('加法算法测试')
    @pytest.mark.run(order=1) #控制加法测试用例顺序为第一个
    def test_add(self,get_calc,get_add_data): #定义测试加法案例，实例化加法
        result = get_calc.add(get_add_data[0],get_add_data[1])
        if isinstance(result,float):#判断result的数据类型，如果是浮点数，result强制保留小数点后两位
            result = round(result,2)
        assert result == get_add_data[2] #断言:判断是否相等，相等则测试通过，不相等则失败

    @allure.story('除法算法测试')
    @pytest.mark.run(order=4) #控制加法测试用例顺序为第四个
    def test_div(self,get_calc,get_div_data): #定义测试除法案例，实例化除法
        result = get_calc.div(get_div_data[0],get_div_data[1])
        if isinstance(result,float):#判断result的数据类型，如果是浮点数，result强制保留小数点后两位
            result = round(result,2)
        assert result == get_div_data[2] #断言:判断是否相等，相等则测试通过，不相等则失败

    @allure.story('减法算法测试')
    @pytest.mark.run(order=2) #控制加法测试用例顺序为第二个
    def test_sub(self,get_calc,get_sub_data): #定义测试减法案例，实例化减法法
        result = get_calc.sub(get_sub_data[0],get_sub_data[1])
        if isinstance(result,float):#判断result的数据类型，如果是浮点数，result强制保留小数点后两位
            result = round(result,2)
        assert result == get_sub_data[2] #断言:判断是否相等，相等则测试通过，不相等则失败

    @allure.story('乘法算法测试')
    @pytest.mark.run(order=3) #控制加法测试用例顺序为第三个
    def test_mul(self,get_calc,get_mul_data): #定义测试乘法案例，实例化乘法
        result = get_calc.mul(get_mul_data[0],get_mul_data[1])
        if isinstance(result,float):#判断result的数据类型，如果是浮点数，result强制保留小数点后两位
            result = round(result,2)
        assert result == get_mul_data[2] #断言:判断是否相等，相等则测试通过，不相等则失败



