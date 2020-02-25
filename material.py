# -*- coding: utf-8 -*-
# filename: material.py
import urllib.request
import json
from basic import Basic

class Material(object):
    #获取素材列表
    def batch_get(self, accessToken, mediaType, offset=0, count=20):
        postUrl = ("https://api.weixin.qq.com/cgi-bin/material"
               "/batchget_material?access_token=%s" % accessToken)
        postData = ("{ \"type\": \"%s\", \"offset\": %d, \"count\": %d }"
                    % (mediaType, offset, count))
        urlResp = urllib.request.urlopen(postUrl, postData.encode())
        print(urlResp.read().decode())

if __name__ == '__main__':
    myMaterial = Material()
    accessToken = Basic().get_access_token()
    mediaType = "news"
    myMaterial.batch_get(accessToken, mediaType)