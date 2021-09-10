# -*- coding = utf -8 -*-
# @Time : 2021/3/25 16:39
# @Author : hair
import requests
from graia.application.message.elements.internal import At, Plain,Image
from graia.application.message.chain import MessageChain
from graia.application.group import Group, Member
from graia.application.message.parser.kanata import Kanata
from graia.application.message.parser.signature import FullMatch, RequireParam
from core import *
__plugin_name__ = '金山每日一句'
__plugin_usage__ = '每日一句'

bcc = get.bcc()
@bcc.receiver("GroupMessage",dispatchers=[
    Kanata([FullMatch("每日一句")])
])
async def fy1(
    message:MessageChain,
    group:Group,
    member:Member,
    app:GraiaMiraiApplication,
    han:MessageChain
):
    head = {'user-agent': 'firefox'}
    url = "http://open.iciba.com/dsapi/"
    res = requests.get(url,head)
    eng = res.json()['content']
    tran = res.json()['note']
    pic = res.json()['picture']
    await app.sendGroupMessage(group, MessageChain.create(
        [Image.fromNetworkAddress(pic),
        Plain(f'{eng}\n{tran}')]
    ))