# -*- coding = utf -8 -*-
# @Time : 2021/3/16 20:33
# @Author : hair
import requests
from graia.application.message.elements.internal import At, Plain
from graia.application.message.chain import MessageChain
from graia.application.message.parser.kanata import Kanata
from graia.application.message.parser.signature import FullMatch, RequireParam
from core import *
from lxml import etree
__plugin_name__ = '百度百科'
__plugin_usage__ = '百科'

bcc = get.bcc()
@bcc.receiver("GroupMessage",dispatchers=[
    Kanata([FullMatch("百科"),RequireParam(name='aim')])
])
async def cl(
    message:MessageChain,
    group:Group,
    member:Member,
    app:GraiaMiraiApplication,
    aim:MessageChain
):
    # aim = input()

    url = f'https://baike.baidu.com/item/{aim.asDisplay()}'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'
    }
    res = requests.get(url=url, headers=headers).text
    # print(res.apparent_encoding) #utf-8
    data = etree.HTML(res)
    # 获取文本内容 返回字符串列表
    listdata = data.xpath('//div[contains(@class,"lemma-summary") or contains(@class,"lemmaWgt-lemmaSummary")]//text()')
    # 过滤数据，去掉空白
    if listdata == []:
        await app.sendGroupMessage(group,MessageChain.create([
            Plain('你是外星人吧，找不到这词条'),
            At(member.id)
        ]))
    else:
        Listdata = [item.strip('\n ') for item in listdata]
        # 将字符串列表连成字符串并返回
        enddata = ''.join(Listdata)
        # print(enddata)
        await app.sendGroupMessage(group,MessageChain.create([
            Plain(enddata)
        ]))

