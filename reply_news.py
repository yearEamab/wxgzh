__author__ = 'yearEamab'

def make_reply(fromUser,toUser,create_time,content,res_content,img_url,url):
     reply='''<xml>
                  <ToUserName><![CDATA[%s]]></ToUserName>
                  <FromUserName><![CDATA[%s]]></FromUserName>
                  <CreateTime>%s</CreateTime>
                  <MsgType><![CDATA[news]]></MsgType>
                  <ArticleCount>1</ArticleCount>
                  <Articles>
                    <item>
                      <Title><![CDATA[%s]]></Title>
                      <Description><![CDATA[%s]]></Description>
                      <PicUrl><![CDATA[%s]]></PicUrl>
                      <Url><![CDATA[%s]]></Url>
                    </item>
                  </Articles>
                </xml>
                '''
     return reply %(fromUser,toUser,create_time,content,res_content,img_url,url)