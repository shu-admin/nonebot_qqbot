from os import path
import nonebot
import config
if __name__ == '__main__':
    nonebot.init(config)
    nonebot.load_builtin_plugins()
    nonebot.load_plugins(
        path.join(path.dirname(__file__),'awesome','plugins'),
        'awesome.plugins'
    )
    """
    这里的重点在于 nonebot.load_plugins() 函数的两个参数。
    第一个参数是插件目录的路径，
    这里根据 bot.py 的所在路径和相对路径拼接得到；
    第二个参数是导入插件模块时使用的模块名前缀，
    这个前缀要求必须是一个当前 Python 解释器可以导入的模块前缀，
    NoneBot 会在它后面加上插件的模块名共同组成完整的模块名来让解释器导入，
    因此这里我们传入 awesome.plugins，
    当运行 bot.py 的时候，
    Python 解释器就能够正确导入 awesome.plugins.weather 
    这个插件模块了。
    """
    nonebot.run()