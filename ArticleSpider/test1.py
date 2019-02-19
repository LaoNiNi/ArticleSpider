#! /usr/bin/env python
# -*- coding:utf-8 -*-
#Author:Bigni

import re

info = '1000 收藏'
# try:
#     ret = re.match('.*(\d+).*',info).group(1)
# except:
#     ret = 0
#
# print(ret)


info2 = {"aa":3,"bb":4}
# print(info2.get("aa",""))


aa = '  收藏'
print(aa.strip().replace("收藏",""))