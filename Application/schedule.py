from graia.application.message.elements.internal import At, Plain,Image
from graia.application.message.chain import MessageChain
from graia.application.group import Group, Member
from graia.application.message.parser.kanata import Kanata
from graia.application.message.parser.signature import FullMatch, RequireParam
from core import *
import time
__plugin_name__ = '课表'
__plugin_usage__ = '课表/明日课表'

bcc = get.bcc()
@bcc.receiver("GroupMessage")
async def kb(
    message:MessageChain,
    group:Group,
    app:GraiaMiraiApplication,
    member:Member
):
    mes = message.asDisplay()
    if mes == '课表' or mes == '明日课表':
        # print(type(time.asctime())) str:'Mon Mar 22 20:50:52 2021'
        a = time.asctime()
        data = a.split(' ') # 以空格分成列表
        print(data[0])
        di = {'Mon': 0, 'Tue': 1, 'Wed': 2, 'Thu': 3, 'Fri': 4, 'Sat': 5, 'Sun': 6}
        # 换位
        # tempdi = {v:k for k,v in di.items()}
        classes = [['空', '线代105', '物理308', '近代史204'], ['高数301', '电路104', '空', '空', '创心思危111'], ['英语102', '单：线代104/双：物理105', '编程108', '空'], ['高数102', '电路104', '写作204', '规划213'], ['高数102', '体育', '编程108', '空'], ['无'], ['无']]

        if member.id != 1334655959:
        # with open('/home/a5203031/qqbot/data/schedule', 'r', encoding='utf-8') as fp:
        #     for line in fp.readlines():
        #         # print(type(line))# str
        #         line = line.strip()
        #         line = line.split(' ')
        #         classes.append(line)
            index = di[data[0]]
            aim = classes[index]
            if index == 6:
                to_aim = classes[0]
            else:
                to_aim = classes[index+1]
            text = '\n'.join(aim)
            to_text = '\n'.join(to_aim)

            if mes == '课表':
                if index < 5:
                    await app.sendGroupMessage(group, MessageChain.create(
                        [Plain(f'今日课表:\n{text}')]
                    ))
                else:
                    await app.sendGroupMessage(group, MessageChain.create(
                        [Plain('今天是周末啊，不会还补课吧')]
                    ))
            elif mes == '明日课表':
                if index+1 < 5 or index == 6:
                    await app.sendGroupMessage(group, MessageChain.create(
                        [Plain(f'明日课表:\n{to_text}')]
                    ))
                else:
                    await app.sendGroupMessage(group, MessageChain.create(
                        [Plain('明天是周末啊，不会还补课吧')]
                    ))
        if member.id == 1334655959:
            index = di[data[0]]
            aim = classes2[index]
            if index == 6:
                to_aim = classes2[0]
            else:
                to_aim = classes2[index + 1]
            text = '\n'.join(aim)
            to_text = '\n'.join(to_aim)

            if mes == '课表':
                if index < 5:
                    await app.sendGroupMessage(group, MessageChain.create(
                        [Plain(f'今日课表:\n{text}')]
                    ))
                else:
                    await app.sendGroupMessage(group, MessageChain.create(
                        [Plain('今天是周末啊，不会还补课吧')]
                    ))
            elif mes == '明日课表':
                if index + 1 < 5 or index == 6:
                    await app.sendGroupMessage(group, MessageChain.create(
                        [Plain(f'明日课表:\n{to_text}')]
                    ))
                else:
                    await app.sendGroupMessage(group, MessageChain.create(
                        [Plain('明天是周末啊，不会还补课吧')]
                    ))



