from graia.application.message.elements.internal import At, Plain,Image
from graia.application.message.chain import MessageChain
import graia.application.message.elements.internal as Elements
from graia.application.group import Group, Member
from graia.application.message.parser.kanata import Kanata
from graia.application.message.parser.signature import FullMatch, RequireParam
from core import *

__plugin_name__ = '回答'
__plugin_usage__ = '特殊词汇'

# with open('/home/a5203031/qqbot/data/gjc', 'r', encoding='utf-8') as f1:
#     list_all = f1.readlines()

bcc = get.bcc()
@bcc.receiver("GroupMessage")
async def answer(
    message:MessageChain,
    group:Group,
    app:GraiaMiraiApplication,
    member:Member
):
    list_all = ['sb SB 傻逼 臭猪 弟弟 小丑\n', '玩手机 不交手机 请假 不去了 不上自习 查人了吗\n', '哈哈哈哈哈哈 蛤蛤蛤蛤 xswl\n', '不知道 ？？？ ??? 啥\n', '群主 警告 危\n', '求 dbq 错了 对不起 原谅\n', '1038201434 876117114 773580302 屏蔽猪叫问号\n', '867018573 876117114发送班级图片\n', '764839290 876117114 1038201434 867018573撤回信息\n']

    badword = list_all[0].strip().split(' ')
    sensitive = list_all[1].strip().split(' ')
    laugh = list_all[2].strip().split(' ')
    why = list_all[3].strip().split(' ')
    jiuzhe = list_all[4].strip().split(' ')
    pa = list_all[5].strip().split(' ')
    negative_group = list_all[6].strip()
    mes = message.asDisplay()
    for i in pa:
        if i in mes:
            await app.sendGroupMessage(group, MessageChain.create(
                [Plain("爬！")]
            ))
    for i in badword:
        if i in mes:
            await app.sendGroupMessage(group, MessageChain.create(
                [Plain("没错，我同意！")]
            ))
    for i in sensitive:
        if i in mes:
            await app.sendGroupMessage(group, MessageChain.create(
                [Plain("马上到509找我")]
            ))
    for i in laugh:
        if i in mes:
            if str(group.id) not in negative_group:
                await app.sendGroupMessage(group, MessageChain.create(
                    [Plain("猪叫？")]
                ))
    for i in why:
        if i in mes:
            if str(group.id) not in negative_group:
                await app.sendGroupMessage(group, MessageChain.create(
                    [Plain("就你？多")]
                ))
    for i in jiuzhe:
        if i in mes:
            await app.sendGroupMessage(group, MessageChain.create(
                [Plain("就这？")]
            ))
