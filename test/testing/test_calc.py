# -*- coding: utf-8 -*-
import pytest
import yaml

from mycode.calculator import Calculator


def get_datas():
    with open("./datas/calc.yaml") as f:
        datas = yaml.safe_load(f)
    add_datas = datas['add']['datas']
    sub_datas = datas['sub']['datas']
    mul_datas = datas['mul']['datas']
    div_datas = datas['div']['datas']
    return [add_datas, sub_datas, mul_datas, div_datas]


class TestCalc:
    def setup_class(self):
        print("计算开始")
        self.calc = Calculator()

    def teardown_class(self):
        print("计算结束")

    @pytest.mark.parametrize(('a', 'b', 'expect'), get_datas()[0])
    def test_add(self, a, b, expect):
        result = self.calc.add(a, b)
        assert round(result, 2) == expect

    @pytest.mark.parametrize(('a', 'b', 'expect'), get_datas()[1])
    def test_sub(self, a, b, expect):
        result = self.calc.sub(a, b)
        assert result == expect

    @pytest.mark.parametrize(('a', 'b', 'expect'), get_datas()[2])
    def test_mul(self, a, b, expect):
        result = self.calc.mul(a, b)
        assert result == expect

    @pytest.mark.parametrize(('a', 'b', 'expect'), get_datas()[3])
    def test_div(self, a, b, expect):
        try:
            result = self.calc.div(a, b)
            assert round(result, 2) == expect
        except ZeroDivisionError as e:
            print(e)

    # def test_div_zero(self):
    #     with pytest.raises(ZeroDivisionError):
    #         self.calc.div(1, 0)