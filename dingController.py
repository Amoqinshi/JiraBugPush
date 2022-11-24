# !/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：DoPython 
@File ：dingController.py
@Author ：琴师
@Date ：2022/10/28 10:19 上午 
'''
# !/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：python_demo 
@File ：DingTalk.py
@Author ：琴师
@Date ：2022/3/16 10:37 下午 
'''


import dataSearchController
import requests
import json
import datetime,time
import hmac
import hashlib
import base64
from datetime import date, timedelta

# 今天
today = date.today()
# https://oapi.dingtalk.com/robot/send?access_token=

# def getSIGN():
    # timestamp = str(round(time.time() * 1000))
    # FzSecret = "SECbd19e453536cf580bb36f0f4cece879883d0e872680f7cae4f67b57e14bcc69f"
    # access_token = "be036787c5f07d4e29caf0c70712f9c99df18de6f8830aea5540ab5ecbe45dcc"
    # FzStringToSign = "%s\n%s" % (timestamp, FzSecret)
    # FzStringToSign_str = FzStringToSign.encode('utf-8')
    # HmacCode = hmac.new(FzSecret.encode('utf-8'), FzStringToSign_str, digestmod=hashlib.sha256).digest()
    # Sign = base64.b64encode(HmacCode).decode('utf-8')
    # data = {}
    # data["signature"] = Sign
    # data["timestamp"] = timestamp
    # data["access_token"] = access_token
    # return data


# params = getSIGN()


def getRequestUri():
    access_token = "52097df2c2495xxxxxxxxxxxxxxxxxx"
    # uri = "https://oapi.dingtalk.com/robot/send?" + "access_token=%s"%access_token + \
    #       "&" + "timestamp=%s"%time + "&" + "sign=%s"%sign
    uri = "https://oapi.dingtalk.com/robot/send?" + "access_token=%s" % access_token
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
            summary = "\n"
            for x in nums:
                summary += x[6] + "\t\t\t"+ "经办人："+x[4] +"\n"+"状态："+x[5]  + "\n"
                res_content = "今日新增问题:{}个，具体问题如下：{}".format(len(nums),summary)
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
    sendData = json.dumps(getRequestData(dataSearchController.dataSearch())) # 将字典类型数据转化为json格式
    res = requests.post(url=getRequestUri(), data=sendData, headers=header,verify=False)
    # 将请求发回的数据构建成为文件格式
    return res.json()


if __name__=="__main__":

    pass




