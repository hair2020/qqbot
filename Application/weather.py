import requests
import json
from graia.application.message.elements.internal import At, Plain,Image
from graia.application.message.chain import MessageChain
from graia.application.group import Group, Member
from graia.application.message.parser.kanata import Kanata
from graia.application.message.parser.signature import FullMatch, RequireParam, OptionalParam
from core import *
from bs4 import BeautifulSoup as bs

__plugin_name__ = '天气预报'
__plugin_usage__ = '天气某地'

bcc = get.bcc()
@bcc.receiver("GroupMessage",dispatchers=[
    Kanata([FullMatch("天气"),OptionalParam(name='city')])
])
async def report(
    message:MessageChain,
    group:Group,
    member:Member,
    app:GraiaMiraiApplication,
    city:MessageChain
):
    if message.asDisplay() == '天气':
        await app.sendGroupMessage(group, MessageChain.create([Plain("你没说城市呢")]))
    else:
        url_api = f'http://www.tianqiapi.com/api?version=v61&appid=58719735&appsecret=y8wIcaYs&city={city.asDisplay()}'
        res = requests.get(url_api)
        res.encoding='utf-8'
        js = json.loads(res.text)
        try:
            date = js['date']
            week = js['week']
            update_time = js['update_time']
            citys = js['city']
            wea = js['wea']
            tem = js['tem']
            tem1 = js['tem1']
            tem2 = js['tem2']
            win = js['win']
            humidity = js['humidity']
            air_level = js['air_level']
            air_tips = js['air_tips']
            alarm = js['alarm']
            aqi = js['aqi']
            await app.sendGroupMessage(group,MessageChain.create([
                Plain(f"今天是{date}号,{week},到{update_time}为止,{citys}的天气状况为{wea}\n实时温度为{tem}°,今日最高温为{tem1}°,最低温为{tem2}°,请做好穿衣准备\n今日风向为{win},湿度为{humidity}.\n空气质量为{air_level},{air_tips}\n今日预警类型为{alarm['alarm_type']},预警等级为{alarm['alarm_level']},{alarm['alarm_content']}\n空气质量为{aqi['air_level']}")
            ]))
        except:
            await app.sendGroupMessage(group, MessageChain.create([Plain("请输入中国城市")]))
bcc = get.bcc()
@bcc.receiver("GroupMessage",dispatchers=[
    Kanata([FullMatch("明日天气")])
])
async def report(
    message:MessageChain,
    group : Group,
    app :GraiaMiraiApplication
):
    head = {'user-agent': 'firefox'}
    url = 'http://tianqi.2345.com/pc/tomorrowPage'
    res = requests.get(url, head).text
    res.encode('utf-8')
    soup = bs(res, 'lxml')
    w = soup.select('.real-today > span')
    t_w = w[0].string
    await app.sendGroupMessage(group, MessageChain.create([Plain(t_w)]))
