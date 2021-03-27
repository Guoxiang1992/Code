# -- coding: utf-8 --
# @File : base.py
import requests


class Base:
    def __init__(self):
        #例用requests里面的session方法，把获取的token放入到session中
        self.session=requests.session()
        self.session.params={'access_token':self.get_token()}
    #定义关闭session的方法，用于接口测试结束后的清理
    def session_close(self):
        self.session.close()

    def get_token(self):
        self.url = 'https://qyapi.weixin.qq.com/cgi-bin/gettoken'
        self.params = {
            'corpid': 'ww87149f52c3a22b83',
            'corpsecret': 'y_VskGvKJPHdCpgKk0Dcpy9bbGsqjWeZC5Ch4x97lUc'
        }
        r = requests.get(self.url, params=self.params)
        token = r.json()['access_token']
        return token
    #定义一个通用的requests方面
    def request_send(self,url,method,*args,**kwargs):
        r = self.session.request(url=url, method=method,*args,**kwargs)
        return r
