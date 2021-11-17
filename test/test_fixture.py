# -*- coding: utf-8 -*-
import pytest


@pytest.fixture(autouse=True)
def login():
    # yield前相当于setup，yield后相当于teardown，yield相当于return
    print("登录")
    yield ["返回值", 123]
    print("退出")


def test_case1(login):
    print(login)
    print("testcase1")


def test_case2():
    print("testcase2")


@pytest.mark.usefixtures("login")
def test_case3():
    print("testcase3")
