# -*- coding: utf-8 -*-

import time


def record_time(func):
    def wrapper(*kwargs):
        print('function start at {}'.format(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())))
        total = func(*kwargs)
        print('function end at {}'.format(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())))
        return total

    return wrapper


# 注意这一行，我们把record_time这个函数装饰到sum函数上。
@record_time
def sum1(*kwargs):
    total = 0

    for ele in kwargs:
        total = total + ele

    time.sleep(2)

    return total


def test_sum1():
    print(sum1(1, 2, 3, 4))
