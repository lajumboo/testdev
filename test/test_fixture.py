# -*- coding: utf-8 -*-
import pytest


def test_case1(login):
    print(login)
    print("testcase1")


def test_case2():
    print("testcase2")


@pytest.mark.usefixtures("login")
def test_case3():
    print("testcase3")
