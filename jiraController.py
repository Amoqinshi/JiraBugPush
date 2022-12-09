# !/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：DoPython
@File ：jiraController.py
@Author ：琴师
@Date ：2022/10/25 4:36 下午
"""
from jira import JIRA
from datetime import date, timedelta
import dataBaseController
import time
import datedays


username = "qinshi"
password = "909090yh"


# 连接jira服务地址
def login_jira(userName, passWord):
    jira = JIRA("http://jira.huanleguang.com", basic_auth=(userName, passWord))
    return jira


# 实例话jira对象
a = login_jira(username, password)


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


def getIssueList(today_time, tomorrow_time):
    """
    :param today_time: 今天
    :param tomorrow_time: 明天
    :return: 根据时间范围爬去创建的bug列表
    """
    issue_list = a.search_issues(
        "project = {} AND issuetype in (体验走查, 线上问题, 转测问题) AND resolution was not 非问题 AND updated >= {} AND updated <= "
        "{} "
        "".format(
            "NEBULA",
            today_time,
            tomorrow_time))
    return issue_list


# 实例化获取Issue列表对象
issueData = getIssueList(today, tomorrow)


def getBugList(issueData):
    """
    :return: 解析bug数据
    """
    jiraHost = "https://jira.huanleguang.com/browse/"
    if len(issueData) != 0:
        bugId = [issue.key for issue in issueData]
        bugSummary = [issue.fields.summary for issue in issueData]
        bugCreater = [issue.fields.reporter.name for issue in issueData]    #
        bugAssigner = [
            issue.fields.assignee.name if issue.fields.assignee else "null" for issue in issueData]
        bugStatus = [issue.fields.status.name for issue in issueData]
        bugLinkUrl = [jiraHost + issue.key for issue in issueData]
        bugType = [issue.fields.issuetype.name for issue in issueData]
        bugCreateTIme = [issue.fields.created[:10] for issue in issueData]
        bugUpdateTIme = [issue.fields.updated[:10] for issue in issueData]
        bugList = list(zip(bugId,
                           bugSummary,
                           bugCreater,
                           bugAssigner,
                           bugStatus,
                           bugLinkUrl,
                           bugType,
                           bugCreateTIme,
                           bugUpdateTIme))
        return bugList
    else:
        return 0


def writeBugList(data):
    """
    :return: 写入数据
    """
    for data_ in data:
        dataBaseController.insertTables(data_)


def runJiraTask():
    # issueData = getIssueList(today, tomorrow)

    data = getBugList(issueData)
    print("data:", data)
    time.sleep(3)
    if data != 0:
        writeBugList(data)
        return 1
    else:
        pass


if __name__ == "__main__":
    pass
