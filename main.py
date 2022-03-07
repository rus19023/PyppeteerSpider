#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2022/3/5 11:34 PM
# @File : main.py


# 第三方库
import asyncio

# 自定义库
from src.core import spider
from src.utils import log


async def main():
    # 创建 logger 对象
    logger = log.new_logger(__name__)
    logger.info('start crawler service ...')
    await spider.run()
    logger.info('exit crawler service ...')


if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(main())
