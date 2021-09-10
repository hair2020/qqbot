# -*- coding = utf -8 -*-
# @Time : 2021/3/22 12:13
# @Author : hair
import requests
from bs4 import BeautifulSoup
from graia.application.message.elements.internal import At, Plain,Image
from graia.application.message.chain import MessageChain
from graia.application.group import Group, Member
from graia.application.message.parser.kanata import Kanata
from graia.application.message.parser.signature import FullMatch, RequireParam
from core import *
from bs4 import BeautifulSoup
import aiohttp
import re
__plugin_name__ = '新闻类'
__plugin_usage__ = '输入热点，today，简报'

bcc = get.bcc()
@bcc.receiver("GroupMessage")
async def rd(
    message:MessageChain,
    app:GraiaMiraiApplication,
    group:Group,
    member:Member
):
    if message.asDisplay().startswith("实时热点"):
        #百度热点
        url = "http://top.baidu.com/buzz?b=1&fr=topindex"
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36'}
        res = requests.get(url,headers = headers)
        #处理乱码
        res.encoding = res.apparent_encoding
        # news = res.text.encode(res.encoding).decode('gb2312')
        #BS解析网页
        soup0 = BeautifulSoup(res.text,"html.parser") #传str对象
        #用select找出出所有含新闻的标签
        aimdata = soup0.select('a.list-title')#a 标签中的。。。属性
        urls = [] #新闻链接
        titles = [] #新闻题目
        n = 0
        for i in aimdata:
            if n<10: #显示10条
                # 如果标签下没有其他标签，可用.string提取中文
                temp_urls= i['href']
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
        for index,(k,v) in enumerate(ok):
            list.append(f'{index+1}.{k} \n{v}')
        text = '\n'.join(list)
        await app.sendGroupMessage(group,MessageChain.create([
            Plain(text)
        ]))

    if message.asDisplay() == "today":
        Text = requests.get(r'http://www.ipip5.com/today/api.php?type=txt').text.split('\n')
        # 删除最后一个元素
        Text.pop()
        Str = '\n'.join(Text)
        await app.sendGroupMessage(group,MessageChain.create([
            Plain(Str)
        ]))

    if message.asDisplay() == "简报":
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
        for n,i in enumerate(jb):
            JB.append(f'{n+1}、{i}')
        text = '\n'.join(JB)
        await app.sendGroupMessage(group,MessageChain.create([
            Plain(text)
        ]))