# -*- coding: utf-8 -*-
import scrapy
import re,datetime,hashlib
from scrapy.http import Request
from ArticleSpider.items import JobBoleArticleItem
from urllib import parse
class JobboleSpider(scrapy.Spider):
    name = 'jobbole'
    allowed_domains = ['blog.jobbole.com']
    start_urls = ['http://blog.jobbole.com/all-posts/']

    def parse(self, response):
        """
        1.获取文章列表页中的文章url并交给scrapy下载后并进行解析
        2.获取下一页的url并交给scrapy进行下载，下载完成后交给parse
        :param response:
        :return:
        """
        # 解析列表页中的所有文章url并交给scrapy下载后并进行解析
        post_nodes = response.xpath('//div[@class="grid-8"]/div[@class="post floated-thumb"]/div[1]/a')

        for post_node in post_nodes:
            #文章详情页url
            post_url = post_node.xpath('@href').extract_first('')
            img_url = post_node.xpath('img/@src').extract_first('')
            yield Request(url=parse.urljoin(response.url,post_url),meta={"front_image_url":img_url},callback=self.parse_detail)
            print(post_url)

        #提取下一页，并交给scrapy下载
        next_url = response.xpath('//a[@class="next page-numbers"]/@href').extract_first('')
        if next_url:
            yield Request(url=parse.urljoin(response.url,next_url),callback=self.parse)

    def parse_detail(self,response):
        """
        1.提取文章的具体字段
        :param response:
        :return:
        """
        #创建item对象
        article_item = JobBoleArticleItem()
        #文章封面图
        front_image_url = response.meta.get("front_image_url","")
        #文章标题
        #'/html/body/div[1]/div[3]/div[1]/div[@class=entry-header]/h1'
        #'/html/body/div[1]/div[3]/div[1]/div[1]/h1/text()'
        title = response.xpath('/html/body/div[1]/div[3]/div[1]/div[@class="entry-header"]/h1').extract()[0]
        #创建日期
        create_date = response.xpath('/html/body/div[@id="wrapper"]/div[@class="grid-8"]/div[1]/div[2]/p/text()').extract()[0].strip().replace(' ·', '')
        try:
            create_date = datetime.datetime.strftime(create_date,"%Y/%m/%d").date()
        except Exception as e:
            create_date = datetime.datetime.now().date()
        #点赞数
        praise_num = response.xpath('//span[contains(@class,"vote-post-up")]/h10/text()').extract()[0]
        #评论数
        # comment_num = response.xpath('//a[@href="#article-comment"]/span/text()').extract()[0]
        try:
            comment_num = re.match('.*(\d+).*',
                                   response.xpath('//a[@href="#article-comment"]/span/text()').extract()[0]).group(1)
        except:
            comment_num = 0

        # 收藏数
        try:
            match_num = re.match('.*(\d+).*',
                                 response.xpath('//span[contains(@class,"bookmark-btn")]/text()').extract()[0]).group(1)
        except:
            match_num = 0
        #标签
        tag_list = response.xpath('//p[@class="entry-meta-hide-on-mobile"]/a/text()').extract()[0]
        tags = ",".join(tag_list)
        fav_nums = response.xpath('//div[@class="post-adds"]/span[2]/text()').extract_first().strip().replace("收藏","")
        if not fav_nums:
            fav_nums = 0

        url = response.url
        url_object_id = hashlib.md5(url.encode('utf-8')).hexdigest()
        #内容
        content = response.xpath('//div[@class="entry"]').extract()[0]

        #给item对象填充值
        article_item['title'] = title
        article_item['front_image_url'] = [front_image_url]
        article_item['front_image_path'] = "path"
        article_item['create_date'] = str(create_date)
        article_item['praise_nums'] = int(praise_num)
        article_item['comment_nums'] = int(comment_num)
        article_item['fav_nums'] = int(fav_nums)
        article_item['url'] = url
        article_item['url_object_id'] = url_object_id
        article_item['tag_list'] = tag_list
        article_item['tags'] = tags
        article_item['content'] = content


        #把item传给pipelines
        yield article_item