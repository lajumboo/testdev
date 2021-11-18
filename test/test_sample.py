# content of test_sample.py
import pytest


def inc(x):
    return x + 1


def test_answer():
    assert inc(3) == 5

# 入口函数
if __name__ == '__main__':
    pytest.main(['-v', '-s', 'test_sample.py'])
