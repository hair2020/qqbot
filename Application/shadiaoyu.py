# -*- coding = utf -8 -*-
# @Time : 2021/4/5 13:31
# @Author : hair
import aiohttp
from graia.application.message.elements.internal import At, Plain,Image
from graia.application.message.chain import MessageChain
from graia.application.message.parser.kanata import Kanata
from graia.application.message.parser.signature import *
from core import *
ana = {
    '舔狗语录': 'https://chp.shadiao.app/api.php',
    '骂我': 'https://nmsl.shadiao.app/api.php?level=min&lang=zh_cn',
    '鸡汤': 'https://du.shadiao.app/api.php',
    '祖安语录': 'https://nmsl.shadiao.app/api.php?lang=zh_cn',
}


async def Wget(url: str, headers=None, typ="plain"):
    if not headers:
        headers = {}
    async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(family=2)) as session:
        async with session.get(url, headers=headers) as res:
            if typ == "plain":
                return res.status, await res.text()
            elif typ == "json":
                return res.status, await res.json()
            else:
                raise ValueError("Unknown type:", typ)

bcc = get.bcc()
@bcc.receiver("GroupMessage",
              dispatchers= [Kanata([FullMatch('骂'), OptionalParam('para')])])
async def mata(app: GraiaMiraiApplication,
                 group: Group,
                 message: MessageChain,
                 member: Member,
                 para):
    # @谁user是谁，否则是自己
    #user = para.get(At)[0].target if para and para.has(At) else member.id
    user = para.get(At)[0].target if para and para.has(At) else 0
    if user != 0:
        if user == 644661457:
            await app.sendGroupMessage(group, MessageChain.create([
                At(user),
                Plain('咱不理他')
            ]))
        elif user == 2732631493:
            await app.sendGroupMessage(group, MessageChain.create([
                At(member.id),
                Plain('你会自己骂自己吗？笨蛋')
            ]))
        else:
            await app.sendGroupMessage(group, MessageChain.create([
                At(user),
                Plain(text=f'{(await Wget(ana["骂我"]))[1]}')
            ]))
    else:
        return
bcc = get.bcc()
@bcc.receiver("GroupMessage",
              dispatchers= [Kanata([FullMatch('舔'), OptionalParam('para')])])
async def mata(app: GraiaMiraiApplication,
                 group: Group,
                 message: MessageChain,
                 member: Member,
                 para):
    # @谁user是谁，否则是发消息的人
    #user = para.get(At)[0].target if para and para.has(At) else member.id
    user = para.get(At)[0].target if para and para.has(At) else 0
    if user != 0:
        await app.sendGroupMessage(group, MessageChain.create([
            At(user),
            Plain(text=f'{(await Wget(ana["舔狗语录"]))[1]}')
        ]))
@bcc.receiver("GroupMessage",
              dispatchers= [Kanata([FullMatch('夸'), OptionalParam('para')])])
async def mata(app: GraiaMiraiApplication,
                 group: Group,
                 message: MessageChain,
                 member: Member,
                 para):
    # @谁user是谁，否则是发消息的人
    #user = para.get(At)[0].target if para and para.has(At) else member.id
    user = para.get(At)[0].target if para and para.has(At) else 0
    if user != 0:
        await app.sendGroupMessage(group, MessageChain.create([
            At(user),
            Plain(text=f'{(await Wget(ana["舔狗语录"]))[1]}')
        ]))
bcc = get.bcc()
@bcc.receiver("GroupMessage",
              dispatchers= [Kanata([FullMatch('教育'), OptionalParam('para')])])
async def mata(app: GraiaMiraiApplication,
                 group: Group,
                 message: MessageChain,
                 member: Member,
                 para):
    # @谁user是谁，否则是
    #user = para.get(At)[0].target if para and para.has(At) else member.id
    user = para.get(At)[0].target if para and para.has(At) else 0
    if user != 0:
        await app.sendGroupMessage(group, MessageChain.create([
            At(user),
            Plain(text=f'{(await Wget(ana["鸡汤"]))[1]}')
        ]))
