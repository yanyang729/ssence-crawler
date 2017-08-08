# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import psycopg2
from .items import *


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
                    (item.get('id'), item.get('name'), item.get('seoKeyword'), item.get('gender'))
                )
            elif type(item) is Product:
                self.cursor.execute(
                    """
                    INSERT INTO product (id, categoryid, name, brand, url, price, sku)
                    VALUES(%s, %s, %s, %s, %s, %s, %s )
                    """,
                    (item.get('id'), item.get('categoryid'), item.get('name'), item.get('brand'),
                     item.get('url'), item.get('price'), item.get('sku'))
                )
            elif type(item) is ProuctDetail:
                self.cursor.execute(
                    """
                    UPDATE product SET description = %s WHERE id = %s
                    """,
                    (item.get('description'), int(item.get('id')))
                )
            elif type(item) is Image:
                self.cursor.execute(
                    """
                    INSERT INTO image (url, productid)
                    VALUES (%s, %s)
                    """,
                    (item.get('url'), item.get('productid'))
                )
            elif type(item) is Inventory:
                self.cursor.execute(
                    """
                    INSERT INTO inventory  (sku, productid, sizename, instock)
                    VALUES (%s, %s, %s, %s)
                    """,
                    (item.get('sku'), item.get('productid'), item.get('name'), item.get('instock'))
                )

            self.connection.commit()

        except psycopg2.DatabaseError as e:
            print("Error: %s" % e)

        return item