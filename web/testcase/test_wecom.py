# -*- coding: utf-8 -*-

from web.page.main_page import MainPage


class TestWecom:
    # 调用MainPage，初始化driver
    def setup(self):
        self.main = MainPage()

    def test_add_member(self):
        username = "张三九"
        account = "zhangsanjiu"
        phone = "18633333339"

        add_member = self.main.goto_add_member()
        add_member.add_member(username, account, phone)
        assert username in add_member.get_member()
