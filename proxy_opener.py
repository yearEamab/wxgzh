__author__ = 'yearEamab'

import urllib.request
import random


ips=[]
def get_proxy():
    proxy_response=urllib.request.urlopen('http://47.113.102.131:5555/random')
    proxy_ip=proxy_response.read().decode('utf-8')
    return proxy_ip

def get_local_proxy():
    r=ips[random.randint(0,len(ips)-1)]
    return r['address']+':'+r['port']

def load_proxy():
    with open('proxy.txt','r',encoding='utf-8') as f:
        for x in f.readlines():
            ips.append(eval(x))
        f.close()

def proxy_opener(url,is_ajax):
    USER_AGENTS = [
            "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",
            "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)",
            "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)",
            "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)",
            "Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6",
            "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1",
            "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0",
            "Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5",
            "Mozilla/4.0 (compatible; MSIE 5.5;Windows NT)"
        ]
    request=urllib.request.Request(url)
    if is_ajax:
        request.add_header('Content-Type', 'application/json')
        request.add_header('X-Requested-With','XMLHttpRequest')
        request.add_header('Referer',url)
        request.add_header('origin','http://test2.diyiwl.wang')
    request.add_header('User-Agent', USER_AGENTS[random.randint(0,len(USER_AGENTS)-1)])
    p=urllib.request.ProxyHandler({"http" : get_proxy()})
    o=urllib.request.build_opener(p)
    try:
        #一定要设置超时，否则代理不稳定会卡在这,第一次open
        response=o.open(request,timeout=10)
        print('proxy '+url)
        return response.read()
    except:
        try:
            #第二次open
            p=urllib.request.ProxyHandler({"http" : get_proxy()})
            o=urllib.request.build_opener(p)
            response=o.open(request,timeout=3)
            print('proxy '+url)
            return response.read()
        except:
            #最后还不行使用无代理open
            try:
                print('timeout')
                print('no proxy '+url)
                return no_proxy_opener(url,is_ajax)
            except:
                return 0
    finally:
        o.close()



def no_proxy_opener(url,is_ajax):
    USER_AGENTS = [
            "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",
            "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)",
            "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)",
            "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)",
            "Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6",
            "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1",
            "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0",
            "Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5",
            "Mozilla/4.0 (compatible; MSIE 5.5;Windows NT)"
        ]
    request=urllib.request.Request(url)
    if is_ajax:
        request.add_header('Content-Type', 'application/json')
        request.add_header('X-Requested-With','XMLHttpRequest')
        request.add_header('Referer',url)
        request.add_header('origin','http://test2.diyiwl.wang')
    request.add_header('User-Agent', USER_AGENTS[random.randint(0,len(USER_AGENTS)-1)])
    try:
        response=urllib.request.urlopen(request,timeout=3)
        return response.read()
    except:
        return 0

# load_proxy()