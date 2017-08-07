# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import psycopg2
from .items import Category, Product


class DumpPostgresPipeline(object):
    def __init__(self):
        self.connection = psycopg2.connect(host='localhost', database='ssense', user='yangyang')
        self.cursor = self.connection.cursor()

    def process_item(self, item, spider):
        # check item type to decide which table to insert
        try:
            if type(item) is Category:
                self.cursor.execute(
                    """
                    INSERT INTO category (id, name, seokeyword, gender)
                    VALUES(%s, %s, %s, %s)
                    """,
                    (item.get('id'), item.get('name'), item.get('seoKeyword'), item.get('gender'),)
                )
            elif type(item) is Product:
                self.cursor.execute(
                    """
                    INSERT INTO categories (id, name)
                    VALUES(%s, %s)
                    """,
                    (item.get('id'), item.get('code'),)
                )
            self.connection.commit()
            self.cursor.fetchall()

        except psycopg2.DatabaseError as e:
            print("Error: %s" % e)

        return item