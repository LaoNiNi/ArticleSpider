# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import codecs,json
import pymysql


from scrapy.exporters import JsonItemExporter

class ArticlespiderPipeline(object):
    def process_item(self, item, spider):
        return item

#自定义jsonpipeline
class JsonWithEncodingPipeline(object):
    def __init__(self):
        #使用codecs来打开一个文件，可以解决好编码问题
        self.file = codecs.open("article.json","w",encoding="utf-8")
    def process_item(self,item,spider):
        lines = json.dumps(dict(item),ensure_ascii=False) +"\n"
        self.file.write(lines)
        return item

    def spider_closed(self,spider):
        self.file.close()

class JsonExporterPipeline(object):
    #调用scrapy提供的json export导出json文件
    def __init__(self):
        self.file = open("articleexport.json","wb")
        self.exporter = JsonItemExporter(self.file,encoding="utf-8",ensure_ascii=False)
        self.exporter.start_exporting()

    def close_spider(self,spider):
        self.exporter.finish_exporting()
        self.file.close()

    def process_item(self,item,spider):
        self.exporter.export_item(item)
        return item


class MysqlPipeline(object):
    def __init__(self):
        self.conn = pymysql.connect('localhost','root','123456','learn_scrapy',charset='utf8',use_unicode=True)
        self.cursor = self.conn.cursor()

    def process_item(self,item,spider):
        """
        :param item:
        :param spider:
        :return:
        """

        a = 1
        insert_sql ="""insert into jobble(title,front_image_url,front_image_path,create_date,praise_nums,comment_nums,
fav_nums,url,url_object_id,tag_list,tags,content) 
values ('{title}','{front_image_url}','{front_image_path}','{create_date}',{praise_nums},{comment_nums},{fav_nums},
'{url}','{url_object_id}','{tag_list}','{tags}','{content}')"""
        insert_sql2 = insert_sql.format(title=item['title'],front_image_url=item['front_image_url'][0],front_image_path=item['front_image_path'],
                                        create_date=item['create_date'], praise_nums=item['praise_nums'],comment_nums=item['comment_nums'],
                                        fav_nums=item['fav_nums'],url=item['url'],
                                        url_object_id=item['url_object_id'],tag_list=item['tag_list'],tags=item['tags'],content=item['content'])
        # for x,y in item:
        #     print("$$$$$$$$",type(x))
        # self.cursor.execute(insert_sql,(item['title'],item['front_image_url'][0],item['front_image_path'],item['create_date'],
        #                                 item['praise_nums'],item['comment_nums'],item['fav_nums'],item['url'],
        #                                 item['url_object_id'],item['tag_list'],item['tags'],item['content']))
        self.cursor.execute(insert_sql2)
        self.conn.commit()
