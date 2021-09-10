import requests
import json
from graia.application.message.elements.internal import At, Plain,Image
from graia.application.message.chain import MessageChain
from graia.application.group import Group, Member
from graia.application.message.parser.kanata import Kanata
from graia.application.message.parser.signature import FullMatch, RequireParam
from core import *
from lxml import etree
import os
import random
import aiohttp

__plugin_name__ = 'pic'
__plugin_usage__ = '输入关键词'

bcc = get.bcc()

@bcc.receiver("GroupMessage")
async def st(
    message:MessageChain,
    app:GraiaMiraiApplication,
    group:Group,
    member:Member
    ):
    if message.asDisplay().startswith("价值观"):
        await app.sendGroupMessage(group, MessageChain.create(
            [Image.fromLocalFile("/home/a5203031/qqbot/data/jzg.jpg")]
        ))
    if message.asDisplay()==("我太爱看了") or message.asDisplay() == ("我爱看"):
        f = open('/home/a5203031/qqbot/data/gjc','r')
        list_all = f.readlines()
        f.close()
        ai20 = list_all[7].strip()
        if str(group.id) in ai20:
            dirs1 = os.listdir("/home/a5203031/qqbot/data/C2C")
            dirs1 = list(map(lambda a:"/home/a5203031/qqbot/data/C2C/"+a,dirs1))# map(function, iterable, ...)
            if message.asDisplay().startswith("我太爱看了"):
                for _ in range(3):
                    await app.sendGroupMessage(group,MessageChain.create([Image.fromLocalFile(random.choice(dirs1))]))

            if message.asDisplay().startswith("我爱看"):
                await app.sendGroupMessage(group,MessageChain.create(
                    [Plain('你爱看'),Image.fromLocalFile(random.choice(dirs1))]
                ))

    # dirs3 = os.listdir("D:\pic\sexy")
    # dirs3 = list(map(lambda a:"D:/pic/sexy/"+a,dirs3))
    # if message.asDisplay().startswith("3"):
    #     await app.sendGroupMessage(group,MessageChain.create(
    #         [Image.fromLocalFile(random.choice(dirs3))]
    #     ))
    # dirs = [dirs1,dirs2]
    # dirs_fin = random.choice(dirs)
    # if message.asDisplay().startswith(""):
    #     await app.sendGroupMessage(group,MessageChain.create(
    #         [Image.fromLocalFile(random.choice(dirs_fin))]
    #     ))