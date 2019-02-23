#! /usr/bin/env python
# -*- coding:utf-8 -*-
#Author:Bigni
import os
from selenium import webdriver

from scrapy.selector import Selector


project_dir = os.path.abspath(os.path.dirname(__file__))

chromedriver_dir = os.path.join(project_dir,"chromedriver.exe")
browser = webdriver.Chrome(executable_path=chromedriver_dir)

# browser.get("https://www.zhihu.com/signup?next=%2F")
#
# #模拟登录知乎,点击登录按钮
# browser.find_element_by_xpath('//*[@id="root"]/div/main/div/div/div/div[2]/div[2]/span').click()
# #输入账号//*div[@class='SignFlow-accountInput Input-wrapper']/input
# browser.find_element_by_xpath("//*[@id='root']/div/main/div/div/div/div[2]/div[1]/form/div[1]/div[2]/div[1]/input").send_keys("656521736@qq.com")
# #输入密码
# browser.find_element_by_xpath("//*[@id='root']/div/main/div/div/div/div[2]/div[1]/form/div[2]/div/div[1]/input").send_keys("1qaz2wsx3edc")
#
# #模拟登录知乎,点击登录按钮
# browser.find_element_by_xpath("//*[@id='root']/div/main/div/div/div/div[2]/div[1]/form/button").click()

browser.get("https://www.zhihu.com/signin")

# 模拟登录知乎,点击登录按钮
# browser.find_element_by_xpath('//*[@id="root"]/div/main/div/div/div/div[2]/div[2]/span').click()
# 输入账号//*div[@class='SignFlow-accountInput Input-wrapper']/input
browser.find_element_by_xpath(
    "//*[@id='root']/div/main/div/div/div/div[2]/div[1]/form/div[1]/div[2]/div[1]/input").send_keys(
    "656521736@qq.com")
# 输入密码
browser.find_element_by_xpath(
    "//*[@id='root']/div/main/div/div/div/div[2]/div[1]/form/div[2]/div/div[1]/input").send_keys("1qaz2wsx3edc")
# 模拟登录知乎,点击登录按钮
# //*[@id="root"]/div/main/div/div/div/div[2]/div[1]/form/button
browser.find_element_by_xpath('//*[@id="root"]/div/main/div/div/div/div[2]/div[1]/form/button').click()


#selenium也有自带的css、xpath选择器，但运行效率没scrapy的Selector快。
t_selector = Selector(text=browser.page_source)

print(browser.page_source)