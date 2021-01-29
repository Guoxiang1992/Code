# -*- coding: utf-8 -*- 
# @File : test_calc.py
import pytest
import yaml
from day1.lagouPY.pytest.report2.datas.calc_case import Calc

with open('./calc.yaml') as f:
    data = yaml.safe_load(f)
    add_value = data['value']
    add_ids = data['myids']
    div_value = data['value1']
    div_ids = data['myids1']
class TestCalc:
    def setup_class(self):
        print('Start the test')
        self.calc = Calc()
    def teardown_class(self):
        print('End of the test')
    def setup(self):
        print('Start the calculation')
    def teardown(self):
        print('End the calculation')

    @pytest.mark.parametrize('a,b,expect', add_value, ids=add_ids)
    def test_add(self,a,b,expect):
        result = self.calc.add(a,b)
        if isinstance(result,float):
            result = round(result,2)
        assert result == expect

    @pytest.mark.parametrize('a,b,expect', div_value, ids=div_ids)
    def test_div(self,a,b,expect):
        result = self.calc.div(a,b)
        if isinstance(result,float):
            result = round(result,2)
        assert result == expect




