__author__ = 'yearEamab'


def make_reply(fromUser,toUser,create_time,res_content):
    reply = '''<xml>
            <ToUserName><![CDATA[%s]]></ToUserName>
            <FromUserName><![CDATA[%s]]></FromUserName>
            <CreateTime>%s</CreateTime>
            <MsgType><![CDATA[text]]></MsgType>
            <Content><![CDATA[%s]]></Content>
            </xml>'''
    return reply % (fromUser, toUser, create_time, res_content)