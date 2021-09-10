# -*- coding = utf -8 -*-
# @Time : 2021/9/1 11:02
# @Author : hair
# -*- coding = utf -8 -*-
# @Time : 2021/4/5 13:02
# @Author : hair
from graia.application.entry import *
from graia.application.message.elements.internal import At, Plain,Image
from graia.application.message.chain import MessageChain
from graia.application.friend import Friend
from core import *
import json
import re
def choice_words(n):
    import random
    with open('frequentWord.txt','r',encoding='utf-8') as f:
        data = f.readlines()
    zh = data[1::2]
    words = data[::2]
    # print(len(zh),len(words))
    index = []
    for i in range(n):
        index.append(random.randint(0,691))

    chinese = ''
    english = ''
    for i in range(n):
        chinese += zh[index[i]] + '\n'
        english += words[index[i]] + '\n'

    return chinese,english
bcc = get.bcc()
@bcc.receiver("FriendMessage")
async def friend_message_listener(message:MessageChain,app: GraiaMiraiApplication, friend: Friend):
    mes = message.asDisplay()
    if mes:
        await app.sendFriendMessage(friend, MessageChain.create([
            Plain("")
        ]))