import requests
import json
from graia.application.message.elements.internal import At, Plain,Image,Voice,Voice_LocalFile
from graia.application.message.chain import MessageChain
from graia.application.group import Group, Member
from graia.application.message.parser.kanata import Kanata
from graia.application.message.parser.signature import FullMatch, RequireParam
from core import *
from pathlib import Path
from lxml import etree
__plugin_name__ = '诗词'
__plugin_usage__ = '输入诗词'

bcc = get.bcc()

@bcc.receiver('GroupMessage',dispatchers=[
    Kanata([FullMatch("诗词")])
])
async def sc(
    message:MessageChain,
    group:Group,
    member:Member,
    app:GraiaMiraiApplication,

):
    res = requests.get('http://poetry.apiopen.top/sentences')
    res = json.loads(res.text)
    await app.sendGroupMessage(group,MessageChain.create([
        Plain(f"{res['result']['name']}----{res['result']['from']}")
    ]))