# coding: utf-8

"""

客户端
接收任务包，进行扫描，上传结果

"""

import os
import requests
import urllib2

os.path.join(os.getcwd())

from config import SERVER, MONGODB, NOSERVER, PLUGINS
from mlog import logger
from plugin import Plugin
from logo import LOGO1


class Client(object):
    def __init__(self):
        print LOGO1
        logger.info("Init client")
        self.plugins = self.load_plugins()

        if not NOSERVER:
            connect = self.server_connection() and self.db_connection()
        else:
            pass


    @staticmethod
    def server_connection():
        connect = False
        return connect


    @staticmethod
    def db_connection():
        connect = False
        return connect


    @staticmethod
    def load_plugins():
        plugins = []
        for p in PLUGINS:
            plugin = Plugin(name=p.get("name"), rootpath=p.get("rootpath"), plugin_id=p.get("plugin_id"))
            plugins.append(plugin)
        return plugins


if __name__ == '__main__':
    cln = Client()


