# -*- coding: utf-8 -*-
import pytest
import yaml


class TestDate:
    @pytest.mark.parametrize("a,b", [(10, 20), (20, 30), (30, 40)])
    def test_data(self, a, b):
        print(a + b)

    @pytest.mark.parametrize(("a", "b"), yaml.safe_load(open("./data.yaml")))
    def test_data1(self, a, b):
        print(a - b)
