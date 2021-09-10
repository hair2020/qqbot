from graia.application import GraiaMiraiApplication
from graia.application.event.messages import GroupMessage
from graia.application.message.elements.internal import Plain, Image
from graia.application.message.chain import MessageChain
from graia.application.message.parser.kanata import Kanata
from graia.application.message.parser.signature import FullMatch, RequireParam
from graia.application.group import Group, Member
from core import get

import aiohttp
from urllib.parse import quote

__plugin_name__ = '帮助列表'
__plugin_usage__ = '输入help'

bcc = get.bcc()
@bcc.receiver("GroupMessage",dispatchers=[Kanata([FullMatch("help")])])
async def help(
    app:GraiaMiraiApplication,
    member:Member,
    group:Group,
    message:MessageChain
):
    await app.sendGroupMessage(group, MessageChain.create(
        [
            Plain("1.实时热点/today/简报:查看10条实时热点+链接/历史上的今天/新闻简报\n"),
            Plain("2.语种+句子/词:翻译支持英文 日文 文言文 中文\n"),
            Plain("3.天气+地点/明日天气:查看中国某地天气/烟台明日天气\n"),
            Plain("4.诗词:随机诗词\n"),
            Plain("5.lol:lol资讯\n"),
            Plain("6.抢劫+@：与功能19联动\n"),
            Plain("7.签到:签个到，加钱\n"),
            Plain("8.XXXXXXX\n"),
            Plain("9.比站xx:搜索B站视频弹出前三条\n"),
            Plain("10.输入特殊词汇有反应\n"),
            Plain("11.百科xx : 显示该词条主要信息\n"),
            Plain("12.点歌xx : 弹出前三首\n"),
            Plain("13.成语xx、接龙xx : 查询意思、成语接龙\n"),
            Plain("14.课表/明日课表：我的课表\n"),
            Plain("15.摸头：摸头+@\n"),
            Plain("16.每日一句：英语每日一句\n"),
            Plain("17.瞎写+主题+字数：瞎写一篇文章\n"),
            Plain("18.骂他/舔/教育+@\n"),
            Plain("19.查询余额:看钱，如果有的话\n"),
            Plain("可针对群定时发送内容\n"),
            Plain("秘密功能。特殊群有效\n"),
            Plain("有想要的功能联系644661457，有空就做\n"),
            Plain("没有反应就是服务器关了或者网络不行，仅供娱乐学习"),
        ]
    ))