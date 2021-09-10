import requests
import json
from graia.application.message.elements.internal import At, Plain,Image
from graia.application.message.chain import MessageChain
from graia.application.group import Group, Member
from graia.application.message.parser.kanata import Kanata
from graia.application.message.parser.signature import FullMatch, RequireParam
from core import *
import random
import hashlib
__plugin_name__ = '翻译'
__plugin_usage__ = '英文汉语日文'

bcc = get.bcc()
@bcc.receiver("GroupMessage",dispatchers=[
    Kanata([FullMatch("英文"),RequireParam(name='han')])
])
async def fy1(
    message:MessageChain,
    group:Group,
    member:Member,
    app:GraiaMiraiApplication,
    han:MessageChain
):
    appid = '20201213000646579'
    mishi = 'RhvMUyAdiKssxgF0IIFR'
    fromLang = 'auto'   #原文语种
    toLang = 'en'   #译文语种
    salt = random.randint(32768, 65536)
    q = han.asDisplay()
    sign = appid + q + str(salt) + mishi
    sign = hashlib.md5(sign.encode()).hexdigest()
    url = f'http://api.fanyi.baidu.com/api/trans/vip/translate?q={q}&from={fromLang}&to={toLang}&appid={appid}&salt={salt}&sign={sign}'
    res = requests.get(url)
    js = json.loads(res.text)
    await app.sendGroupMessage(group,MessageChain.create([
        Plain(f"{js['trans_result'][0]['src']} : {js['trans_result'][0]['dst']}")
    ]))

@bcc.receiver("GroupMessage",dispatchers=[
    Kanata([FullMatch("中文"),RequireParam(name='han')])
])
async def fy2(
    message:MessageChain,
    group:Group,
    member:Member,
    app:GraiaMiraiApplication,
    han:MessageChain
):
    appid = '20201213000646579'
    mishi = 'RhvMUyAdiKssxgF0IIFR'
    fromLang = 'auto'   #原文语种
    toLang = 'zh'   #译文语种
    salt = random.randint(32768, 65536)
    q = han.asDisplay()
    sign = appid + q + str(salt) + mishi
    sign = hashlib.md5(sign.encode()).hexdigest()
    url = f'http://api.fanyi.baidu.com/api/trans/vip/translate?q={q}&from={fromLang}&to={toLang}&appid={appid}&salt={salt}&sign={sign}'
    res = requests.get(url)
    js = json.loads(res.text)
    await app.sendGroupMessage(group,MessageChain.create([
        Plain(f"{js['trans_result'][0]['src']} : {js['trans_result'][0]['dst']}")
    ]))


@bcc.receiver("GroupMessage",dispatchers=[
    Kanata([FullMatch("文言文"),RequireParam(name='wyw')])
])
async def fy2(
    message:MessageChain,
    group:Group,
    member:Member,
    app:GraiaMiraiApplication,
    wyw:MessageChain
):
    appid = '20201213000646579'
    mishi = 'RhvMUyAdiKssxgF0IIFR'
    fromLang = 'auto'   #原文语种
    toLang = 'wyw'   #译文语种
    salt = random.randint(32768, 65536)
    q = wyw.asDisplay()
    sign = appid + q + str(salt) + mishi
    sign = hashlib.md5(sign.encode()).hexdigest()
    url = f'http://api.fanyi.baidu.com/api/trans/vip/translate?q={q}&from={fromLang}&to={toLang}&appid={appid}&salt={salt}&sign={sign}'
    res = requests.get(url)
    js = json.loads(res.text)
    await app.sendGroupMessage(group,MessageChain.create([
        Plain(f"{js['trans_result'][0]['src']} : {js['trans_result'][0]['dst']}")
    ]))
@bcc.receiver("GroupMessage",dispatchers=[
    Kanata([FullMatch("日文"),RequireParam(name='rw')])
])
async def fy2(
    message:MessageChain,
    group:Group,
    member:Member,
    app:GraiaMiraiApplication,
    rw:MessageChain
):
    appid = '20201213000646579'
    mishi = 'RhvMUyAdiKssxgF0IIFR'
    fromLang = 'auto'   #原文语种
    toLang = 'jp'   #译文语种
    salt = random.randint(32768, 65536)
    q = rw.asDisplay()
    sign = appid + q + str(salt) + mishi
    sign = hashlib.md5(sign.encode()).hexdigest()
    url = f'http://api.fanyi.baidu.com/api/trans/vip/translate?q={q}&from={fromLang}&to={toLang}&appid={appid}&salt={salt}&sign={sign}'
    res = requests.get(url)
    js = json.loads(res.text)
    await app.sendGroupMessage(group,MessageChain.create([
        Plain(f"{js['trans_result'][0]['src']} : {js['trans_result'][0]['dst']}")
    ]))




