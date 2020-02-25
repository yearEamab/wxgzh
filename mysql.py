__author__ = 'yearEamab'
import pymysql
import time

#从数据库中拿数据
def get_from_mysql_by_namedetail(text):
    db = pymysql.connect("127.0.0.1","wxgzh","Yeareamab6859","wxgzh")
    cursor = db.cursor()
    sql="select url from dfydm where id=(select max(id) from dfydm where name_detail='{0}')".format(text)
    cursor.execute(sql)
    result=cursor.fetchall()
    res_content=result[0][0]
    db.close()
    return res_content

def get_xinfan_from_mysql():
    db = pymysql.connect("127.0.0.1","wxgzh","Yeareamab6859","wxgzh")
    cursor = db.cursor()
    sql="select distinct name_detail from dfydm where insert_time>=CURDATE()"
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