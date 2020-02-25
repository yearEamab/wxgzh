__author__ = 'yearEamab'
from flask import make_response
import xml.etree.cElementTree as ET
import time
import pymysql
import reply_text

#处理event数据
def handle(data):
    xml = ET.fromstring(data)
    toUser = xml.find('ToUserName').text
    fromUser = xml.find('FromUserName').text
    msgType = xml.find("MsgType").text
    event = xml.find('Event').text
    res_content=''
    if event == 'subscribe':   #关注
        res_content='欢迎来到大枫叶，找到喜欢的动漫就可以进入观看哦,发送"新番"即可查看最近更新的番剧,发送星期一到星期日即可查看当天的更新,观看方法：将动漫名复制，发送消息到公众号，即可得到视频链接，点击即可观看~'
    else:  #取消关注
        res_content='期待你的下次关注~'
    if not res_content:
        res_content='呜呜呜，没有找到'
    reply=reply_text.make_reply(fromUser, toUser, str(int(time.time())), res_content)
    response = make_response(reply)
    response.headers['content-type'] = 'application/xml'
    return response