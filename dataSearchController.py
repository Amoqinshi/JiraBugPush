# !/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：DoPython
@File ：dataSearchController.py
@Author ：琴师
@Date ：2022/10/28 11:47 上午
"""

import dataBaseController
from datetime import date

# 今天
today = date.today()


def dataSearchType(values=repr(str(today)), bugtype=None):
    """查询问题类型"""
    todayBug = dataBaseController.selectType(values, bugtype)
    return todayBug


def dataSearch(values=(repr(str(today)))):
    """查询问题总数"""
    todayBug = dataBaseController.selectTables(values)
    return todayBug


if __name__ == "__main__":
    pass
