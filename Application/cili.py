import requests
import json
from graia.application.message.elements.internal import At, Plain,Image
from graia.application.message.chain import MessageChain
from graia.application.group import Group, Member
from graia.application.message.parser.kanata import Kanata
from graia.application.message.parser.signature import FullMatch, RequireParam
from core import *
from lxml import etree
__plugin_name__ = '磁力链接'
__plugin_usage__ = '输入磁力xx'

bcc = get.bcc()
@bcc.receiver("GroupMessage",dispatchers=[
    Kanata([FullMatch("磁力"),RequireParam(name='cili')],headless_decoraters = [judge.config_check(__name__)])
])
async def cl(
    message:MessageChain,
    group:Group,
    member:Member,
    app:GraiaMiraiApplication,
    cili:MessageChain
):
    headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'
    }
    url = 'https://btsow.com/search/'
    name = cili.asDisplay()
    qianzhui = 'magnet:?xt=urn:btih:'
    try:
        res = requests.get(url+name,headers =headers)
        sele = etree.HTML(res.text)
        lis = sele.xpath('//div[@class="row"]')
        url_pages = []
        for li in lis:
            url_pages.append(li.xpath('a/@href')[0]+f"&dn={li.xpath('a/@title')[0]}")
    except IndexError:
        pass
    new_cili = []
    for url_i in url_pages:
        url_i = url_i.replace('https://btsow.cam/magnet/detail/hash/',qianzhui)
        new_cili.append(url_i)
    await app.sendGroupMessage(group,MessageChain.create([
        Plain(f"{i}\n\n") for i in new_cili[:3]
    ]))

