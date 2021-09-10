from graia.application.entry import *
from graia.application.message.parser.kanata import Kanata
from graia.application.message.parser.signature import *
from core import *
import os
import json
import time
jishi = {}
bcc = get.bcc()
@bcc.receiver(GroupMessage,dispatchers= [Kanata([FullMatch('查询'), RequireParam('parameter')])])
async def answer(
    message:MessageChain,
    group:Group,
    app:GraiaMiraiApplication,
    member:Member,
    parameter : MessageChain
):
    # 判断字典是否为空
    if jishi:
        # print(jishi)
        if member.id not in jishi.keys():
            jishi[member.id] = time.time()
        # 判断时间差是否超过60秒
        else:
            gap = time.time() - jishi[member.id]
            if gap > 60.0:
                pass
            else:
                await app.sendGroupMessage(group, MessageChain.create([At(member.id), Plain(f'请60秒内查一次，太快受不了')]))
                return
    else:
        pass
        jishi[member.id] = time.time()
    # 秒一次
    jishi[member.id] = time.time()
    with open('/home/a5203031/qqbot/data/RobRecord.json', 'r', encoding='utf-8') as f:
        dic = json.loads(f.read())
    if parameter.asDisplay() == '余额':
        await app.sendGroupMessage(group, MessageChain.create([Plain(f'您的账户余额为：{dic[str(member.id)][0]}元。')]))
    elif parameter.asDisplay() == '次数':

        await app.sendGroupMessage(group, MessageChain.create([Plain(f'还能再抢{dic[str(member.id)][1]}次。')]))
    elif parameter.asDisplay() == '收入':

        if dic[str(member.id)][2] >= 0:
            await app.sendGroupMessage(group, MessageChain.create([Plain(f'今天非法收入{dic[str(member.id)][2]}元。')]))
        else:
            await app.sendGroupMessage(group, MessageChain.create([Plain(f'今天被抢了{dic[str(member.id)][2]}元。')]))
    elif parameter.asDisplay() == '更新':
        a = '查询 + 余额、次数（每人每天抢10次）、收入、黑老大、小老弟\n 次日会更新次数 \n 一些小细节，预防顶不住'
        await app.sendGroupMessage(group, MessageChain.create([Plain(a)]))
    elif parameter.asDisplay() == '黑老大':
        # 倒序排余额
        rank = sorted(dic.items(), key=lambda d: d[1][0], reverse=True)
        names = []# 存名字、余额
        print(rank[0][0])
        for i in range(3):
            name = await app.getMember(867018573, int(rank[i][0]))
            names.append(f'{name.name}：{rank[i][1][0]}元')

        text = '\n'.join(names)
        await app.sendGroupMessage(group, MessageChain.create([Plain(f'{text}')]))
    elif parameter.asDisplay() == '小老弟':
        rank = sorted(dic.items(), key=lambda d: d[1][0], reverse=False)
        name1 = await app.getMember(867018573, int(rank[0][0]))
        await app.sendGroupMessage(group, MessageChain.create([Plain(f'目前被抢最多的小老弟是‘{name1.name}’'),Image.fromLocalFile('/home/a5203031/qqbot/data/xianqi.jpg')]))



