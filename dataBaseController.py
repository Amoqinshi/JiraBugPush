# !/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：DoPython 
@File ：dataBaseController.py
@Author ：琴师
@Date ：2022/10/27 10:22 上午 
'''
import pymysql
from datetime import date, timedelta


# 数据库配置
data_dict = {"host":"xxxxxx",
             "user":"xxxxxx",
             "password":"xxxxxx",
             "port":3306,
             "dataBase":"xxxxxx"}




def connectDatabse():
    """
    :return: 连接数据库
    """
    db = pymysql.connect(host=data_dict["host"],
                         user=data_dict["user"],
                         password=data_dict["password"],
                         port=data_dict["port"],
                         database=data_dict["dataBase"])
    try:
        db.ping(reconnect=True)
        print("数据库处于连接中状态")
        return db
    except:
        connectDatabse()
        print("数据库断开连接，请重新连接数据库")


# 实例化数据库连接对象
db_con = connectDatabse()


# 创建数据库表
def createTable():
    """
    :param connect: 传入数据库对象
    :return: 生成表
    """
    try:
        with db_con.cursor() as cursor:
            sql = """CREATE TABLE NewIncreasedBug(
                                   id int auto_increment,
                                   bugId varchar(120),
                                   bugName varchar(120),
                                   createBy varchar(20),
                                   createDay date,
                                   updateDay date,
                                   primary key (id))"""
            cursor.execute(sql)
            db_con.commit()
            return "新表创建成功"

    except:
        db_con.rollback()


def insertTables(data):
    """
    :param connect:
    :param table:
    :param kwargs:
    :return:
    """
    try:
        with db_con.cursor() as cursor:
            sql = """INSERT INTO NewIncreasedBug (bugId, bugName, createBy, createDay, updateDay)
                        VALUES {}""".format(data)
            cursor.execute(sql)
            db_con.commit()
            return "表数据插入成功"

    except:
        db_con.rollback()


def selectTables(values,condition="CREATEDAY"):
    """
    :param connect:
    :param table:
    :param kwargs:
    :return:
    """
    try:
        with db_con.cursor() as cursor:
            sql = """SELECT *  FROM  NewIncreasedBug WHERE {} = {} ORDER BY CREATEDAY DESC""".format(condition,values)
            cursor.execute(sql)
            all = cursor.fetchall()
            return all
    except:
        db_con.rollback()

def selectAll():
    """
    :param connect:
    :param table:
    :param kwargs:
    :return:
    """
    try:
        with db_con.cursor() as cursor:
            sql = """SELECT distinct bugId,bugName,createBy,createDay,updateDay from NewIncreasedBug """
            cursor.execute(sql)
            all = cursor.fetchall()
            return all
    except:
        db_con.rollback()


def selectDistinct(values,condition="CREATEDAY"):
    """
    :param connect:
    :param table:
    :param kwargs:
    :return:
    """
    try:
        with db_con.cursor() as cursor:
            sql = """SELECT distinct bugId,bugName,createBy,createDay,updateDay  FROM  NewIncreasedBug  WHERE {} = {} 
                    """.format(condition,values)
            cursor.execute(sql)
            all = cursor.fetchall()
            return all
    except:
        db_con.rollback()

def deleteTables(values,condition="CREATEDAY"):
    """
    :param connect:
    :param table:
    :param kwargs:
    :return:
    """
    try:
        with db_con.cursor() as cursor:
            sql = """DELETE FROM  NewIncreasedBug WHERE {} = {}""".format(condition,values)
            cursor.execute(sql)
            return ("表数据删除成功")
    except:
        db_con.rollback()





if __name__=="__main__":

    pass
