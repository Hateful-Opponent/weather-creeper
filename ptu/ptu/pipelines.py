# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymysql
import json

class PtuPipeline:
    def process_item(self, item, spider):
        self.db = pymysql.connect(
            host="localhost",
            user="root",
            password="root",
            database="weather"
        )

        self.cursor = self.db.cursor()
        sqls = "create table weather(日期 varchar(255), 平均高温 varchar(255), 平均低温 varchar(255), 最高气温 varchar(255)," \
               " 最低气温 varchar(255), 平均空气质量指数 varchar(255), 空气最好 varchar(255), 空气最差 varchar(255))"
        self.cursor.execute(sqls)
        self.db.commit()

        sql = "INSERT INTO weather (日期, 平均高温, 平均低温, 最高气温, 最低气温, 平均空气质量指数, 空气最好, 空气最差)" \
              " VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"

        values = [item['date'],item['avange_high_temp'],item['avange_low_temp'],
                  item['higgest_temp'],item['lowest_temp'],item['avange_air'],
                  item['best_air'],item['worst_air']]

        self.cursor.execute(sql, values)
        self.db.commit()

        return item


    def close_spider(self,spider):

        self.cursor.close()
        self.db.close()