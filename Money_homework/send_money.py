# -*- coding: utf-8 -*- 
# @File : send_money.py
import money
salary = int(input('salary:'))
def sendmonney():
    print(f"我这次发了{salary}元")
    money.saved_money = money.saved_money + salary
    # return money.saved_money
#
# if __name__ == '__main__':
#     print(f"这次工资发了{salary}元")
#
#     print(f"发工资之后我的小金库居然有{}元，买买买买买。。")

