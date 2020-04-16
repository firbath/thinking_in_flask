# -*- coding:utf-8 -*-
"""
File: file_manager.py
Author: YuFangHui
Date: 2019/11/25
Description:
"""
import json
import os
import shutil

from flask import current_app
from flask_uploads import UploadSet, ALL

from service.module.config import get_config
from y_utils import time_utils, tools
from y_utils.file_utils import check_dir

upload_mark = 'tk'
upload_dest = 'UPLOADED_TK_DEST'
map_file = 'file_map.json'


def init_work_dir(date):
    work_dir = os.path.join(current_app.default_config.get('data', 'work_dir'), date)
    if check_dir(work_dir, True):
        return work_dir
    return None


def list_my_file(user_name, check=True):
    folder = user_name
    destination = current_app.upload_set_config.get(upload_mark).destination
    tar_dir = os.path.join(destination, folder)
    check_dir(tar_dir, True)
    src_dict = get_files_dict(tar_dir)
    key_list = list()
    dst_dict = dict()
    for k, v in src_dict.items():
        real_path = os.path.join(tar_dir, v)
        if os.path.exists(real_path):
            dst_dict[k] = v

    if check:
        map_path = os.path.join(tar_dir, map_file)
        with open(map_path, 'w') as f:
            json.dump(dst_dict, f)

    for word in dst_dict.keys():
        key_list.append({
            'name': word,
            'url': '/download_mine/%s/%s' % (user_name, word)
        })

    return key_list


def upload_files(file_list, user_name):
    up_list = list()
    if not file_list:
        return up_list
    ac_upload_set = UploadSet(upload_mark, ALL)
    folder = user_name
    destination = current_app.upload_set_config.get(upload_mark).destination
    tar_dir = os.path.join(destination, folder)
    map_path = os.path.join(tar_dir, map_file)

    try:
        with open(map_path, 'r') as f:
            map_dict = json.load(f)
    except Exception as e:
        print(e)
        map_dict = dict()

    for storage in file_list:
        print(storage)
        basename = 'y_' + ac_upload_set.get_basename(storage.filename)
        print(basename)
        upload_name = sign_st_name(basename)
        print(upload_name)
        save_name = ac_upload_set.save(storage, folder=folder, name=upload_name)
        print(os.path.basename(save_name))
        map_dict[basename] = os.path.basename(save_name)
        up_list.append(basename)

    with open(map_path, 'w') as f:
        json.dump(map_dict, f)

    return up_list


# 文件名加注时间戳
def sign_st_name(basename):
    ts_filename = '{}.{}'.format(time_utils.get_timestamp(), basename)
    return ts_filename


def check_file(file_reg, user_name):
    folder = user_name
    destination = current_app.upload_set_config.get(upload_mark).destination
    tar_dir = os.path.join(destination, folder)
    file_dict = get_files_dict(tar_dir)
    real_path = os.path.join(tar_dir, get_real_name(file_dict, file_reg))
    if os.path.exists(real_path):
        return real_path
    return ''


def prepare_work_dir(file_reg, user_name):
    work_dir = os.path.join(get_config().get('data', 'work_dir'), user_name, file_reg[0:len(file_reg) - 4])
    print('rm', work_dir)
    shutil.rmtree(work_dir, ignore_errors=True)
    if tools.check_dir(work_dir) and tools.check_dir(os.path.join(work_dir, 'rec')):
        return work_dir
    else:
        return ''


def get_files_dict(tar_dir):
    map_path = os.path.join(tar_dir, map_file)
    try:
        with open(map_path, 'r') as f:
            map_dict = json.load(f)
    except Exception as e:
        map_dict = dict()
        print(e)
    return map_dict


def get_real_name(file_dict, reg_name):
    real_name = file_dict.get(reg_name)
    if not real_name:
        real_name = reg_name
    return real_name


def download_mine(user_name, target):
    real_path = check_file(target, user_name)
    if not real_path:
        return None
    return os.path.split(real_path)
