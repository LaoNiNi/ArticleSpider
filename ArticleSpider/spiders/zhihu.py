# -*- coding: utf-8 -*-
import scrapy,os


class ZhihuSpider(scrapy.Spider):
    name = 'zhihu'
    allowed_domains = ['zhihu.com']
    start_urls = ['http://zhihu.com/']

    headers = {
        "HOST": "www.zhihu.com",
        "Referer": "https://www.zhizhu.com",
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.109 Safari/537.36"
    }

    def parse(self, response):
        pass

    def parse_request(self,response):
        pass

    def parse_answer(self,response):
        pass

    def start_requests(self):
        return [scrapy.Request('https://www.zhihu.com/signin',headers=self.headers,callback=self.login]

    def login(self,response):
        from selenium import webdriver
        from scrapy.selector import Selector

        project_dir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))

        chromedriver_dir = os.path.join(project_dir, "chromedriver.exe")
        browser = webdriver.Chrome(executable_path=chromedriver_dir)

        browser.get("https://www.zhihu.com/signin")

        # 模拟登录知乎,点击登录按钮
        #browser.find_element_by_xpath('//*[@id="root"]/div/main/div/div/div/div[2]/div[2]/span').click()
        # 输入账号//*div[@class='SignFlow-accountInput Input-wrapper']/input
        browser.find_element_by_xpath(
            "//*[@id='root']/div/main/div/div/div/div[2]/div[1]/form/div[1]/div[2]/div[1]/input").send_keys(
            "656521736@qq.com")
        # 输入密码
        browser.find_element_by_xpath(
            "//*[@id='root']/div/main/div/div/div/div[2]/div[1]/form/div[2]/div/div[1]/input").send_keys("1qaz2wsx3edc")
        # 模拟登录知乎,点击登录按钮
        browser.find_element_by_xpath("//*[@id='root']/div/main/div/div/div/div[2]/div[1]/form/button").click()
        import time
        time.sleep(10)
        Cookies = browser.get_cookies()
        print(Cookies)
        cookie_dict = {}
        import pickle
        for cookie in Cookies:
            #写入文件
            f = open("")








