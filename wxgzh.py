from flask import Flask
from flask import request,make_response
import hashlib
import xml.etree.cElementTree as ET
import time
import handle_text
import handle_event

app = Flask(__name__)

@app.route("/weixin/",methods=["GET","POST"])
def index():
    if request.method == "GET":       # 判断请求方式是GET请求
        my_signature = request.args.get('signature')     # 获取携带的signature参数
        my_timestamp = request.args.get('timestamp')     # 获取携带的timestamp参数
        my_nonce = request.args.get('nonce')        # 获取携带的nonce参数
        my_echostr = request.args.get('echostr')         # 获取携带的echostr参数

        token = 'hahaha'     # 一定要跟刚刚填写的token一致

        # 进行字典排序
        data = [token,my_timestamp ,my_nonce ]
        data.sort()

        # 拼接成字符串
        temp = ''.join(data)

        # 进行sha1加密
        mysignature = hashlib.sha1(temp.encode('utf8')).hexdigest()

        # 加密后的字符串可与signature对比，标识该请求来源于微信
        if my_signature == mysignature:
            return my_echostr
    if request.method=="POST":
        xml = ET.fromstring(request.data)
        msgType = xml.find("MsgType").text
        if msgType=='text':
            response=handle_text.handle(request.data)
        if msgType=='event':
            response=handle_event.handle(request.data)
        return response

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=80)