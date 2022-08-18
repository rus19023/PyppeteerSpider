PyppeteerSpider features
Use Pyppeteer to crawl related movie information
Use mongodb to store data
Ready to use
First clone the code
git clone git@github.com:StudentCWZ/PyppeteerSpider.git
Go into the PyppeteerSpider folder
cd PyppeteerSpider
run as usual
Install and configure MongoDB
It is possible to install Mongodb locally, start Mongodb with Docker, and remotely Mongodb, as long as it can be connected normally.
Here it is recommended to start Mongodb with Docker
Install dependencies
It is strongly recommended to use Conda or virtualenv to create a virtual environment. The Python version is not lower than 3.6, and 3.9 is used here.
Then pip install the dependencies:
pip3 install -r requirements.txt
Configure Pyppeteer
pip install pyppeteer (the process of installing dependencies has been installed)
View the browser version that needs to be downloaded chromium
import pyppeteer.chromium_downloader
print(pyppeteer.chromium_downloader.chromiumExecutable.get("mac"))
The output is as follows (Mac platform)
There will be a number circled in red in the returned address and path, remember this number
Open Taobao mirror
Select the relevant platform and download according to the version
View the jump download link, copy the download link
Then find the chromium_downloader.py file in pyppeteer in python's library management folder site-packages and modify the following code
downloadURLs = {
    'linux': f'{BASE_URL}/Linux_x64/{REVISION}/chrome-linux.zip',
    'mac': f'{BASE_URL}/Mac/{REVISION}/chrome-mac.zip',
    'win32': f'{BASE_URL}/Win/{REVISION}/{windowsArchive}.zip',
    'win64': f'{BASE_URL}/Win_x64/{REVISION}/{windowsArchive}.zip',
}
Modified as follows:
downloadURLs = {
    'linux': f'{BASE_URL}/Linux_x64/{REVISION}/chrome-linux.zip',
    'mac': f'https://cdn.npmmirror.com/binaries/chromium-browser-snapshots/Mac/588429/chrome-mac.zip',
    'win32': f'{BASE_URL}/Win/{REVISION}/{windowsArchive}.zip',
    'win64': f'{BASE_URL}/Win_x64/{REVISION}/{windowsArchive}.zip',
}
save
Initialize pyppeteer
pyppeteer-install
run the project
python3 main.py
Article citations
pyppeteer install
Cui Qingcai Blog






# PyppeteerSpider
## PyppeteerSpider 功能
- 利用 Pyppeteer 爬取相关电影信息
- 使用 mongodb 对数据进行存储

## 使用准备
1. 首先克隆代码
```
git clone git@github.com:StudentCWZ/PyppeteerSpider.git
```
2. 进入 PyppeteerSpider 文件夹
```
cd PyppeteerSpider
```

## 常规方式运行
### 安装和配置 Mongodb
1. 本地安装 Mongodb、Docker 启动 Mongodb、远程 Mongodb 都是可以的，只要能正常连接使用即可。
2. 这里建议用 Docker 启动 Mongodb

### 安装依赖包
1. 这里强烈推荐使用 Conda 或 virtualenv 创建虚拟环境，Python 版本不低于 3.6，这里使用的是 3.9。
2. 然后 pip 安装依赖即可：
```
pip3 install -r requirements.txt
```

### 配置 Pyppeteer
1. pip 安装 pyppeteer(安装依赖包过程已安装)
2. 查看需要下载 chromium 浏览器版本
```
import pyppeteer.chromium_downloader
print(pyppeteer.chromium_downloader.chromiumExecutable.get("mac"))
```
3. 输出结果如下(Mac 平台)
![](/Users/cuiweizhi/Downloads/Snip20220307_1.png)
4. 返回的地址和路径中会有红色圈起来的数字，记住这个数字
5. 打开淘宝镜像[](https://registry.npmmirror.com/binary.html?path=chromium-browser-snapshots/)
6. 选取相关平台，根据版本下载
7. 查看跳转的下载链接，复制下载链接
8. 然后找到 python 的库管理文件夹 site-packages 中 pyppeteer 中的 chromium_downloader.py 文件并修改以下代码
```
downloadURLs = {
    'linux': f'{BASE_URL}/Linux_x64/{REVISION}/chrome-linux.zip',
    'mac': f'{BASE_URL}/Mac/{REVISION}/chrome-mac.zip',
    'win32': f'{BASE_URL}/Win/{REVISION}/{windowsArchive}.zip',
    'win64': f'{BASE_URL}/Win_x64/{REVISION}/{windowsArchive}.zip',
}
```
9. 修改后如下：
```
downloadURLs = {
    'linux': f'{BASE_URL}/Linux_x64/{REVISION}/chrome-linux.zip',
    'mac': f'https://cdn.npmmirror.com/binaries/chromium-browser-snapshots/Mac/588429/chrome-mac.zip',
    'win32': f'{BASE_URL}/Win/{REVISION}/{windowsArchive}.zip',
    'win64': f'{BASE_URL}/Win_x64/{REVISION}/{windowsArchive}.zip',
}
```
10. 保存
11. 初始化 pyppeteer
```
pyppeteer-install
```

## 运行项目
```angular2html
python3 main.py
```

## 文章引用
- pyppeteer 安装[](https://www.icode9.com/content-4-968162.html)
- 崔庆才博客[](https://cuiqingcai.com/archives/)
