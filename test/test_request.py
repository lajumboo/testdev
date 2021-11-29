# -*- coding: utf-8 -*-
import requests


def test_demo():
    r = requests.get("https://httpbin.ceshiren.com/get")
    print(r.text)
    assert r.status_code == 200


def test_query():
    payload = {
        "name": "zhang",
        "age": 18
    }
    r = requests.get("https://httpbin.ceshiren.com/get", params=payload)
    print(r.text)
    assert r.status_code == 200


def test_post_form():
    payload = {
        "name": "zhang",
        "age": 18
    }
    r = requests.post("https://httpbin.ceshiren.com/post", data=payload)
    print(r.text)
    assert r.status_code == 200


def test_post_json():
    payload = {
        "name": "zhang",
        "age": 18
    }
    r = requests.post("https://httpbin.ceshiren.com/post", json=payload)
    print(r.text)
    print(r.json()['data'])
    assert r.status_code == 200
