# !/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：DoPython 
@File ：jiraController.py
@Author ：琴师
@Date ：2022/10/25 4:36 下午 
'''
from jira import JIRA
from datetime import date, timedelta
import dataBaseController
import time,datedays


username = "qinshi"
password = "909090yh"


# 连接jira服务地址
def login_jira(username,password):
    jira = JIRA("http://jira.huanleguang.com",basic_auth=(username,password))
    return jira

# 实例话jira对象
a = login_jira(username,password)



def getAllProjects():
    """
    :return: 获取所有项目空间
    """
    return a.projects()


def getSingleProjects(id):
    """
    :return: 获取单个项目空间
    """
    return a.project(id)


# 昨天
yesterday = (date.today() + timedelta(days=-1)).strftime("%Y-%m-%d")

# 今天
today = date.today()

# 明天
tomorrow = datedays.gettomorrow()


def getIssueList(today_time,tomorrow_time):
    """
    :param today_time: 今天
    :param tomorrow_time: 明天
    :return: 根据时间范围爬去创建的bug列表
    """
    issue_list = a.search_issues("project = {} AND issuetype in (线上问题, 转测问题) AND status = 问题-新  AND created >= {} AND created <= {} "
                                 # "order by created DESC".format("NEBULA", "2022-10-29", "2022-10-30"))
                                 "order by created DESC".format("NEBULA", today_time, tomorrow_time))
    return issue_list


# 实例化获取Issue列表对象
# issueData = getIssueList("2022-10-27", "2022-10-31")
# issueData = getIssueList("2022-11-03", "2022-11-04")
issueData = getIssueList(today, tomorrow)



def getBugList(issueData):
    """
    :return: 解析bug数据
    """
    if len(issueData) == 0 :
        print("jiraBug数据获取为空")
    else:
        print("jiraBug数据正常获取")
        bugId = [issue.key for issue in issueData]
        bugSummary =  [issue.fields.summary for issue in issueData]
        bugCreater =  [issue.fields.reporter.name for issue in issueData]
        bugCreateTIme =  [(issue.fields.created)[:10] for issue in issueData]
        bugUpdateTIme =  [(issue.fields.updated)[:10] for issue in issueData]
        bugList = list(zip(bugId,bugSummary,bugCreater,bugCreateTIme,bugUpdateTIme))
        return bugList

# A = getBugList()
# print(A)

def writeBugList(bugData):
    """
    :return: 写入数据
    """
    for  x in bugData:
        time.sleep(1)
        dataBaseController.insertTables(x)
    print ("==============数据写入完成===================")


def runJiraTask():
    data = getBugList(issueData)
    time.sleep(2)
    if data is not None:
        writeBugList(data)
        return 1
    else:
        print("==============今日无数据写入==================")
        return 0


if __name__=="__main__":

    pass
