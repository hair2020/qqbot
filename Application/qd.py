
from graia.application.message.chain import MessageChain
from graia.application.message.parser.kanata import Kanata
from graia.application.message.parser.signature import FullMatch, OptionalParam
from graia.application.message.elements.internal import At, Plain,Image
from core import *

import aiohttp
import random
import time
import json
# 存信息
qded = {}
date = []

bcc = get.bcc()
@bcc.receiver("GroupMessage", dispatchers=[
	Kanata([FullMatch("签到")])  # 需要匹配值后面的内容时需要加RequireParam(name='RobRecord.json') 否则别加不然没反应
])
async def qd(
		message: MessageChain,
		app: GraiaMiraiApplication,
		group: Group,
		member: Member,
):
	# 更新
	a = time.asctime()  # str:'Mon Mar 22 20:50:52 2021'
	data = a.split(' ')  # 以空格分成列表
	if data[2] in date:
		pass
	else:
		date.append(data[2])
	if len(date)>1:
		qded.clear()
		del(date[0])
	with open('/home/a5203031/qqbot/data/qdju','r',encoding='utf-8') as f:
		sentences = f.readlines()
	t = random.choice(sentences)
	qian = random.randint(-10,40)
	if member.id not in qded:
		if member.id == 644661457:
			if qian >= 0:
				await app.sendGroupMessage(group, MessageChain.create(
					[Image.fromNetworkAddress(f'http://q1.qlogo.cn/g?b=qq&nk={member.id}&s=640'),
					 At(member.id),
					 Plain(f"恭喜获得{qian}元\n{'你真帅！'}"), ]
				))
				qded[member.id] = '你真帅！ '
			else:
				await app.sendGroupMessage(group, MessageChain.create(
					[Image.fromNetworkAddress(f'http://q1.qlogo.cn/g?b=qq&nk={member.id}&s=640'),
					 At(member.id),
					 Plain(f"今天上缴保护费{abs(qian)}元\n{'你真帅！'}"), ]
				))
				qded[member.id] = '你真帅！ '
			with open('/home/a5203031/qqbot/data/RobRecord.json','r',encoding='utf-8') as f1:
				dic = json.loads(f1.read())
				dic[str(member.id)][0] += qian
				dic = json.dumps(dic)
			with open('/home/a5203031/qqbot/data/RobRecord.json', 'w', encoding='utf-8') as f2:
				f2.write(dic)
		else:
			if qian >= 0:
				await app.sendGroupMessage(group, MessageChain.create(
					[Image.fromNetworkAddress(f'http://q1.qlogo.cn/g?b=qq&nk={member.id}&s=640'),
					 At(member.id),
					 Plain(f"恭喜获得{qian}元\n{t}")]
				))
				qded[member.id] = t
			else:
				await app.sendGroupMessage(group, MessageChain.create(
					[Image.fromNetworkAddress(f'http://q1.qlogo.cn/g?b=qq&nk={member.id}&s=640'),
					 At(member.id),
					 Plain(f"今天上交保护费{abs(qian)}元\n{t}")]
				))
				qded[member.id] = t
			with open('/home/a5203031/qqbot/data/RobRecord.json','r',encoding='utf-8') as f1:
				dic = json.loads(f1.read())
				dic[str(member.id)][0] += qian
				dic = json.dumps(dic)
			with open('/home/a5203031/qqbot/data/RobRecord.json', 'w', encoding='utf-8') as f2:
				f2.write(dic)
	else:
		await app.sendGroupMessage(group, MessageChain.create(
			[Image.fromNetworkAddress(f'http://q1.qlogo.cn/g?b=qq&nk={member.id}&s=640'),
			 At(member.id),
			 Plain(f"今天在我这签到过啦!\n{qded[member.id]}")]
		))







