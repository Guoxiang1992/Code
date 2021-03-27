# -- coding: utf-8 --
# @File : testcase.py
from project.lagouPY.Homework.requests_po.base.address_page import Address


class TestAddress:
    def setup(self):
        self.address=Address()
        self.data={
            "userid": "zhangsan4",
            "name": "张三4",
            "alias": "jackzhang4",
            "mobile": "14200000004",
            "department": [1]
        }
    def test_create(self):
        #在创建前先清洗脏数据，确保创建的成员的成员，信息不存在重复
        self.address.delete_member(self.data['userid'])
        r = self.address.create_member(self.data)
        assert r.get('errmsg') == "created"
        #创建成员后进行查看，确保成员信息与创建的成员是一致的
        r = self.address.get_member(self.data['userid'])
        assert r.get("name") == self.data['name']

    def test_get(self):
        self.address.create_member(self.data)
        # 查看成员信息前，先删除，创建，确保查看的成员是新创建的成员
        r = self.address.get_member(self.data['userid'])
        #断言查看的成员名字跟新创建的成员名字一致
        print(r['name'])
        print(self.data['name'])
        assert r.get('name')==self.data['name']
    def test_delete(self):
        self.address.create_member(self.data)
        #删除成员前，先创建，确保删除的成员是我创建的成员
        r = self.address.delete_member(self.data['userid'])
        assert r.get('errmsg')=='deleted'
        #删除之后再次查看，确定删除的成员确实已经查看不到
        r = self.address.get_member(self.data['userid'])
        assert r.get("errcode") == 60111

    def test_update(self):
        self.address.delete_member(self.data['userid'])
        self.address.create_member(self.data)
        #更新信息前，先创建,保证成员一定是新添加的
        new_name='lisi'
        self.data['name']=new_name
        r=self.address.update_member(self.data)
        assert r.get('errmsg')== 'updated'
        #更新信息后再查询,判断名字是否已经更新成功
        r = self.address.get_member(self.data['userid'])
        assert r.get('name')==new_name