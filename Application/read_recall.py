# -*- coding = utf -8 -*-
# @Time : 2021/4/6 16:19
# @Author : hair
from graia.application.message.elements.internal import At, Plain, Image
from graia.application.message.chain import MessageChain
from graia.broadcast.interrupt.waiter import Waiter
from graia.application.event.messages import GroupMessage
from core import *
chakanren = [644661457,3107449425]
app = get.app()
bcc = get.bcc()
inc = InterruptControl(bcc)
@bcc.receiver("GroupMessage")
async def group_message_handler(
    message: MessageChain,
    app: GraiaMiraiApplication,
    group: Group,
    member: Member,
):
    if message.asDisplay().startswith("recall mes") and member.id in chakanren:
        n = 1
        temp = ''
        recalled = {}
        with open('/home/a5203031/qqbot/data/recall.txt', 'r', encoding='utf-8') as f:
            for line in f.readlines():
                line = line.strip()
                line = line.split(' ')
                if line[0] == temp:
                    recalled[f'{line[0]}{n}'] = line[1]
                    n += 1
                else:
                    try:
                        recalled[line[0]] = line[1]
                    except:
                        await app.sendGroupMessage(group, MessageChain.create([Plain('抱歉，出现预期之外的错误')]))
                        return
                temp = line[0]
        if len(recalled) == 0:
            await app.sendGroupMessage(group, MessageChain.create([
                At(member.id), Plain("没有收到撤回消息")
            ]))
        else:
            await app.sendGroupMessage(group, MessageChain.create([
                At(member.id), Plain(f"共有{len(recalled)}条，输入confirm查看撤回人(时间由上到下递增)\n输入cancel取消操作")
            ]))
            @Waiter.create_using_function([GroupMessage])
            def waiter(
                event: GroupMessage, waiter_group: Group,
                waiter_member: Member, waiter_message: MessageChain
            ):
                if all([
                    waiter_group.id == group.id,
                    waiter_member.id == member.id,
                    waiter_message.asDisplay() == "confirm"
                ]):
                    return event
                if all([
                    waiter_group.id == group.id,
                    waiter_member.id == member.id,
                    waiter_message.asDisplay() == "cancel"
                ]):
                    return 0
            a = await inc.wait(waiter)
            if a == 0:
                return
            dic = {}
            for index,i in enumerate(tuple(recalled.values())):
                dic[index] = i
            s = ''
            for index,i in enumerate(tuple(recalled.keys())):
                s += str(index) + '.' + i + '\n'
            await app.sendGroupMessage(group, MessageChain.create([
                Plain(s)
            ]))
            await app.sendGroupMessage(group, MessageChain.create([
                At(member.id),
                Plain('输入序号(1 2...)查看内容')
            ]))
            @Waiter.create_using_function([GroupMessage])
            def waiter(
                event: GroupMessage, waiter_group: Group,
                waiter_member: Member, waiter_message: MessageChain
            ):
                if all([
                    waiter_group.id == group.id,
                    waiter_member.id == member.id,
                    waiter_message.asDisplay() in '0123456789'
                ]):
                    return event.messageChain.asDisplay()

            mes_index = await inc.wait(waiter)
            try:
                await app.sendGroupMessage(group, MessageChain.create([
                    Plain(f'撤回内容如下\n'),
                    Image.fromNetworkAddress(dic[int(mes_index)])
                ]))
            except:
                await app.sendGroupMessage(group, MessageChain.create([
                    Plain(f'撤回内容如下\n{dic[int(mes_index)]}')
                ]))



