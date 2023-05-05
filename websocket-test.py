#!/usr/bin/env python3
# -*- coding: utf-8 -*- 
import websocket
import json

url = 'ws://host:8866'  #websocket连接地址
ws = websocket.create_connection(url)  #创建连接
#'''data为json格式'''
data = {"body":{"address":"陕西省","location":{"latitude":11.23256618923611,"longitude":218.9637478298611,"timestamp":1541735071192},"state":"arrivalDepot","timestamp":1541862074000,"trackId":3218111000038001,"transportId":218111000038},"token":"token","type":"roadtrace_state"}
ws.send(json.dumps(data))   #json转化为字符串，必须转化
print(ws.recv())    #服务器响应数据
ws.close()   #关闭连接