
from graia.application.message.elements.internal import At, Plain,Image
from graia.application.message.chain import MessageChain
from graia.application.group import Group, Member
from graia.application.message.parser.kanata import Kanata
from graia.application.message.parser.signature import FullMatch, RequireParam
from core import *
import requests
import json
import random

__plugin_name__ = 'st'
__plugin_usage__ = '我要冲'

bcc = get.bcc()
@bcc.receiver("GroupMessage",
              headless_decoraters = [judge.config_check(__name__)],)
async def st(
    message:MessageChain,
    group:Group,
    app:GraiaMiraiApplication,
    member:Member
):
    mes = message.asDisplay()
    if '冲' in mes:
        if mes == '轻冲':
            url = 'https://el-bot-api.vercel.app/api/setu'
            res = requests.get(url)
            result = res.json()
            image = result['url']
            await app.sendGroupMessage(group, MessageChain.create(
                [Image.fromNetworkAddress(image)]
            ))
        if mes == '我要冲':
            fp = open('/home/a5203031/qqbot/data/urls.txt', 'r')
            # fp = open(r'D:\hair\pythonProject\测试\urls.txt', 'r',encoding='utf-8')
            ci = fp.read()
            fp.close()
            image = ci.split('\n')
            await app.sendGroupMessage(group, MessageChain.create(
                [Image.fromNetworkAddress(random.choice(image))]
            ))
        if mes == '我要冲爆':
            fp = open('/home/a5203031/qqbot/data/urls.txt', 'r')
            # fp = open(r'D:\hair\pythonProject\测试\urls.txt', 'r',encoding='utf-8')
            ci = fp.read()
            fp.close()
            image = ci.split('\n')
            for i in range(6):
                await app.sendGroupMessage(group, MessageChain.create(
                    [Image.fromNetworkAddress(random.choice(image))]
                ))
        if mes == '我要看着冲':
            fp = open('/home/a5203031/qqbot/data/liao.txt', 'r')
            # fp = open(r'D:\hair\pythonProject\测试\urls.txt', 'r',encoding='utf-8')
            v = fp.read()
            fp.close()
            vv = random.choice(v.split('\n'))
            await app.sendGroupMessage(group, MessageChain.create(
                    [Plain(f'希望人没事\n{vv}')]
                ))