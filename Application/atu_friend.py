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
import requests
__plugin_name__ = '回答好友'
__plugin_usage__ = '无'

ana = {
    '舔狗语录': 'https://chp.shadiao.app/api.php',
    '骂': 'https://nmsl.shadiao.app/api.php?level=min&lang=zh_cn',
    '鸡汤': 'https://du.shadiao.app/api.php',
    '祖安语录': 'https://nmsl.shadiao.app/api.php?lang=zh_cn',
}
def rq(url):
    res = requests.get(url).text
    return res


bcc = get.bcc()
@bcc.receiver("FriendMessage")
async def friend_message_listener(message:MessageChain,app: GraiaMiraiApplication, friend: Friend):
    mes = message.asDisplay()
    if mes not in ana.keys():
        await app.sendFriendMessage(friend, MessageChain.create([
            Plain("只服务3人及以上的群,带我进去吧,群内发送help查看功能，有疑问咨询644661457")
        ]))
    else:
        await app.sendFriendMessage(friend,MessageChain.create([Plain(text=f'{rq(ana[message.asDisplay()])}')]))
    if mes.startswith('加'):
        if '次' in mes:
            n = re.findall('\d+',mes)
            with open('/home/a5203031/qqbot/data/RobRecord.json', 'r', encoding='utf-8') as f:
                dic = json.loads(f.read())
            dic = dict(dic)
            dic[str(friend.id)][1] += int(n[0])
            now = dic[str(friend.id)][1]
            dic = json.dumps(dic)
            with open('/home/a5203031/qqbot/data/RobRecord.json','w',encoding='utf-8') as f1:
                f1.write(dic)
            await app.sendFriendMessage(friend,MessageChain.create([Plain(f'添加成功！还有{now}次')]))
    if mes.startswith('加钱'):
        # 加钱qq空格金额
        n = re.findall('\d+',mes)# [qq,金额]
        with open('/home/a5203031/qqbot/data/RobRecord.json','r',encoding='utf-8') as f:
            dic = json.loads(f.read())
            dic = dict(dic)
            dic[n[0]][0] += int(n[1])
            now = dic[n[0]][0]
            dic = json.dumps(dic)
        with open('/home/a5203031/qqbot/data/RobRecord.json','w',encoding='utf-8') as f1:
            f1.write(dic)
        await app.sendFriendMessage(friend,MessageChain.create([Plain(f'添加成功！{n[0]}有{now}元')]))
    if mes.startswith('减钱'):
        # 加钱qq空格金额
        n = re.findall('\d+',mes)# [qq,金额]
        with open('/home/a5203031/qqbot/data/RobRecord.json','r',encoding='utf-8') as f:
            dic = json.loads(f.read())
            dic = dict(dic)
            dic[n[0]][0] -= int(n[1])
            now = dic[n[0]][0]
            dic = json.dumps(dic)
        with open('/home/a5203031/qqbot/data/RobRecord.json','w',encoding='utf-8') as f1:
            f1.write(dic)
        await app.sendFriendMessage(friend,MessageChain.create([Plain(f'添加成功！{n[0]}有{now}元')]))
    if mes.startswith('全部加钱'):
        # 全部加钱金额
        n = re.findall('\d+',mes)# [金额]
        with open('/home/a5203031/qqbot/data/RobRecord.json','r',encoding='utf-8') as f:
            dic = json.loads(f.read())
            dic = dict(dic)
            it = list(dic.items())
            for i in range(len(dic)):
                it[i][1][0] += int(n[0])
            dic = json.dumps(dic)
        with open('/home/a5203031/qqbot/data/RobRecord.json','w',encoding='utf-8') as f1:
            f1.write(dic)
        await app.sendFriendMessage(friend,MessageChain.create([Plain('添加成功！')]))
# 自动加好友
@bcc.receiver("NewFriendRequestEvent")
async def accept(event:NewFriendRequestEvent):
    await event.accept()