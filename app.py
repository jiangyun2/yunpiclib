#!/usr/bin/python
# -*- coding: utf-8 -*

import tornado.ioloop
import tornado.web
from tornado.options import define, options
from handlers import main

# 定义端口信息
define('port', default=8888, type=int, help="Listening port")
define('debug', default=True, type=bool, help="debug y/n")


class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r"/", main.MainHandler),
        ]
        settings = dict(
            # debug模式下，检测到代码改变将自动重启tornado
            debug=options.debug,
            # 模板
            template_path='templates',
            # 静态文件
            static_path='statics',
        )
        # 继承父类的init，主要起作用的是父类的init
        super().__init__(handlers=handlers, **settings)


if __name__ == "__main__":
    app = Application()
    # 命令行参数转换
    tornado.options.parse_command_line()
    # 控制台输出port
    print("Server start on port {}".format(options.port))
    app.listen(options.port)
    tornado.ioloop.IOLoop.current().start()