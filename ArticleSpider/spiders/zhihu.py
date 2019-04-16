# -*- coding: utf-8 -*-
import scrapy,os,re,pickle,time
from scrapy.http import Request
from selenium import webdriver
from ArticleSpider.items import CustnomItemLoader
from ArticleSpider.items import ZhihuQuestionItem,ZhihuAnswerItem


class ZhihuSpider(scrapy.Spider):
    name = 'zhihu'
    allowed_domains = ['zhihu.com']
    start_urls = ['https://www.zhihu.com/question/30878980/answer/508972915']

    headers = {
        "HOST": "www.zhihu.com",
        "Referer": "https://www.zhizhu.com",
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36"
    }
    custom_settings = {
        "COOKIES_ENABLED": True
    }
    #获取cookie.zhihu
    base_dir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
    cookies = os.path.join(base_dir, "cookies/zhihu")
    for root, dirs, files in os.walk(cookies):
        file_path = os.path.join(root, files[0])

    cookies_file = open(file_path, 'rb')
    cookies_data = pickle.load(cookies_file)
    cookies_file.close()

    def parse(self, response):
        print(response.text)
        item_loader = CustnomItemLoader(item=ZhihuQuestionItem(),response=response)
        item_loader.add_xpath('zhihu_id',)
        item_loader.add_xpath()
        item_loader.add_xpath()
        item_loader.add_xpath('title','//h1[@class="QuestionHeader-title"]')

        item_loader.add_xpath()
        item_loader.add_xpath()
        item_loader.add_xpath()
        item_loader.add_xpath()
        item_loader.add_xpath()
        item_loader.add_xpath()
        item_loader.add_xpath()
        item_loader.add_xpath()
        item_loader.add_xpath()

    def parse_request(self,response):
        pass

    def parse_answer(self,response):
        pass

    def start_requests(self):

        return [Request('https://www.zhihu.com/signup?next=%2F',headers=self.headers,encoding="utf-8",
                        cookies=self.cookies_data,dont_filter=True,callback=self.login)]

    def login(self,response):
        """
        模拟登录
        :param response: 
        :return: 
        """
        project_dir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
        chromedriver_dir = os.path.join(project_dir, "tools\\chromedriver.exe")
        browser = webdriver.Chrome(
            executable_path=chromedriver_dir)
        browser.get("https://www.zhihu.com/signup?next=%2F")

        # 模拟登录知乎,选择登录选项
        info = response.xpath('//*[@id="root"]/div/main/div/div/div/div[2]/div[2]/span/text()')
        browser.find_element_by_xpath('//*[@id="root"]/div/main/div/div/div/div[2]/div[2]/span').click()
        # 输入账号//*div[@class='SignFlow-accountInput Input-wrapper']/input
        browser.find_element_by_xpath(
            '//*[@id="root"]/div/main/div/div/div/div[2]/div[1]/form/div[1]/div[2]/div[1]/input').send_keys(
            "656521736@qq.com")
        # 输入密码
        browser.find_element_by_xpath(
            '//*[@id="root"]/div/main/div/div/div/div[2]/div[1]/form/div[2]/div/div[1]/input').send_keys("1qaz2wsx3edc")
        # 模拟登录知乎,点击登录按钮
         #//*[@id="root"]/div/main/div/div/div/div[2]/div[1]/form/button
        browser.find_element_by_xpath('//*[@id="root"]/div/main/div/div/div/div[2]/div[1]/form/button').click()

        time.sleep(10)
        Cookies = browser.get_cookies()
        print(Cookies)
        cookie_dict = {}
        for cookie in Cookies:
            cookie_dict[cookie['name']] = cookie['value']
         # 写入文件
        zhihu_cookie_dir = os.path.join(project_dir, "cookies\\zhihu\\")
        f = open(zhihu_cookie_dir + 'cookie' + '.zhihu', "wb")
        pickle.dump(cookie_dict, f)
        f.close()
        browser.close()
        return Request(url="https://www.zhihu.com/",headers=self.headers,cookies=cookie_dict,meta={'cookie_dict':cookie_dict},callback=self.check_login)

    def check_login(self,response):
        response_text = response.text
        result = re.search('首页 - 知乎', response_text)
        if result:
            print("登录了")
            return Request(url=self.start_urls[0], headers=self.headers,
                                dont_filter=True)
        else:
                print("没登录")

        #return Request(url=self.start_urls[0],headers=self.headers,callback=self.parse,cookies=response.meta['cookie_dict'],dont_filter=True)
        # except:
        #     print("没有登录")












