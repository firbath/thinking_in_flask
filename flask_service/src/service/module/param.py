# -*- coding:utf-8 -*-
"""
File: ac_param.py
Author: YuFangHui
Date: 2019/11/19
Description:
"""
import json
import os

from service.module import config


def get_all_role_list():
    rp_dict = load_role_permission()
    role_list = rp_dict.keys() - "administrator"

    return role_list


def get_role_permissions(role):
    rp_dict = load_role_permission()

    return rp_dict.get(role, list())


def load_role_permission():
    path = os.path.join(config.get_param_dir(), 'role_permission.json')
    param = dict()
    try:
        with open(path, 'r') as f:
            param = json.load(f)
    except Exception as e:
        print(e)

    return param

# def set_all_role_list(task_list):
#     path = os.path.join(config.get_param_dir(), 'all_role_list.json')
#     with open(path, 'w') as f:
#         json.dump(task_list, f)
