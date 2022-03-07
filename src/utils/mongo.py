#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author: StudentCWZ
# @Date: 2022/3/7 10:25 AM
# @File: mongo.py


# 第三方库
import motor
from motor.motor_asyncio import AsyncIOMotorClient

# 自定义库
from src.utils import log

# 创建 logger 对象
logger = log.new_logger(__name__)


def conn_mongo(host: str, db: str, collection: str) -> motor.motor_asyncio.AsyncIOMotorCollection:
    # 创建 mongodb 连接对象
    client = AsyncIOMotorClient(host)
    db = client[db]
    col = db[collection]
    return col


async def save_data(collection: motor.motor_asyncio.AsyncIOMotorCollection, data: dict):
    logger.info('saving data: %s', data)
    if data:
        return await collection.update_one(
            {
                'name': data.get('name')
            }, {
                '$set': data
            }, upsert=True
        )
