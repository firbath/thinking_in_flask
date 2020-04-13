# -*- coding:utf-8 -*-
"""
File: tools.py
Author: YuFangHui
Date: 2019-05-06
Description:
"""
import os
from os.path import exists


def check_dir(dir_path, flag=True):
    if exists(dir_path):
        return True
    elif flag:
        os.makedirs(dir_path)
    return exists(dir_path)


def print_content(content):
    print('type:', type(content), '\n', content, '\n')


def read_file(path):
    f = open(path, 'r', encoding='utf-8')
    content = f.read()
    f.close()
    return content


def write_file(path, content):
    f = open(path, 'w', encoding='utf-8')
    f.write(content)
    f.close()
