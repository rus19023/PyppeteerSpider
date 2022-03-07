#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author: StudentCWZ
# @Date: 2022/3/7 10:24 AM
# @File: log.py


# 基本库
import logging


def new_logger(name: str) -> logging.Logger:
    # 输出格式配置
    fmt = '%(asctime)s-%(levelname)s:%(message)s'
    # 创建 logger
    logger = logging.getLogger(name)
    # 清空 handlers
    logger.handlers = list()
    # 设置日志级别
    logger.setLevel(logging.INFO)
    # 设置日志格式
    format_str = logging.Formatter(fmt=fmt)
    # 用于输出到控制台的 handler
    ch = logging.StreamHandler()
    # 设置 ch 的日志级别
    ch.setLevel(logging.INFO)
    # 设置 ch 的格式
    ch.setFormatter(fmt=format_str)
    # 将 logger 添加到 handler 里面
    logger.addHandler(ch)
    # 返回 logger
    return logger
