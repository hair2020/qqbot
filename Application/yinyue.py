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
__plugin_name__ = '音乐播放'
__plugin_usage__ = '输入点歌歌名'

bcc = get.bcc()

@bcc.receiver('GroupMessage',dispatchers=[
    Kanata([FullMatch("点歌"),RequireParam(name='music')])
])
async def yinyue(
    message:MessageChain,
    group:Group,
    member:Member,
    app:GraiaMiraiApplication,
    music:MessageChain
):
    content = []
    try:
        headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'
            }
        key_word = music.asDisplay()
        api = 'https://musicapi.leanapp.cn/search?keywords='
        res = requests.get(api+key_word,headers=headers)
        res = json.loads(res.text)
        for i in res['result']['songs'][:3]:
            ids = i['id']
            name = i['name']
            author = i['artists'][0]['name']
            bofang = f'https://music.163.com/song/media/outer/url?id={ids}.mp3'
            await app.sendGroupMessage(group,MessageChain.create([
            Plain(f"歌名:{name}\n歌手:{author}\n"+bofang)
        ]))
        
    except Exception:
        await app.sendGroupMessage(group,MessageChain.create([Plain("没有这个歌！")]))
   