__author__ = 'yearEamab'
from flask import make_response
import xml.etree.cElementTree as ET
import time
import pymysql
import re
import reply_text
import reply_news
import mysql

#处理text数据
def handle(data):
    xml = ET.fromstring(data)
    toUser = xml.find('ToUserName').text
    fromUser = xml.find('FromUserName').text
    msgType = xml.find("MsgType").text
    content=xml.find("Content").text
    res_content=''
    if content=='新番':
        res_content=mysql.get_xinfan_from_mysql()
        img_url='http://ae01.alicdn.com/kf/Hcf4a81a8f3174d4483e4ebfd82bb6d15M.jpg'
        url=mysql.get_news_url_from_mysql(content)
        reply=reply_news.make_reply(fromUser,toUser,str(int(time.time())),content,res_content,img_url,url)
        response = make_response(reply)
        response.headers['content-type'] = 'application/xml'
        return response
    #如果是星期一到星期日返回图文信息
    elif re.match('^(星期一|星期二|星期三|星期四|星期五|星期六|星期日)$',content):
        #拿当天的前10条作为desc
        res_content=mysql.get_xingqi_from_mysql(content)
        img_url='http://ae01.alicdn.com/kf/Hcf4a81a8f3174d4483e4ebfd82bb6d15M.jpg'
        url=mysql.get_news_url_from_mysql(content)
        reply=reply_news.make_reply(fromUser,toUser,str(int(time.time())),content,res_content,img_url,url)
        response = make_response(reply)
        response.headers['content-type'] = 'application/xml'
        return response
    else:
        res_content=mysql.get_from_mysql_by_namedetail(content)
    if not res_content:
        res_content='呜呜呜，没有找到'
    reply=reply_text.make_reply(fromUser, toUser, str(int(time.time())), res_content)
    response = make_response(reply)
    response.headers['content-type'] = 'application/xml'
    return response