# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ArticlespiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

#文章详情页需要存储的字段
class JobBoleArticleItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    front_image_url = scrapy.Field()
    front_image_path = scrapy.Field()
    create_date = scrapy.Field()
    praise_nums = scrapy.Field()
    comment_nums = scrapy.Field()
    fav_nums = scrapy.Field()
    url = scrapy.Field()
    url_object_id = scrapy.Field()
    tag_list = scrapy.Field()
    tags = scrapy.Field()
    content = scrapy.Field()
