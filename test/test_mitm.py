# -*- coding: utf-8 -*-
import json

from mitmproxy import http


# 实现maplocal
# def request(flow: http.HTTPFlow) -> None:
#     if "quote.json" in flow.request.pretty_url:
#         # 打开保存在本地的数据文件
#         with open("./quote.json", encoding='utf-8') as f:
#             # 创造一个 response
#             flow.response = http.Response.make(
#                 200,  # (optional) status code
#                 # 读取文件中数据作为返回内容
#                 f.read(),
#                 # 指定返回数据的类型
#                 {"Content-Type": "application/json"}  # (optional) headers
#             )

# 实现rewrite
def response(flow: http.HTTPFlow):
    # 加上过滤条件
    if "quote.json" in flow.request.pretty_url and "extend" in flow.request.pretty_url:
        # 把响应数据转化成json对象，保存到data中
        data = json.loads(flow.response.content)
        # 修改股票的名称
        second_name = data['data']['items'][1]['quote']['name']
        data['data']['items'][0]['quote']['name'] = "测试股票"
        data['data']['items'][1]['quote']['name'] = second_name * 2
        data['data']['items'][2]['quote']['current'] = 10.0
        # 把修改后的内容赋值给 response 原始数据格式
        flow.response.text = json.dumps(data)
