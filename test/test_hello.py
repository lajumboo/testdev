# -*- coding: utf-8 -*-
import importlib


def test_hello():
    c = importlib.import_module("hello")
    getattr(c, "b")()
