#!/usr/bin/python
# -*- coding: utf-8 -*

import logging
import tornado.web

logging.basicConfig(level=logging.DEBUG)


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('home.html', user=self.current_user)

