# -*- coding: utf-8 -*-
from web.page.main_page import MainPage


class TestWecom:
    def setup(self):
        self.main = MainPage()

    def test_add_member(self):
        assert self.main.goto_add_member().add_member()
