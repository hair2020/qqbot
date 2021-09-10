# -*- coding = utf -8 -*-
# @Time : 2021/3/23 12:35
# @Author : hair
from graia.application.message.elements.internal import At, Plain,Image
from graia.application.message.chain import MessageChain
from graia.application.group import Group, Member
from graia.application.message.parser.kanata import Kanata
from graia.application.message.parser.signature import *
from core import *
import random
__plugin_name__ = '摸头'
__plugin_usage__ = '摸头@。。'

bcc = get.bcc()
@bcc.receiver("GroupMessage",
              dispatchers= [Kanata([FullMatch('摸头'), OptionalParam('para')])])

async def petpet(app: GraiaMiraiApplication,
                 group: Group,
                 message: MessageChain,
                 member: Member,
                 para):
    # @谁user是谁，否则是自己
    #user = para.get(At)[0].target if para and para.has(At) else member.id
    user = para.get(At)[0].target if para and para.has(At) else member.id
    print(para.get(At))  # [At(type='At', target=644661457, display=None)]
    others = ['  好家伙，你的头上好多油','  哇，好头','  哇，圆啊','  好家伙，秃了','  有病吧，你叫什么']
    my = ['  放心吧，我不会的', '  这头不会秃']
    o = random.choice(others)
    m = random.choice(my)
    if user == int('644661457'):
        await app.sendGroupMessage(group, MessageChain.create([
            At(user),
            Plain(m)
        ]))
    else:
        await app.sendGroupMessage(group, MessageChain.create([
            At(user),
            Plain(o)
        ]))