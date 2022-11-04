# !/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：DoPython 
@File ：dataSearchController.py
@Author ：琴师
@Date ：2022/10/28 11:47 上午 
'''

import jiraController
import dingController
import dataBaseController
from datetime import date

# 今天
today = date.today()


def dataSearch(values=repr(str(today))):
    todayBug = dataBaseController.selectDistinct(values)
    return todayBug





if __name__=="__main__":

    pass



