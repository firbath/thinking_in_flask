# -*- coding:utf-8 -*-
"""
File: flask_service.py
Author: YuFangHui
Date: 2019/11/18
Description:
"""
import argparse
import os

from gevent import pywsgi
from geventwebsocket.handler import WebSocketHandler

from service import create_app
from service.utils import flask_utils

app = create_app()


def run_service():
    # 获取运行参数
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--port', type=int, default=8089, help='main service port')
    parser.add_argument('-d', '--debug_mode', action="store_true")
    args = parser.parse_args()
    flask_utils.show_all_route(app)
    app.config['MAX_CONTENT_LENGTH'] = 1024 * 1024 * 1024

    # crt_file = os.path.join(os.path.dirname(__file__), 'server.crt')
    # key_file = os.path.join(os.path.dirname(__file__), 'server.key')
    # server = pywsgi.WSGIServer(('0.0.0.0', args.port), app, keyfile=key_file, certfile=crt_file,
    #                            handler_class=WebSocketHandler)
    server = pywsgi.WSGIServer(('0.0.0.0', args.port), app, handler_class=WebSocketHandler)
    server.serve_forever()


if __name__ == "__main__":
    run_service()
