# !/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：JiraBugPush
@File ：run.py
@Author ：琴师
@Date ：2022/11/8 2:16 下午
"""
from jiraController import runJiraTask
from dingController import send_request
from datetime import date
import schedule
import time


# 今天
today = date.today()

# 每1小时执行jira问题爬取的定时任务
schedule.every().hour.do(runJiraTask)

# 每天下午18：00定时发送钉钉
schedule.every().day.at("18:00").do(send_request)


def main():
    """
    :return:
    """

    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    main()
