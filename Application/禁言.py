# -*- coding = utf -8 -*-
# @Time : 2021/3/30 13:04
# @Author : hair
from graia.application.entry import *
from graia.application.message.parser.kanata import Kanata
from graia.application.message.parser.signature import *
from core import *
bcc = get.bcc()
@bcc.receiver('GroupMessage',dispatchers= [Kanata([FullMatch('禁言'), RequireParam('parameter')])])#禁言
async def auto_ban(app: GraiaMiraiApplication,
                   group: Group,
                   message: MessageChain,
                   member:Member,
                   parameter):
    if member.id == 644661457:
        if parameter.has(At):
            beijinqq = parameter.get(At)[0].target
            try:
                await app.mute(group, beijinqq, 600)
                await app.sendGroupMessage(group, MessageChain.create([
                    Plain('遵命！')]))
            except PermissionError:
                await app.sendGroupMessage(group, MessageChain.create([
                    Plain('对不起，我没权限')]))

# app = get.app()
# @bcc.receiver('GroupRecallEvent')#撤回
# async def recall.txt(event:GroupRecallEvent):
#     await app.sendGroupMessage(event.dict()['group']['id'], MessageChain.create([
#         Plain('撤回？')]))







