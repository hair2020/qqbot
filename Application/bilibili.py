from graia.application import GraiaMiraiApplication
from graia.application.event.messages import GroupMessage
from graia.application.message.elements.internal import Plain, Image
from graia.application.message.chain import MessageChain
from graia.application.group import Group, Member
from graia.application.message.parser.signature import FullMatch, RequireParam
from graia.application.message.parser.kanata import Kanata
from core import get

import re
import aiohttp
from bs4 import BeautifulSoup
import requests
__plugin_name__ = 'B站搜索'
__plugin_usage__ = '比站xx'

bcc = get.bcc()
@bcc.receiver("GroupMessage",dispatchers=[
    Kanata([FullMatch("比站"),RequireParam(name='message')])
])
async def video_info(app: GraiaMiraiApplication,
                     group: Group,
                     message: MessageChain,
                     member:Member):
    head = {'user-agent': 'firefox'}
    shuru = message.asDisplay()
    url = f"https://search.bilibili.com/all?keyword={shuru}&from_source=nav_suggest_new"
    res = requests.get(url, head).content.decode('utf-8')
    # data = res.text
    # fp = open('./data/bili.txt','w',encoding='utf-8')
    # fp.write(res)
    alldata = BeautifulSoup(res, 'lxml')
    # 提取网址和标题
    url_title = alldata.select('.img-anchor')
    # urls = alldata.find_all('li', {'class': 'video-item matrix'}) #li标签下 class为...的内容

    # 提取图片 标签下为空？？？
    # image = alldata.select('.lazy-img > img')
    # print(image)

    # 提取网址
    if len(url_title)<3:
        await app.sendGroupMessage(group, MessageChain.create([
            Plain('搜啥玩意呢？三个凑不齐')
        ]))
    else:
        urls = []
        for i in range(3):
            complete = 'https:' + url_title[i]['href']
            urls.append(complete)
        # 提取图片
        image_url = []
        for i in urls:
            res = requests.get(i, head)
            res.encoding = res.apparent_encoding
            soups = BeautifulSoup(res.text, "html.parser")
            target = soups.find("meta", itemprop="thumbnailUrl")
            image_url.append(target["content"])

        # 提取标题
        title = []
        for j in range(3):
            title.append(url_title[j]['title'])

        ok = dict(zip(title, urls)).items()

        for index, (k, v) in enumerate(ok):
            # print(f'{k} \n {v}')
            await app.sendGroupMessage(group, MessageChain.create([
            Image.fromNetworkAddress(image_url[index]),
            Plain(f'{k} \n {v}'),
            ]))