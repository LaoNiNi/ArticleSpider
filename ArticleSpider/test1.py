#! /usr/bin/env python
# -*- coding:utf-8 -*-
#Author:Bigni

# import re
#
# info = '1000 收藏'
# # try:
# #     ret = re.match('.*(\d+).*',info).group(1)
# # except:
# #     ret = 0
# #
# # print(ret)
#
#
# info2 = {"aa":3,"bb":4}
# # print(info2.get("aa",""))
#
#
# aa = '  收藏'
# print(aa.strip().replace("收藏",""))

# D:\software\pycharm\helpers\pydev\_pydevd_bundle\pydevd_comm.py
# 375hang

import re
a = "asdf"
# print(re.search("([0-9]*)([a-z]*)([0-9]*)",a).group())   #123abc456,返回整体
# print(re.search("([0-9]*)([a-z]*)([0-9]*)",a).group(1))   #123
# print(re.search("([0-9]*)([a-z]*)([0-9]*)",a).group(2))   #abc
# print(re.search("([0-9]*)([a-z]*)([0-9]*)",a).group(4))   #456
###group(1) 列出第一个括号匹配部分，group(2) 列出第二个括号匹配部分，group(3) 列出第三个括号匹配部分。###

# response_text="234324ffafsdaf"
# result = re.search('首页 - 知乎', response_text)
# print(result)

# info ="\xe9\xa6\x96\xe9\xa1\xb5 - \xe7\x9f\xa5\xe4\xb9\x8e"
# byte_s = bytes(info,encoding="utf8")
# print(type(info),info,str(byte_s,encoding="utf8"))
# #b'<!doctype html>\n<html lang="zh" data-hairline="true" data-theme="light"><head><meta charSet="utf-8"/><title data-react-helmet="true">\xe9\xa6\x96\xe9\xa1\xb5 - \xe7\x9f\xa5\xe4\xb9\x8e</title><meta name="viewport" content="width=device-width,initial-scale=1,maximum-scale=1"/><meta name="renderer" content="webkit"/><meta name="force-rendering" content="webkit"/><meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1"/><meta name="google-site-verification" content="FTeR0c8arOPKh8c5DYh_9uu98_zJbaWw53J-Sch9MTg"/><meta name="description" property="og:description" content="\xe6\x9c\x89\xe9\x97\xae\xe9\xa2\x98\xef\xbc\x8c\xe4\xb8\x8a\xe7\x9f\xa5\xe4\xb9\x8e\xe3\x80\x82\xe7\x9f\xa5\xe4\xb9\x8e\xef\xbc\x8c\xe5\x8f\xaf\xe4\xbf\xa1\xe8\xb5\x96\xe7\x9a\x84\xe9\x97\xae\xe7\xad\x94\xe7\xa4\xbe\xe5\x8c\xba\xef\xbc\x8c\xe4\xbb\xa5\xe8\xae\xa9\xe6\xaf\x8f\xe4\xb8\xaa\xe4\xba\xba\xe9\xab\x98\xe6\x95\x88\xe8\x8e\xb7\xe5\xbe\x97\xe5\x8f\xaf\xe4\xbf\xa1\xe8\xb5\x96\xe7\x9a\x84\xe8\xa7\xa3\xe...
#
#
# str = '\xe5\xae\x9d\xe9\xb8\xa1\xe5\xb8\x82'
# print(str.encode('utf-8'))
# https://www.zhihu.com/api/v3/feed/topstory/recommend?session_token=030c28d07a07224356853d959cb4a2b5&desktop=true&page_number=8&limit=6&action=pull&before_id=41

for i in range(2,10):
    print(i)


