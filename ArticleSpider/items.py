# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy,re,datetime,hashlib
#使用MapCompose可以拿到返回结果后执行某些函数,TakeFirst取数组第一个值
from scrapy.loader.processors import MapCompose,TakeFirst
from scrapy.loader import ItemLoader
import scrapy.item
class CustnomItemLoader(ItemLoader):
    #自定义ItemLoader
    default_output_processor = TakeFirst()



class ArticlespiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


def add_jobbole(value):
    return value

def data_convert(value):
    try:
        create_date = datetime.datetime.strftime(value, "%Y/%m/%d").date()
    except Exception as e:
        create_date = datetime.datetime.now().date()
    return create_date

def comment_num(value):
    try:
        comment_num = re.match('.*(\d+).*',value).group(1)
    except:
        comment_num = 0
    return comment_num

def fav_num(value):
    fav_nums = value.strip().replace("收藏", "")
    if not fav_nums:
        fav_nums = 0
    return fav_nums

def md5_has(value):
    value = hashlib.md5(value.encode('utf-8')).hexdigest()
    return value

def str_convert(value):
    return str(value)


#文章详情页需要存储的字段
class JobBoleArticleItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field(
        #返回结果预处理
        input_processor = MapCompose(add_jobbole)
    )
    front_image_url = scrapy.Field()
    front_image_path = scrapy.Field()
    create_date = scrapy.Field(
        input_processor = MapCompose(data_convert,str_convert)
    )
    praise_nums = scrapy.Field()
    comment_nums = scrapy.Field(
        input_processor=MapCompose(comment_num)
    )
    fav_nums = scrapy.Field(
        input_processor=MapCompose(fav_num)
    )
    url = scrapy.Field()
    url_object_id = scrapy.Field(
        input_processor=MapCompose(md5_has)
    )
    tag_list = scrapy.Field()
    tags = scrapy.Field()
    content = scrapy.Field()

#知乎问答item
class ZhihuQuestionItem(scrapy.item):
    """
    知乎问题item
    """
    zhihu_id = scrapy.Field()
    topics = scrapy.Field()
    url = scrapy.Field()
    title = scrapy.Field()
    content = scrapy.Field()
    create_time = scrapy.Field()
    update_time = scrapy.Field()
    answer_num = scrapy.Field()
    comments_num = scrapy.Field()
    watch_user_num = scrapy.Field()
    click_num = scrapy.Field()
    crawl_time = scrapy.Field()
    crawl_update_time = scrapy.Field()

class ZhihuAnswerItem(scrapy.item):
    #z知乎回答item
    zhihu_id = scrapy.Field()
    url = scrapy.Field()
    question_id = scrapy.Field()
    author_id = scrapy.Field()
    content = scrapy.Field()
    praise_num = scrapy.Field()
    comments_num = scrapy.Field()
    create_time = scrapy.Field()
    update_time = scrapy.Field()
    crawl_time = scrapy.Field()
    crawl_update_time = scrapy.Field()

