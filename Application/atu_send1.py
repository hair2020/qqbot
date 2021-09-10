# -*- coding = utf -8 -*-
# @Time : 2021/3/30 13:04
# @Author : hair
import graia.application.message.elements.internal as Elements
from graia.application import GraiaMiraiApplication, Session
from graia.application.message.chain import MessageChain
from graia.application.message.elements.internal import At, Plain,Image
from bs4 import BeautifulSoup
from graia.application.message.elements.internal import Plain,Image
from graia.application.friend import Friend
from graia.scheduler import (
    timers,
)
from core import *
import requests
import time
import json
import re
def rd():
    # 百度热点
    url = "http://top.baidu.com/buzz?b=1&fr=topindex"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36'}
    res = requests.get(url, headers=headers)
    # 处理乱码
    res.encoding = res.apparent_encoding
    # news = res.text.encode(res.encoding).decode('gb2312')
    # BS解析网页
    soup0 = BeautifulSoup(res.text, "html.parser")  # 传str对象
    # 用select找出出所有含新闻的标签
    aimdata = soup0.select('a.list-title')  # a 标签中的。。。属性
    urls = []  # 新闻链接
    titles = []  # 新闻题目
    n = 0
    for i in aimdata:
        if n < 10:  # 显示10条
            # 如果标签下没有其他标签，可用.string提取中文
            temp_urls = i['href']
            titles.append(i.string)
            n += 1

            # 取百度后的第一条
            res = requests.get(temp_urls,headers = headers).text
            soup1 = BeautifulSoup(res, 'lxml')
            aimdata2 = soup1.select('.title_3p8-I > a')  # <class 'bs4.element.ResultSet'>
            # 请求网页不一致导致列表为空时
            try:
                urldata2 = aimdata2[0]['href']
                urls.append(urldata2)
            except:
                pass
    # 合为字典
    ok = dict(zip(titles, urls)).items()
    list = []
    for index, (k, v) in enumerate(ok):
        list.append(f'{index + 1}.{k} \n{v}')
    text = '\n'.join(list)
    return text

def kebiao():
    a = time.asctime()# str:'Mon Mar 22 20:50:52 2021'
    data = a.split(' ')# 以空格分成列表
    di = {'Mon': 0, 'Tue': 1, 'Wed': 2, 'Thu': 3, 'Fri': 4, 'Sat': 5, 'Sun': 6}
    # 换位
    # tempdi = {v:k for k,v in di.items()}
    # fp = open('D:\hair\qqbot\data\schedule', 'r', encoding='utf-8')
    # with open('/home/a5203031/qqbot/data/schedule', 'r', encoding='utf-8') as fp:
    # fp = open(r'D:\hair\qqbot\data\schedule', 'r', encoding='utf-8')
    classes = [['空', '线代105', '物理308', '近代史204'], ['高数301', '电路104', '空', '空', '创心思危111'], ['英语102', '单：线代104/双：物理105', '编程108', '空'], ['高数102', '电路104', '写作204', '规划213'], ['高数102', '体育', '编程108', '空'], ['无'], ['无']]
    # print(len(classes))
    index = di[data[0]]
    aim = classes[index]
    text = '\n'.join(aim)
    if index < 5:
        return text
    else:
        return '今天周末'

def yingyu():
    head = {'user-agent': 'firefox'}
    url = "http://open.iciba.com/dsapi/"
    res = requests.get(url,head)
    eng = res.json()['content']
    tran = res.json()['note']
    pic = res.json()['picture']
    return f'{eng}\n{tran}',pic

def tianqi():
    head = {'user-agent': 'firefox'}
    url_api = f'http://www.tianqiapi.com/api?version=v61&appid=58719735&appsecret=y8wIcaYs&city=烟台'
    res = requests.get(url_api,head)
    res.encoding='utf-8'
    js = json.loads(res.text)
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
    return f"今天是{date}号,{week},到{update_time}为止,{citys}的天气状况为{wea}\n实时温度为{tem}°,今日最高温为{tem1}°,最低温为{tem2}°,请做好穿衣准备\n今日风向为{win},湿度为{humidity}.\n空气质量为{air_level},{air_tips}\n今日预警类型为{alarm['alarm_type']},预警等级为{alarm['alarm_level']}"

