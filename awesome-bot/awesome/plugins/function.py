from nonebot import on_command,CommandSession
import json,requests

@on_command('function',aliases =('开启','打开','功能','你会干什么','你有什么功能'))
# 以function为命令，可以使用'开启','打开','功能','你会干什么','你有什么功能'别名
async def function(session:CommandSession):
    functionText = await getFunctionText()
    await session.send(functionText)


async def getFunctionText():
    #此函数返回机器人的功能

    return f'1.输出提问信息--Command(echo  "xxx")\n \
        2.查询天气--Command(天气 城市)\n \
        3.每日一词--Command(诗词)'