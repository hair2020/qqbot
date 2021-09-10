from graia.application.message.elements.internal import At, Plain,Image
from graia.application.message.chain import MessageChain
from graia.application.group import Group, Member
from graia.application.message.parser.kanata import Kanata
from graia.application.message.parser.signature import FullMatch, RequireParam
from core import *
import random
import os


__plugin_name__ = '抽奖'
__plugin_usage__ = '输入抽奖'

bcc = get.bcc()
@bcc.receiver("GroupMessage")
async def choujiang(
    message:MessageChain,
    group:Group,
    app:GraiaMiraiApplication,
    member:Member   
):  
    if message.asDisplay().startswith("抽奖"):
        pic_folder = r'D:\hair\qqbot\data\pic_choujiang/'
        x = random.randint(1,100000)
        if x<=255: #非凡
            pic_folder = pic_folder+'feifan/'
            types = '非凡'
        elif x>255 and x<=892:
            pic_folder = pic_folder+'yinmi/'
            types = '隐秘'
        elif x>892 and x<= 4079:
            pic_folder = pic_folder+'baomi/'
            types = '保密'
        elif x>4079 and x<= 20016:
            pic_folder = pic_folder+'shouxian/'
            types = '受限'
        elif x>20016 and x<= 100000:
            pic_folder = pic_folder+'junjian/'
            types = '军规'
        pics = os.listdir(pic_folder)
        pic_paths = []
        for i in pics:
            pic_paths.append(pic_folder+i)
        fin_pic = random.choice(pic_paths)
        await app.sendGroupMessage(group,MessageChain.create([
            Plain(f"你抽到了{types}级别的物品!"),Image.fromLocalFile(fin_pic)
        ]))
    if message.asDisplay().startswith("十连"):
        for i in range(10):
            pic_folder = r'C:/Users/vllbc/Desktop/qqbot/data/pic_choujiang/'
            x = random.randint(1,100000)
            if x<=255+i*100: #非凡
                pic_folder = pic_folder+'feifan/'
                types = '非凡'
            elif x>255+i*100 and x<=892+i*100:
                pic_folder = pic_folder+'yinmi/'
                types = '隐秘'
            elif x>892+i*100 and x<= 4079+i*100:
                pic_folder = pic_folder+'baomi/'
                types = '保密'
            elif x>4079+i*100 and x<= 20016+i*100:
                pic_folder = pic_folder+'shouxian/'
                types = '受限'
            elif x>20016+i*100 and x<= 100000:
                pic_folder = pic_folder+'junjian/'
                types = '军规'
            pics = os.listdir(pic_folder)
            pic_paths = []
            for i in pics:
                pic_paths.append(pic_folder+i)
            fin_pic = random.choice(pic_paths)
            await app.sendGroupMessage(group,MessageChain.create([
                Plain(f"你抽到了{types}级别的物品!"),Image.fromLocalFile(fin_pic)
            ]))
    
