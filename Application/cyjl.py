import requests
import json
from graia.application.message.elements.internal import At, Plain,Image
from graia.application.message.chain import MessageChain
from graia.application.group import Group, Member
from graia.application.message.parser.kanata import Kanata
from graia.application.message.parser.signature import FullMatch, RequireParam
from core import *
import random
import hashlib
__plugin_name__ = '成语接龙'
__plugin_usage__ = '输入jl'
def readData(filepath):
        fp = open(filepath, 'r', encoding='utf-8')
        idiom_data = {}
        valid_idioms = {}
        for line in fp.readlines():
            line = line.strip()
            if not line: continue
            item = line.split('\t')
            if len(item) != 3: continue
            if item[0][0] not in idiom_data:
                idiom_data[item[0][0]] = [item]
            else:
                idiom_data[item[0][0]].append(item)
            valid_idioms[item[0]] = item[1:]
        return idiom_data, valid_idioms
idiom_data,valid_idioms = readData(r"/home/a5203031/qqbot/data/chengyu.txt")
def isvalid(idiom):
        return (idiom in valid_idioms)
bcc = get.bcc()

# 接龙
@bcc.receiver("GroupMessage",dispatchers=[
    Kanata([FullMatch("接龙"),RequireParam(name='cyjl')])
])
async def cyjl(
    message:MessageChain,
    member:Member,
    group:Group,
    app:GraiaMiraiApplication,
    cyjl:MessageChain
):
    ai_as = None
    idiom = cyjl.asDisplay()
    if len(idiom) < 4:
        await app.sendGroupMessage(group, MessageChain.create([Plain("你识数？")]))
    else:
        if idiom[-1] in idiom_data:
            answers = idiom_data[idiom[-1]]
            answer = random.choice(answers)
            ai_as = answer.copy()
            await app.sendGroupMessage(group,MessageChain.create([Plain(f"{ai_as[0]}")]))
        else:
            await app.sendGroupMessage(group,MessageChain.create([Plain("接不了 爬！")]))
            return

# 查意思
@bcc.receiver("GroupMessage",dispatchers=[
    Kanata([FullMatch("成语"),RequireParam(name='mean')])
])
async def cyjl(
    message:MessageChain,
    member:Member,
    group:Group,
    app:GraiaMiraiApplication,
    mean:MessageChain
):
    ai_as = None
    idiom = mean.asDisplay()
    if len(idiom) < 4:
        await app.sendGroupMessage(group, MessageChain.create([Plain("你识数？")]))
    else:

        if idiom in valid_idioms:
            answer = valid_idioms[idiom]
            ai_as = answer.copy()
            await app.sendGroupMessage(group,MessageChain.create([Plain(f"{ai_as[1]}")]))
        else:
            await app.sendGroupMessage(group,MessageChain.create([Plain("你有文化吗？")]))
            return
    
