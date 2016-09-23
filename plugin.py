# coding: utf-8

"""

扫描插件

"""

import os

os.path.join(os.getcwd())

from mlog import logger


class Plugin(object):
    def __init__(self, name=None, plugin_id=None, rootpath=None,):
        self.rootpath = rootpath
        self.name = name
        self.plugin_id = plugin_id

        if not self.load_plugin():
            logger.error("Load plugin %s failed" % name)
        else:
            logger.debug("Load Plugin %s " % name)

    def load_plugin(self):
        """
        加载模块
        :return:
        """
        load_success = False
        if os.path.isdir(self.rootpath):
            plugin_path = int(os.popen("which " + self.name + " | grep found | wc -l").read())
            if plugin_path != 0:
                load_success = True
        return load_success

    def handel_task(self):
        pass

    def start(self):
        pass


