# -- coding: utf-8 --
# @File : test_enterprise_wechat.py
import shelve
import time

from selenium import webdriver

class TestEnterpriseWechat:
    def setup(self):
        self.driver=webdriver.Chrome() #定义测试时使用chrome浏览器
        self.driver.maximize_window() #窗口最大化
        self.driver.implicitly_wait(5) #隐式等待5秒
    def teardown(self):
        self.driver.quit() #测试结束关闭浏览器
    def test_login(self):
        #打开企业微信扫描登录界面
        self.driver.get('https://work.weixin.qq.com/wework_admin/frame')
        #获取提前通过shelve数据库存储的cookies
        my_dat=shelve.open('./mydats/qiyeweixin')
        cookies = my_dat['cookie']
        #遍历cookies
        for cookie in cookies:
            if 'expriy' in cookie.keys():  #怕exprity的value是浮点数，而且它也不影响登录，所以可以删除
                del cookie['expriy']  #也可以用cookie.pop('exprity')去删除
            self.driver.add_cookie(cookie)
        #再次打开企业微信登录界面，就会因为已经有了cookie，所以就会自动登录企业微信
        self.driver.get('https://work.weixin.qq.com/wework_admin/frame')
        time.sleep(3) #给个固定等待时间，用来加载页面
        #对导入通讯录按钮的元素进行定位，并点击
        self.driver.find_element_by_xpath('//*[@id="_hmt_click"]/div[1]/div[4]/div[2]/a[2]/div/span[1]').click()
        time.sleep(3)
        #对文件上传按钮的元素进行定位，并填写你上传文件的路径
        self.driver.find_element_by_id('js_upload_file_input').send_keys('C:\\Users\\CVL\\Desktop\\mail list.xlsx')
        #断言上传文件的文本属性是否和上传的文件是一样的
        assert 'mail list.xlsx' == self.driver.find_element_by_id('upload_file_name').text
        time.sleep(5)