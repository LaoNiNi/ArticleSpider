#! /usr/bin/env python
# -*- coding:utf-8 -*-
#Author:Bigni

#pycharm没有运行scrapy的方法，需要借助scrapy的模块来模拟脚本启动命令
from scrapy.cmdline import execute


import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
execute(["scrapy","crawl","jobbole"])

