# -*- coding: utf-8 -*-
import pytest

from mycode.calculator import Calculator


@pytest.fixture(scope='function')
def login():
    # yield前相当于setup，yield后相当于teardown，yield相当于return
    print("登录")
    yield ["返回值", 123]
    print("退出")


@pytest.fixture(scope="class")
def get_calc():
    print("计算开始")
    calc = Calculator()
    yield calc
    print("计算结束")