def jianbao():
    head = {'user-agent': 'firefox'}
    # 拿到今日简报网址
    url = 'https://www.163.com/dy/media/T1603594732083.html'
    res = requests.get(url, head)
    res.encoding = res.apparent_encoding
    datas = res.text
    soup = BeautifulSoup(datas, 'lxml')
    aimdata = soup.select('.media_article_title > a')
    to_url = aimdata[0]['href']

    # 爬取简报
    jianbao = []
    res1 = requests.get(to_url, head)
    res1.encoding = res1.apparent_encoding
    datas1 = res1.text
    soup1 = BeautifulSoup(datas1, 'lxml')
    aimdata1 = soup1.select('.post_body > p')
    # 取
    jb = re.findall('、(.*?)。', str(aimdata1))
    JB = []
    for n, i in enumerate(jb):
        JB.append(f'{n + 1}、{i}')
    text = '\n'.join(JB)
    return text
def huangli():
    head = {'user-agent': 'firefox'}
    # 黄历网址
    url = 'https://huangli999.com/'
    res = requests.get(url, head)
    res.encoding = res.apparent_encoding
    # print(res.apparent_encoding)
    datas = res.text
    soup = BeautifulSoup(datas, 'lxml')
    nongli = soup.select('.nongli')[0]
    yi = soup.select('.yi')[0]
    ji = soup.select('.ji')[0]
    # print(nongli.string)
    # print(yi)
    # print(ji)
    yi = re.findall('</span> (.*?)</div>', str(yi))
    ji = re.findall('</span>(.*?)</div>', str(ji))
    text = f'{nongli.string}\n宜：{yi[0]}\n忌:{ji[0]}'
    return text
# 群
glist = [867018573]

bcc = get.bcc()
app = get.app()
sche = get.sche()
@sche.schedule(timers.crontabify('06 6 * * *'))
async def auto():
        # sentence,pic = yingyu()
        ke = kebiao()
        weather = tianqi()
        # 班级群
        await app.sendGroupMessage(glist[0], MessageChain.create([
            # Elements.AtAll(),
            Plain(f'{weather}今日课表：\n{ke}')
        ]))

        # await app.sendGroupMessage(glist[1], MessageChain.create([
        #     Plain(f'今日课表:\n{ke}\n{ke2}')
        # ]))

sche = get.sche()
@sche.schedule(timers.crontabify('16 11 * * *'))
async def auto():
        jb = jianbao()
        for g in glist:
            await app.sendGroupMessage(g, MessageChain.create([
                # Elements.AtAll(),
                Plain(jb)
            ]))
sche = get.sche()
@sche.schedule(timers.crontabify('16 16 * * *'))
async def auto():
        baidu = rd()
        for g in glist:
            await app.sendGroupMessage(g, MessageChain.create([
                # Elements.AtAll(),
                Plain(baidu)
            ]))

# 刷新群抢劫次数
sche = get.sche()
@sche.schedule(timers.crontabify('00 00 * * *'))
async def auto():
    with open('/home/a5203031/qqbot/data/RobRecord.json', 'r', encoding='utf-8') as f:
        dic = json.loads(f.read())
        dic = dict(dic)
    it = list(dic.items())# 更新次数用
    # rank = sorted(dic.items(), key=lambda d: d[1][2], reverse=True)# 按收入倒序排
    # name = await app.getMember(867018573,int(rank[0][0]))
    # name = name.name# 最多收入的人
    # print(rank[0][1][2])
    for i in glist:
        await app.sendGroupMessage(i, MessageChain.create([
            # Plain(f'各位大佬抢劫次数刷新\n今日老大是{name},抢了{rank[0][1][2]}元\n')
            # Image.fromLocalFile('/home/a5203031/qqbot/data/first.jpg')
            Plain(f'早上好'),
            Image.fromLocalFile('/home/a5203031/qqbot/data/morning.jpg')
        ]))

    # 更新次数和收入
    # print(it)
    for i in range(len(dic)):
        it[i][1][1] = 10
        it[i][1][2] = 0
    dic = json.dumps(dic)
    with open('/home/a5203031/qqbot/data/RobRecord.json', 'w', encoding='utf-8') as f1:
        f1.write(dic)
        # print('ok')

sche = get.sche()
@sche.schedule(timers.crontabify('06 8 * * *'))
async def auto():
        hl = huangli()
        for g in glist:
            await app.sendGroupMessage(g, MessageChain.create([
                # Elements.AtAll(),
                Plain(f'{hl}')
            ]))








