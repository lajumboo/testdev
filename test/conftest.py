# -*- coding: utf-8 -*-
import pytest

from mycode.calculator import Calculator


# fixture带参数传递
@pytest.fixture(scope='function', params=['tom', 'jerry'])
def login(request):
    # yield前相当于setup，yield后相当于teardown，yield相当于return
    print("登录")
    username = request.param
    yield username
    print("退出")


@pytest.fixture(scope="class")
def get_calc():
    print("计算开始")
    calc = Calculator()
    yield calc
    print("计算结束")
