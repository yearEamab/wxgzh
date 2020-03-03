__author__ = 'yearEamab'
import proxy_opener
import time
import json

def get_url(id):
    try:
        res=proxy_opener.proxy_opener('http://test.1yltao.com/testapi888.php?time='+str(int(time.time()))+'&url='+id,1)
        if res!=0:
            try:
                dict_url=json.loads(res.decode())
            except:
                return 0
            print(dict_url)
            if dict_url['success']==1:
                return dict_url['url']
            else:
                return 0
        else:
            return 0
    except:
        return 0

def get_url_noproxy(id):
    try:
        res=proxy_opener.no_proxy_opener('http://test.1yltao.com/testapi888.php?time='+str(int(time.time()))+'&url='+id,1)
        if res!=0:
            try:
                dict_url=json.loads(res.decode())
            except:
                return 0
            print(dict_url)
            if dict_url['success']==1:
                return dict_url['url']
            else:
                return 0
        else:
            return 0
    except:
        return 0


if __name__=="__main__":
    get_url('1097_d13a9f2c8aec4bdb8d40842632a0dbbb')