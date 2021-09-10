from graia.application.entry import *
from graia.application.message.parser.kanata import Kanata
from graia.application.message.parser.signature import *
from core import *
import os
import json
import random
import time
def shui(t):
    if t > 0:
        t = t - t / 8
        if t > 0 and t <= 1:
            t = 1
            return t
        else:
            return int(t - t / 8)
    elif t < 0:
        return int(t/1.5)
g = [773580302,867018573]
jishi = {}
bcc = get.bcc()
@bcc.receiver(GroupMessage,dispatchers= [Kanata([FullMatch('抢劫'), RequireParam('parameter')])])
async def answer(
    message:MessageChain,
    group:Group,
    app:GraiaMiraiApplication,
    member:Member,
    parameter
):
    # 判断字典是否为空
    if jishi:
        # print(jishi)
        if member.id not in jishi.keys():
            jishi[member.id] = time.time()
        # 判断时间差是否超过10秒
        else:
            gap = time.time() - jishi[member.id]
            if gap > 10.0:
                pass
            else:
                await app.sendGroupMessage(group, MessageChain.create([At(member.id), Plain(f'请10秒内抢一次，你太快了'),Image.fromLocalFile('/home/a5203031/qqbot/data/xu.jpg')]))
                return
    else:
        pass
        jishi[member.id] = time.time()

    # print(parameter)# __root__=[At(type='At', target=644661457, display=None)]
    # print(parameter.get(At))# [At(type='At', target=644661457, display=None)]
    # print(parameter.get(At)[0].target)# 644661457
    # print(parameter.has(At))# True or False
    if parameter.has(At):
        if parameter.get(At)[0].target == 2732631493:
            await app.sendGroupMessage(group, MessageChain.create(
                [Plain(f'想什么呢？小老弟')]))
        # 键值[0,0,0]分别对：余额、次数、今日收入
        with open('/home/a5203031/qqbot/data/RobRecord.json', 'r', encoding='utf-8') as f:
            dic = json.loads(f.read())
        # 10秒一次
        jishi[member.id] = time.time()
        # 判断剩余次数
        if dic[str(member.id)][1] == 0:
            await app.sendGroupMessage(group,MessageChain.create([At(member.id),Image.fromLocalFile('/home/a5203031/qqbot/data/xu.jpg'),
                                                                  Plain(f'你今天虚了，不能抢劫了')]))
        else:
            t = random.randint(-20,50)
            beiqq = parameter.get(At)[0].target# 被抢的qq
            beiname = await app.getMember(group.id,beiqq)
            beiname = beiname.name# 被抢的名字
            if dic[str(beiqq)][3] >= 11:
                await app.sendGroupMessage(group, MessageChain.create([Plain(f'大哥这人今天被疯了，换个人吧')]))
                return
            if dic[str(beiqq)][0] <= -100:
                await app.sendGroupMessage(group, MessageChain.create([Plain(f'大哥这人还欠我100多还不上，换个人吧')]))
                return
            with open('data/rob','r',encoding='utf-8') as f1:
                    sens = f1.read().split('\n')
                    sen = random.choice(sens)
            if t > 0:
                t = shui(t)
                await app.sendGroupMessage(group,MessageChain.create([Plain(f'{sen}{beiname}成功!\n税后获得{t}元')]))
                dic[str(member.id)][0] += t# 加余额
                dic[str(member.id)][2] += t# 加收入
                dic[str(beiqq)][0] -= int(t/1.1)
                dic[str(beiqq)][2] -= int(t/1.1)
                dic[str(member.id)][1] -= 1# 减次数
            elif t < 0:
                await app.sendGroupMessage(group,MessageChain.create([Plain(f'{sen}{beiname}失败.\n医药费报销后花了{abs(shui(t))}元')]))
                dic[str(member.id)][0] += t# 减余额
                dic[str(member.id)][2] += t# 减收入
                dic[str(member.id)][1] -= 1
            else:
                await app.sendGroupMessage(group, MessageChain.create([Plain(f'打了个平手，还亲了一口？\n然后俩人一起逛街各花了{99}元')
                                                                          ,Image.fromLocalFile('/home/a5203031/qqbot/data/pingju.png')]))
                dic[str(member.id)][0] -= 99
                dic[str(beiqq)][0] -= 99
                dic[str(member.id)][2] -= 99
                dic[str(beiqq)][2] -= 99
                dic[str(member.id)][1] -= 1  # 减次数
            dic = json.dumps(dic)
            with open('/home/a5203031/qqbot/data/RobRecord.json', 'w', encoding='utf-8') as f2:
                f2.write(dic)
    else:
        await app.sendGroupMessage(group,MessageChain.create([Plain('大哥我迷了，你要抢谁？')
                                                              ,Image.fromLocalFile('/home/a5203031/qqbot/data/robbing.jpg')]))

# # 回本
# bcc = get.bcc()
# @bcc.receiver(GroupMessage,dispatchers= [Kanata([FullMatch('探险')])])
# async def answer(
#     message:MessageChain,
#     group:Group,
#     app:GraiaMiraiApplication,
#     member:Member,
# ):
#
#     luck = random.randint(0,100)
#     bad = random.randint(-100,0)