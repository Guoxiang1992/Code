# -*- coding: utf-8 -*- 
# @File : conftest.py
import pytest
import yaml
from Code.lagouPY.Homework.Testing_Calculator.test_case.calc_case import Calc

#在conftest下创建 fixture 方法
@pytest.fixture(scope="module") #将fixture作用域设置为模块级别
def get_calc():
    print("开始计算") #实现执行测试用例前打印【开始计算】
    calc = Calc()
    yield calc
    print('结束计算') #实现执行测试用例后打印【结束计算】

#加载yaml文件，对里面的数据分别赋值给对变量，给后续测试方法想要参数化
with open('calc.yaml') as f:
    datas = yaml.safe_load(f)
    add_date = datas['add_value']
    add_ids = datas['add_myids']
    sub_date = datas['sub_value']
    sub_ids = datas['sub_myids']
    mul_date = datas['mul_value']
    mul_ids = datas['mul_myids']
    div_date = datas['div_value']
    div_ids = datas['div_myids']

@pytest.fixture(params=add_date,ids=add_ids)#获取加法数据，并返回
def get_add_data(request):
    data = request.param
    return data

@pytest.fixture(params=sub_date,ids=sub_ids)#获取减法数据，并返回
def get_sub_data(request):
    data = request.param
    return data

@pytest.fixture(params=mul_date,ids=mul_ids)#获取乘法数据，并返回
def get_mul_data(request):
    data = request.param
    return data

@pytest.fixture(params=div_date,ids=div_ids)#获取除法数据，并返回
def get_div_data(request):
    data = request.param
    return data




