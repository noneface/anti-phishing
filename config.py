# coding: utf-8

"""

客户端配置文件

"""

# 服务器配置
SERVER = {
    "ip": "",
    "port": 2333,
    "path": {
        "connect": "/api/connect",
        "status": "/api/status"
    }
}


# MongoDB配置
MONGODB = {
    "ip": "",
    "port": 27017,
    "auth": {
        "username": "",
        "password": ""
    }
}


# 本地模块
PLUGINS = [
    {
        "name": "masscan",
        "rootpath": "",
        "plugin_id": 10,
        "output": ""
    },

    {
        "name": "zmap",
        "rootpath": "",
        "plugin_id": 11,
        "output": ""
    },

    {
        "name": "zgrab",
        "rootpath": "",
        "plugin_id": 12,
        "output": ""
    }
]


# 日志
LOG = {
    "file": "scan.log",

}


# 是否开启调试
DEBUG = True


# 是否独立运行
NOSERVER = True


# task struct
TASK = {
    'tid': "",

    'scan_status': 0,

    'info': {
        'name': "",
        'time': "",
        'author': ""
    },

    'detail': {
        'task_type': 10,
        'plugin_id': 1,
        'command': "",
        'ip': "",
        'port': 80,
        'scan_sum': 0

    }

}


RESULT = {
    'rid': "",
    'tid': "",
    'time': "",
    'is_error': 0,
    'error_message': "",
    'is_finished': 0,
    'datas': ""
}


STATUS = {
    'tid': "",
    'process': 0.0,
    'scaned': 0,
    'disscaned': 0,
    'is_error': 0,
    'is_finished': 0
}

