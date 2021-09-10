from graia.application.session import Session
from core import *
from pathlib import Path

init(Session(
        host="http://localhost:8000", # 填入 httpapi 服务运行的地址
        authKey="muchhair",
        account=2732631493, # 你的机器人的 qq 号
        websocket=True, # Graia 已经可以根据所配置的消息接收的方式来保证消息接收部分的正常运作.
        debug_flag=True  
    ))
app = get.app()
# load_plugins(Path('App'),
#              active_groups = [773580302,876117114,704240183,764839290,1038201434])
load_plugins(Path('App'),
             )
while True:
    try:
        app.launch_blocking()  
    except KeyboardInterrupt:
        pass
