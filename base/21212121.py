#!-*- coding:utf-8 -*-
__author__ = 'ALX LIN'
#连接数据库
import pymysql.cursors
#
# conn = pymysql.connect(
#     host="127.0.0.1",
#     port=3306,
#     user="root",
#     passwd="123456",
#     db="hulin",
#     charset="utf8",
#     cursorclass=pymysql.cursors.DictCursor)
#
# cur = conn.cursor()
#
# sql = "select * from test2"
# cur.execute(sql)
# print(cur.fetchone())


#比较二个字典
import operator
a = {"name": "hulin", "address": "chengdu", "transactor": "it", "id": 1}
b = {"transactor": "it", "id": 1, "name": "hulin", "address": "chengdu"}
print(operator.eq(a,b))