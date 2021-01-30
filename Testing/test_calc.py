# -*- coding: utf-8 -*- 
# @File : test_calc.py
import pytest
import yaml
from Code.lagouPY.pytest.testdemo.Testing.python_code.calc_case import Calc

with open('./data/calc.yaml') as f: #打开yaml文件，把里面的内容赋给对应变量，方便后续的参数化的调用
    data = yaml.safe_load(f)
    add_value = data['value']
    add_ids = data['myids']
    div_value = data['value1']
    div_ids = data['myids1']

class TestCalc: #定义测试算法的类
    def setup_class(self): #在测试类所有测试方法执行之前输出“Start the test”，同时实例化Calc，这样类下面的所有方法就可以直接调用Calc里的方法了
        print('Start the test')
        self.calc = Calc()
    def teardown_class(self): #在测试类所有测试方法执行之后输出“End of the test”
        print('End of the test')
    def setup(self): #在测试类下面的所有测试方法执行前，都会输出'Start the calculation'
        print('Start the calculation')
    def teardown(self): #在测试类下面的所有测试方法执行之后，都会输出'End the calculation'
        print('End the calculation')

    @pytest.mark.parametrize('a,b,expect', add_value, ids=add_ids) #对测试用例进行参数化
    def test_add(self,a,b,expect):
        result = self.calc.add(a,b)
        if isinstance(result,float):#判断result的数据类型，如果是浮点数，result强制保留小数点后两位
            result = round(result,2)
        assert result == expect #断言:判断result 和 expect是否相等，相等则测试通过，不相等则失败

    @pytest.mark.parametrize('a,b,expect', div_value, ids=div_ids)
    def test_div(self,a,b,expect):
        result = self.calc.div(a,b)
        if isinstance(result,float):
            result = round(result,2)
        assert result == expect




