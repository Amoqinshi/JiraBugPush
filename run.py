# !/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：DoPython 
@File ：run.py
@Author ：琴师
@Date ：2022/10/28 12:51 下午 
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


def main():

    job = schedule.every().day.at("15:00").do(send_request)
    job1 = schedule.every().day.at("17:00").do(send_request)
    job2 = schedule.every().day.at("18:00").do(send_request)
    if runJiraTask() ==1:
        while True:
            if  len(dataSearch()) > 0:
                schedule.run_pending()
                time.sleep(1)
            else:
                schedule.cancel_job(job)
                schedule.cancel_job(job1)
                schedule.cancel_job(job2)

    else:
        pass


if __name__=="__main__":
    main()