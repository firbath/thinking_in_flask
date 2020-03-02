# -*- coding:utf-8 -*-
"""
File: socket_controller
Author: YuFangHui
Date: 2020/1/23
Description:
"""
from flask import request
from geventwebsocket.websocket import WebSocket

from service.SI_Utils import time_utils

user_dict = {}


def play(username):
    print(username)
    user_socket = request.environ.get('wsgi.websocket')  # type:WebSocket
    user_dict[username] = user_socket
    while 1:
        msg = user_socket.receive()  # 等待接收客户端发来的数据
        # msg = msg + ':' + time_utils.time2str()
        for uname, uwebsocket in user_dict.items():
            if uname == username:  # 不用给自己发
                continue
            uwebsocket.send(msg)
