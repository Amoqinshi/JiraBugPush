# !/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：DoPython 
@File ：runMain.py
@Author ：琴师
@Date ：2022/11/8 2:16 下午
'''
from  jiraController import runJiraTask
from  dingController import send_request
from  dataSearchController import dataSearch
from dataBaseController import selectTables
from datetime import date
import schedule
import time



# 今天
today = date.today()

# 每小时执行jira问题爬取的定时任务
schedule.every().hour.do(runJiraTask)
# 每天18：00定时发送钉钉
schedule.every().day.at("18:01").do(send_request)


def main():
    """
    :return:
    """

    while True:
        schedule.run_pending()
        time.sleep(1)




if __name__=="__main__":
    main()