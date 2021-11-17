# -*- coding: utf-8 -*-

# 被测代码，计算器
class Calculator:
    # a: int指定变量类型，->指定范围值类型，起提示作用非强制
    def add(self, a: int, b: int) -> int:
        return a + b

    def sub(self, a, b):
        return a - b

    def mul(self, a, b):
        return a * b

    def div(self, a, b):
        return a / b
