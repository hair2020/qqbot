# -*- coding = utf -8 -*-
# @Time : 2021/4/13 19:44
# @Author : hair
from graia.application.message.elements.internal import At, Plain,Image
from graia.application.message.parser.signature import *
from core import *
from graia.application.friend import Friend
from graia.scheduler import (
    timers,
)
from graia.application.entry import *

import time
import sqlite3


def help():
	func = '1.回复“E” FrequentWords 16s后出中文\n2.回复"Week" 查询第几周及寒假时间\n3.回复“今天”“明天”查看课表，任意回复提示当前要上啥课\n4.隐藏功能无介绍'
	return func

# 1234对应第几节课
def judgeTime():
	h = time.localtime().tm_hour
	# print(h)
	if h < 9:
		return 1
	elif h < 11:
		return 2
	elif h < 15:
		return 3
	elif h < 17:
		return 4
	else:
		return 0

def judgeDay():
	day = time.localtime().tm_wday

	return day + 1

def get_data(c):

	datas = c.execute('select * from MyClass').fetchall()

	dic = {}
	nn = 0
	for ind,d in enumerate(datas):
		if (ind+1) % 4 == 0:
			dic[(ind+1) / 4] = datas[nn:(ind+1)]
			nn += 4
		else:
			pass
	# print(dic)
	# print(len(dic))
	return dic

def choice_words(n,c):
	import random
	words = c.execute('select eng from FrequentWords').fetchall()
	zh = c.execute('select zh from FrequentWords').fetchall()

	# print(len(zh),len(words))
	index = []
	for i in range(n):
		index.append(random.randint(0, 691))

	chinese = ''
	english = ''
	for i in range(n):
		chinese += zh[index[i]][0] + '\n'
		english += words[index[i]][0] + '\n'

	return chinese, english

def WitchWeek():
	import datetime
	start = datetime.datetime(2021,8,30).date()
	now = datetime.date.today()

	end = datetime.datetime(2022,1,9).date()
	winterHolidayDays = (end - now).days

	gap = (now - start).days
	if gap / 7 < 1:
		return 1,winterHolidayDays
	else:
		if gap % 7 == 0:
			return int(gap / 7),winterHolidayDays
		else:
			return int(gap / 7) + 1 , winterHolidayDays

def findUsers(c):
	qq = c.execute('select qq from user').fetchall()
	u = ''
	for q in qq:
		u += str(q[0])+','
	return u

def addUser(c,qq):
	c.execute(f'insert into user values ({qq})')
def deleteUser(c,qq):
	c.execute(f'delete from user where qq = {qq}')

def sentence(c):
	Rfart = c.execute('select RainbowFart from sentence').fetchall()
	qh = c.execute('select qinghua from sentence').fetchall()
	qh = qh[:94]
	return Rfart,qh

bcc = get.bcc()
@bcc.receiver("FriendMessage")
async def friend_message_listener(message:MessageChain,app: GraiaMiraiApplication, friend: Friend):
	conn = sqlite3.connect('/home/a5203031/qqbot/App/txt.db')
	c = conn.cursor()
	users = findUsers(c)

	if str(friend.id) in users:
		mes = message.asDisplay()

		if mes == 'E':
			chinese, english = choice_words(6,c)

			await app.sendFriendMessage(friend, MessageChain.create([
				Plain(english)
			]))

			await asyncio.sleep(16)

			await app.sendFriendMessage(friend, MessageChain.create([
				Plain(chinese)
			]))

		elif mes == 'help':
			func = help()
			await app.sendFriendMessage(friend, MessageChain.create([
				Plain(func)
			]))
		elif mes == 'Week':
			number,winterHolidayDays = WitchWeek()
			await app.sendFriendMessage(friend, MessageChain.create([
				Plain(f'这是第{number}周，\n距离寒假还有{winterHolidayDays}天')
			]))

		elif mes in '明天今天':
			dayke = get_data(c)
			day = judgeDay()
			# print(dayke)
			# print(dayke[day])

			if mes == '今天':
				if day < 6:
					text = ''
					for tup in dayke[day]:
						text += tup[0]
					await app.sendFriendMessage(friend, MessageChain.create([
						Plain(text)
					]))
				else:
					await app.sendFriendMessage(friend, MessageChain.create([
						Plain(f'今天是周日')
					]))
			else:
				if day < 5:
					text2 = ''
					for tup in dayke[day+1]:
						text2 += tup[0]

					await app.sendFriendMessage(friend, MessageChain.create([
						Plain(text2)
					]))
				elif day == 7:
					text2 = ''
					for tup in dayke[1]:
						text2 += tup[0]

					await app.sendFriendMessage(friend, MessageChain.create([
						Plain(text2)
					]))
				else:
					await app.sendFriendMessage(friend, MessageChain.create([
						Plain(f'明天是周日')
					]))

		elif mes.startswith('qq=='):
			qq = mes.split('==')[1]
			addUser(c,qq)
			await app.sendFriendMessage(friend, MessageChain.create([
				Plain('添加用户成功')
			]))
		elif mes.startswith('delete=='):
			qq = mes.split('==')[1]
			deleteUser(c,qq)
			await app.sendFriendMessage(friend, MessageChain.create([
				Plain('删除用户成功')
			]))

		elif mes in 'Rf,Qh':
			r,q = sentence(c)
			import random

			if mes == 'Rf':
				rf = random.choice(r)
				await app.sendFriendMessage(friend, MessageChain.create([
					Plain(rf[0])
				]))
			else:
				qh = random.choice(q)
				await app.sendFriendMessage(friend, MessageChain.create([
					Plain(qh[0])
				]))
		else:
			tly = judgeTime()
			dayke = get_data(c)

			day = judgeDay()
			if day <6:
				if tly == 0:
					await app.sendFriendMessage(friend, MessageChain.create([
						Plain('这都几点了')
					]))
				else:
					await app.sendFriendMessage(friend, MessageChain.create([
						Plain(dayke[day][tly-1][0])
					]))
			else:
				await app.sendFriendMessage(friend, MessageChain.create([
					Plain(f'今天是周{day}')
				]))

	else:
		await app.sendFriendMessage(friend, MessageChain.create([
			Plain('您没有权限使用，请联系644661457')
		]))

	conn.commit()
	conn.close()

# 自动加好友
@bcc.receiver("NewFriendRequestEvent")
async def accept(event:NewFriendRequestEvent):
    await event.accept()