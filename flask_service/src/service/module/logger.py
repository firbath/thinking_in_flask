# -*- coding:utf-8 -*-
"""
File: logger.py
Author: YuFangHui
Date: 2019/11/19
Description:
"""
import logging.handlers
import os


def create_logger(log_path='/home/y_demo/log/', log_name="y_demo.log", level=logging.INFO):
    logging_msg_format = '[%(asctime)s] [%(filename)s[line:%(lineno)d]] [%(levelname)s] [%(message)s]'
    logging_date_format = '%Y-%m-%d %H:%M:%S'
    logging.basicConfig(level=level, format=logging_msg_format, datefmt=logging_date_format)
    if not os.path.exists(log_path):
        os.makedirs(log_path)
    log_path = os.path.join(log_path, log_name)
    file_handler = logging.handlers.WatchedFileHandler(log_path)
    file_handler.setFormatter(logging.Formatter(logging_msg_format))
    logger_h = logging.getLogger()
    logger_h.addHandler(file_handler)
    return logger_h


def init_app(app):
    # 配置
    config = app.default_config
    # 日志
    log = create_logger(config.get('log', 'log_dir'), config.get('log', 'log_file'), logging.INFO)
    app.app_logger = log
