__author__ = 'yearEamab'
import pymysql
import time
import re
import get_url_from_ajax

#从数据库中拿数据
def get_from_mysql_by_namedetail(text):
    db = pymysql.connect("127.0.0.1","wxgzh","Yeareamab6859","wxgzh")
    cursor = db.cursor()
    sql="select url from dfydm where name_detail='{0}'".format(text)
    cursor.execute(sql)
    result=cursor.fetchall()
    res_content=''
    if result:
        res_content=text+'\n'
        for x in result:
            if re.match('.*\.mp4|.*m3u8',x[0]):
                video_url='http://op.mtyee.com/f/dplayer.php?url='+x[0]
                res_content=res_content+video_url+'\n\n'
            if re.match('.*html',x[0]):
                video_url='https://jx.yingxiangbao.cn/vip.php?url='+x[0]
                res_content=res_content+video_url+'\n\n'
        if res_content!='':
            return res_content.strip()
        else:
            for x in result:
                if re.match('\d+_.*',x[0]):
                    video_url=get_url_from_ajax.get_url_noproxy(x[0])
                    res_content=res_content+video_url+'\n\n'
            if res_content=='':
               res_content=res_content+result[0][0]+'\n\n'
            return res_content.strip()
    else:
        sql="select distinct name_detail from dfydm where name_detail like '%{0}%'".format(text)
        cursor.execute(sql)
        result1=cursor.fetchall()
        if len(result1)>100:
            res_content='查询结果过多，请输入更详细的名字'
            return res_content.strip()
        elif result1:
            for x in result1:
                res_content=res_content+x[0]+'\n'
            res_content=res_content+'将上面的结果发送，即可得到播放链接'+'\n'
            return res_content.strip()
    db.close()
    return res_content.strip()

def get_xinfan_from_mysql():
    db = pymysql.connect("127.0.0.1","wxgzh","Yeareamab6859","wxgzh")
    cursor = db.cursor()
    sql="select distinct name from dfydm where insert_time>=CURDATE()"
    cursor.execute(sql)
    result=cursor.fetchall()
    res_content=''
    db.close()
    for x in result:
        res_content=res_content+x[0]+'\n'
    return res_content

def get_xingqi_from_mysql(text):
    db = pymysql.connect("127.0.0.1","wxgzh","Yeareamab6859","wxgzh")
    cursor = db.cursor()
    now=time.localtime(time.time())[6]
    if now==0:
        list=[0,6,5,4,3,2,1]
    if now==1:
        list=[1,0,6,5,4,3,2]
    if now==2:
        list=[2,1,0,6,5,4,3]
    if now==3:
        list=[3,2,1,0,6,5,4]
    if now==4:
        list=[4,3,2,1,0,6,5]
    if now==5:
        list=[5,4,3,2,1,0,6]
    if now==6:
        list=[6,5,4,3,2,1,0]
    if text=='星期一':
        n=list[0]
    if text=='星期二':
        n=list[1]
    if text=='星期三':
        n=list[2]
    if text=='星期四':
        n=list[3]
    if text=='星期五':
        n=list[4]
    if text=='星期六':
        n=list[5]
    if text=='星期日':
        n=list[6]
    sql="select distinct name_detail from dfydm where insert_time>=date_sub(curdate(),interval {0} day) and insert_time<date_sub(curdate(),interval {1} day) limit 10".format(n,n-1)
    cursor.execute(sql)
    result=cursor.fetchall()
    res_content=''
    db.close()
    for x in result:
        res_content=res_content+x[0]+'\n'
    return res_content


def get_news_url_from_mysql(text):
    db = pymysql.connect("127.0.0.1","wxgzh","Yeareamab6859","wxgzh")
    cursor = db.cursor()
    sql="select news_url from news where week_name='{0}'".format(text)
    cursor.execute(sql)
    result=cursor.fetchall()
    res_content=result[0][0]
    db.close()
    return res_content