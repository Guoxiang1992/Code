# -*- coding: utf-8 -*- 
# @File : cat_yaml.py
import yaml
with open('./calc.yaml') as f:
    data = yaml.safe_load(f)
    value = data['value']
    my_ids = data['myids']
    value1 = data['value1']
    my_ids1 = data['myids1']
    print(value)
    print(my_ids)
    print(value1)
    print(my_ids1)



