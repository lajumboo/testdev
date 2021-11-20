# -*- coding: utf-8 -*-
import pytest

from web.page.main_page import MainPage


class TestWecom:
    # 调用mainpage，初始化driver
    def setup(self):
        self.main = MainPage()

    def test_add_member(self):
        username = "张三五"
        account = "zhangsanwu"
        phone = "18633333335"

        add_member = self.main.goto_add_member()
        add_member.add_member(username, account, phone)
        assert username in add_member.get_member()
