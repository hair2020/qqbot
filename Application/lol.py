import requests
import json
from graia.application.message.elements.internal import At, Plain,Image
from graia.application.message.chain import MessageChain
from graia.application.group import Group, Member
from graia.application.message.parser.kanata import Kanata
from graia.application.message.parser.signature import FullMatch, RequireParam
from core import *
from lxml import etree
__plugin_name__ = 'lol咨询'
__plugin_usage__ = '输入lol'

bcc = get.bcc()
@bcc.receiver("GroupMessage",dispatchers=[
    Kanata([FullMatch("lol")])])
async def lol(
    message:MessageChain,
    group:Group,
    member:Member,
    app:GraiaMiraiApplication,
): 
    res =requests.get('http://l.zhangyoubao.com/news/')
    res.encoding = 'utf-8'
    sele = etree.HTML(res.text)
    lis = sele.xpath('//li[@class="day"]')
    titles = []
    for li in lis:
        titles.append(li.xpath('a/@title')[0].strip("( )"))
    await app.sendGroupMessage(group,MessageChain.create(
        [Plain(f"{n+1}.{i}\n") for n,i in enumerate(titles)]
    ))


