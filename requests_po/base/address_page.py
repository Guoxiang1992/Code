# -- coding: utf-8 --
# @File : address_page.py
from project.lagouPY.Homework.requests_po.base.base import Base


class Address(Base):
    def create_member(self,data):
        url='https://qyapi.weixin.qq.com/cgi-bin/user/create'
        method='post'
        r = self.request_send(url,method,json=data)
        return r.json()
    def get_member(self,userid):
        url='https://qyapi.weixin.qq.com/cgi-bin/user/get'
        method='get'
        data={
            "userid": userid
        }
        r = self.request_send(url,method,params=data)
        return r.json()
    def update_member(self,data):
        url = 'https://qyapi.weixin.qq.com/cgi-bin/user/update'
        method = 'post'
        r = self.request_send(url, method, json=data)
        return r.json()
    def delete_member(self, userid):
        url = 'https://qyapi.weixin.qq.com/cgi-bin/user/delete'
        method = 'get'
        data = {
            "userid": userid
        }
        r = self.request_send(url, method, params=data)
        return r.json()