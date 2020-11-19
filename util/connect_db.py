#!-*- coding:utf-8 -*-
__author__ = 'ALX LIN'
import pymysql
import json
class OperationMysql:
    def __init__(self):
        self.conn = pymysql.connect(
            host="127.0.0.1",
            port=3306,
            user="root",
            passwd="123456",
            db="hulin",
            charset="utf8",
            cursorclass=pymysql.cursors.DictCursor)
        self.cur = self.conn.cursor()

    def search_all(self, sql):
        self.cur.execute(sql)
        result = self.cur.fetchone()
        print(type(result))
        result = json.dumps(result)
        print(type(result))
        print(result)

if __name__ == "__main__":
    s = OperationMysql()
    s.search_all("select * from test2")