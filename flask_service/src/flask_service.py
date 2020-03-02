# -*- coding:utf-8 -*-
"""
File: demo_service.py
Author: YuFangHui
Date: 2019/11/18
Description:
"""
import argparse

from gevent import pywsgi
from geventwebsocket.handler import WebSocketHandler

from service import create_app
from service.SI_Utils import si_flask_utils

app = create_app()


def run_service():
    # 获取运行参数
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--port', type=int, default=8083, help='main service port')
    parser.add_argument('-d', '--debug_mode', action="store_true")
    args = parser.parse_args()
    si_flask_utils.show_all_route(app)
    app.config['MAX_CONTENT_LENGTH'] = 1024 * 1024 * 1024

    server = pywsgi.WSGIServer(('0.0.0.0', args.port), app, handler_class=WebSocketHandler)
    server.serve_forever()


if __name__ == "__main__":
    run_service()
