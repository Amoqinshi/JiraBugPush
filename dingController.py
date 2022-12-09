# !/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：DoPython
@File ：dingController.py
@Author ：琴师
@Date ：2022/10/28 10:19 上午
"""

# 今天

import dataSearchController
import requests
import json
import time
from datetime import date

# 今天
today = date.today()


def getRequestUri():
    access_token = "52097df2c2495168c6918c7c5ac468d9b14d8361753fe87axxxxxx"
    uri = "https://oapi.xxxxxxx?" + "access_token=%s" % access_token
    return uri


def getRequestData(nums):
    my_data = {
        "msgtype": "markdown",
        "markdown": {
            "title": "JIRA",
            "text": "我就是我, 是不一样的烟火"
        },
        "at": {
            "isAtAll": True
        }
    }
    if len(nums):
        # summary = "\n"
        testProblem = "\n"
        productProblem = "\n"
        uat = "\n"
        if dataSearchController.dataSearchType(bugtype="转测问题"):
            for x in dataSearchController.dataSearchType(bugtype="转测问题"):
                testProblem += x[6] + "\t\t\t" + "经办人：" + \
                    x[4] + "\n" + "状态：" + x[5] + "\n"
        else:
            testProblem = "0" + "\n个"

        if dataSearchController.dataSearchType(bugtype="体验走查"):
            for y in dataSearchController.dataSearchType(bugtype="体验走查"):
                uat += y[6] + "\t\t\t" + "经办人：" + \
                    y[4] + "\n" + "状态：" + y[5] + "\n"
        else:
            uat = "0" + "\n个"

        if dataSearchController.dataSearchType(bugtype="线上问题"):
            for z in dataSearchController.dataSearchType(bugtype="线上问题"):
                productProblem += z[6] + "\t\t\t" + \
                    "经办人：" + z[4] + "\n" + "状态：" + z[5] + "\n"
        else:
            productProblem = "0" + "\n个"

        res_content = "今日新增问题:{}个，具体问题如下：\n" \
                      "=======================================" \
                      "\n【--转测问题--】：{}\n" \
                      "\n【--体验走查--】：{}\n" \
                      "\n【--线上问题(历史版本遗留)--】：{}\n\n" \
                      "=======================================" \
                      "\nTips：优先解决转测问题和线上问题即可～\n".format(len(nums), testProblem, uat, productProblem)
        my_data["markdown"]["text"] = res_content
        return my_data
    else:
        res_content = "今日新增问题:{}个".format(len(nums))
        my_data["markdown"]["text"] = res_content
        return my_data


def send_request():
    # 传入url和内容发送请求
    # 构建一下请求头部
    header = {"content-Type": "application/json", "Charset": "UTF-8",
              "timestamp": str(round(time.time() * 1000))}
    sendData = json.dumps(
        getRequestData(
            dataSearchController.dataSearch()))  # 将字典类型数据转化为json格式
    res = requests.post(
        url=getRequestUri(),
        data=sendData,
        headers=header,
        verify=False)
    # 将请求发回的数据构建成为文件格式
    return res.json()


if __name__ == "__main__":
    pass

