#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author: StudentCWZ
# @Date: 2022/3/7 10:27 AM
# @File: spider.py


# 第三方库
from pyppeteer import launch
from pyppeteer.errors import TimeoutError

# 自定义库
from src.utils import read_conf as rc
from src.utils import mongo
from src.utils import log


# 全局变量
logger = log.new_logger(__name__)
browser, tab = None, None


async def init():
    # 获取 mongodb 相关配置信息
    mongo_host = rc.init_conf()['mongo']['host']
    mongo_db = rc.init_conf()['mongo']['db']
    mongo_collection = rc.init_conf()['mongo']['collection']
    # 获取 index_url
    index_url = rc.init_conf()['url']['index_url']
    # 获取 request 对象信息
    timeout = int(rc.init_conf()['request']['timeout'])
    window_width = int(rc.init_conf()['request']['window_width'])
    window_height = int(rc.init_conf()['request']['window_height'])
    # 获取 page 相关信息
    total_page = int(rc.init_conf()['page']['total_page'])
    # 返回
    return mongo_host, mongo_db, mongo_collection, index_url, timeout, window_width, window_height, total_page


async def init_browser(window_width: int, window_height: int):
    global browser, tab
    # 获取 browser
    browser = await launch(headless=False, args=['--disable-infobars', '--window-size={window_width}, {window_height}'])
    # 获取 tab
    tab = await browser.newPage()
    await tab.setViewport({'width': window_width, 'height': window_height})


async def scrape_page(url: str, timeout: int, selector):
    # 输出日志
    logger.info('scraping %s', url)
    # 捕获异常
    try:
        await tab.goto(url)
        await tab.waitForSelector(selector, options={'timeout': timeout * 1000})
    except TimeoutError:
        logger.error('error occurred while scraping %s', url, exc_info=True)


async def scrape_index(index_url: str, timeout: int, page: int):
    url = index_url.format(page=page)
    await scrape_page(url, timeout, '.item .name')


async def parse_index():
    return await tab.querySelectorAllEval('.item .name', 'nodes => nodes.map(node => node.href)')


async def scrape_detail(url: str, timeout: int):
    await scrape_page(url, timeout, 'h2')


async def parse_detail():
    url = tab.url
    name = await tab.querySelectorEval('h2', 'node => node.innerText')
    categories = await tab.querySelectorAllEval('.categories button span', 'nodes => nodes.map(node => node.innerText)')
    cover = await tab.querySelectorEval('.cover', 'node => node.src')
    score = await tab.querySelectorEval('.score', 'node => node.innerText')
    drama = await tab.querySelectorEval('.drama p', 'node => node.innerText')
    return {
        'url': url,
        'name': name,
        'categories': categories,
        'cover': cover,
        'score': score,
        'drama': drama
    }


async def run():
    # 初始化相关配置
    host, db, collection, index_url, timeout, window_width, window_height, total_page = await init()
    # 连接 mongodb 数据库
    col = mongo.conn_mongo(host, db, collection)
    # 初始化浏览器
    await init_browser(window_width, window_height)
    # 捕获异常
    try:
        # 遍历
        for page in range(1, total_page + 1):
            await scrape_index(index_url, timeout, page)
            detail_urls = await parse_index()
            for detail_url in detail_urls:
                await scrape_detail(detail_url, timeout)
                detail_data = await parse_detail()
                await mongo.save_data(col, detail_data)
    finally:
        await browser.close()
