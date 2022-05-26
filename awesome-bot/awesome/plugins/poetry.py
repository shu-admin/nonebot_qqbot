
from nonebot import on_command,CommandSession
import json,requests

@on_command('poetry',aliases =('诗','诗词'))
# 以poetry为命令，可以使用'诗','诗词'别名
async def poetry(session:CommandSession):
    poetryText = await getPoetryText()
    await session.send(poetryText)


async def getPoetryText():
    #此函数返回一句诗词
    url = 'https://v2.jinrishici.com/one.json?'
    response = requests.get(url)
    response.raise_for_status()
    poetryData = json.loads(response.text)
    info = poetryData
    poetryAuthor = poetryData['data']['origin']['author']
    poetryContent = poetryData['data']['content']
    poetryDynasty = poetryData['data']['origin']['dynasty']
    # print(poetryContent+'\n----by'+poetryDynasty +''+ poetryAuthor)
    print(poetryData)
    return f'{poetryContent}\n----by {poetryDynasty} {poetryAuthor}'