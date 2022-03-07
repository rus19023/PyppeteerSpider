#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author: StudentCWZ
# @Date: 2022/3/7 10:26 AM
# @File: read_conf.py


# 基本库
import os

# 第三方库
import yaml


def init_conf() -> dict:
    # 字符串拼接
    path = '/'.join(os.path.split(os.path.realpath(__file__))[0].split('/')[:-2]) + '/conf/config.yaml'
    # 获取 cf 对象
    cf = yaml.load(open(path, encoding="utf-8"), Loader=yaml.FullLoader)
    # 返回
    return cf
