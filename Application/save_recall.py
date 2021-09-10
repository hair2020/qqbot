from graia.application.entry import *
from core import *
import os


app = get.app()
bcc = get.bcc()
@bcc.receiver("GroupRecallEvent")
async def function(event:GroupRecallEvent):
    # print('撤回发生')
    # f = open('/home/a5203031/qqbot/data/gjc', 'r', encoding='utf-8')
    # # f = open('data/gjc','r',encoding='utf-8')
    # list_all = f.readlines()
    # f.close()
    chehuiqun = '764839290 876117114 1038201434 867018573 773580302撤回信息'
    active_group = chehuiqun
    if str(event.group.id) in active_group:
        mesId = await app.messageFromId(event.messageId)
        # 执行/被 撤回的人
        do_recall = event.operator.id
        bei_recall = event.authorId
        # 撤回人名字
        recall_peo = event.operator.name
        if len(mesId.messageChain.dict()['__root__']) == 2:
            try:
                # 撤回的文本消息
                recall_mes = mesId.messageChain.dict()['__root__'][1]['text']
                # type='GroupMessage' messageChain=MessageChain(__root__=[Source(id=1164, time=datetime.datetime(2021, 4, 6, 7, 29, 14, tzinfo=datetime.timezone.utc)), Plain(type='Plain', text='1')]) sender=Member(id=2732631493, name='什么都不知道', permission=<MemberPerm.Member: 'MEMBER'>, group=Group(id=773580302, name='测试', accountPerm=<MemberPerm.Administrator: 'ADMINISTRATOR'>))
                recall_mes1 = recall_mes.replace('\r', ' ') # linux系统！！！\r！！！是回车！！！！！！！！
                # recall.txt[recall_peo] = recall_mes
                if bei_recall == 2732631493:
                    await app.sendGroupMessage(event.group.id, MessageChain.create([Plain(f'大胆！\n我再说一遍\n{recall_mes}')]))
                elif bei_recall == 644661457:
                    pass
                else:
                    await app.sendGroupMessage(event.group.id,MessageChain.create([Plain(f'{recall_peo}偷偷吃了一条文字信息'),]))
                    f = open('/home/a5203031/qqbot/data/recall.txt','a',encoding='utf-8')
                    # f = open('data/recall.txt', 'a', encoding='utf-8')
                    f.write(recall_peo+' '+recall_mes1+'\n')
                    f.close()
                    f = open('/home/a5203031/qqbot/data/recall.txt', 'r', encoding='utf-8')
                    # f = open('data/recall.txt', 'r', encoding='utf-8')
                    row = len(f.readlines())
                    f.close()
                    print(row)
                    if row > 9:
                        os.remove('/home/a5203031/qqbot/data/recall.txt')
            except:
                # 撤回的文本消息
                recall_pic = mesId.messageChain.dict()['__root__'][1]['url']
                # type='GroupMessage' messageChain=MessageChain(__root__=[Source(id=1164, time=datetime.datetime(2021, 4, 6, 7, 29, 14, tzinfo=datetime.timezone.utc)), Plain(type='Plain', text='1')]) sender=Member(id=2732631493, name='什么都不知道', permission=<MemberPerm.Member: 'MEMBER'>, group=Group(id=773580302, name='测试', accountPerm=<MemberPerm.Administrator: 'ADMINISTRATOR'>))
                recall_pic1 = recall_pic.replace('\r', ' ') # linux系统！！！\r！！！是回车！！！！！！！！
                # recall.txt[recall_peo] = recall_mes
                if bei_recall == 2732631493:
                    await app.sendGroupMessage(event.group.id, MessageChain.create([Plain('我就发'),Image.fromNetworkAddress(recall_pic1)]))
                elif bei_recall == 644661457:
                    pass
                else:
                    await app.sendGroupMessage(event.group.id,MessageChain.create([Plain(f'{recall_peo}偷偷吃了一条图片信息'),]))
                    f = open('/home/a5203031/qqbot/data/recall.txt','a',encoding='utf-8')
                    # f = open('data/recall.txt', 'a', encoding='utf-8')
                    f.write(recall_peo+' '+recall_pic1+'\n')
                    f.close()
                    f = open('/home/a5203031/qqbot/data/recall.txt.txt', 'r', encoding='utf-8')
                    # f = open('data/recall.txt', 'r', encoding='utf-8')
                    row = len(f.readlines())
                    f.close()
                    print(row)
                    if row > 9:
                        os.remove('/home/a5203031/qqbot/data/recall.txt')
        else:
            try:
                # 先文后图
                recall_mes = mesId.messageChain.dict()['__root__'][1]['text']
                recall_pic = mesId.messageChain.dict()['__root__'][2]['url']
                # type='GroupMessage' messageChain=MessageChain(__root__=[Source(id=1164, time=datetime.datetime(2021, 4, 6, 7, 29, 14, tzinfo=datetime.timezone.utc)), Plain(type='Plain', text='1')]) sender=Member(id=2732631493, name='什么都不知道', permission=<MemberPerm.Member: 'MEMBER'>, group=Group(id=773580302, name='测试', accountPerm=<MemberPerm.Administrator: 'ADMINISTRATOR'>))
                recall_mes1 = (recall_mes+recall_pic).replace('\r', ' ') # linux系统！！！\r！！！是回车！！！！！！！！
                # recall.txt[recall_peo] = recall_mes
                if bei_recall == 2732631493:
                    await app.sendGroupMessage(event.group.id, MessageChain.create([Plain(f'我就发\n{recall_mes}'),Image.fromNetworkAddress(recall_pic)]))
                elif bei_recall == 644661457:
                    pass
                else:
                    await app.sendGroupMessage(event.group.id,MessageChain.create([Plain(f'{recall_peo}偷偷吃了一条图文信息'),]))
                    f = open('/home/a5203031/qqbot/data/recall.txt.txt','a',encoding='utf-8')
                    # f = open('data/recall.txt', 'a', encoding='utf-8')
                    f.write(recall_peo+' '+recall_mes1+'\n')
                    f.close()
                    f = open('/home/a5203031/qqbot/data/recall.txt', 'r', encoding='utf-8')
                    # f = open('data/recall.txt', 'r', encoding='utf-8')
                    row = len(f.readlines())
                    f.close()
                    print(row)
                    if row > 9:
                        os.remove('/home/a5203031/qqbot/data/recall.txt')
            except:
                # 先图后文
                recall_pic = mesId.messageChain.dict()['__root__'][1]['url']
                recall_mes = mesId.messageChain.dict()['__root__'][2]['text']
                # type='GroupMessage' messageChain=MessageChain(__root__=[Source(id=1164, time=datetime.datetime(2021, 4, 6, 7, 29, 14, tzinfo=datetime.timezone.utc)), Plain(type='Plain', text='1')]) sender=Member(id=2732631493, name='什么都不知道', permission=<MemberPerm.Member: 'MEMBER'>, group=Group(id=773580302, name='测试', accountPerm=<MemberPerm.Administrator: 'ADMINISTRATOR'>))
                recall_pic1 = (recall_mes+recall_pic).replace('\r', ' ') # linux系统！！！\r！！！是回车！！！！！！！！
                # recall.txt[recall_peo] = recall_mes
                if bei_recall == 2732631493:
                    await app.sendGroupMessage(event.group.id, MessageChain.create([Plain(f'我就发\n{recall_mes}'),Image.fromNetworkAddress(recall_pic1)]))
                elif bei_recall == 644661457:
                    pass
                else:
                    await app.sendGroupMessage(event.group.id,MessageChain.create([Plain(f'{recall_peo}偷偷吃了一条图文片信息'),]))
                    f = open('/home/a5203031/qqbot/data/recall.txt','a',encoding='utf-8')
                    # f = open('data/recall.txt', 'a', encoding='utf-8')
                    f.write(recall_peo+' '+recall_pic1+'\n')
                    f.close()
                    f = open('/home/a5203031/qqbot/data/recall.txt', 'r', encoding='utf-8')
                    # f = open('data/recall.txt', 'r', encoding='utf-8')
                    row = len(f.readlines())
                    f.close()
                    print(row)
                    if row > 9:
                        os.remove('/home/a5203031/qqbot/data/recall.txt.txt')





