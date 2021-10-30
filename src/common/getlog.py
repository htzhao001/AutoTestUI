# 作者： 迷路的小怪兽
# 创建时间： 2021/10/20 21:40
import logging
import os
import time


class MyLog:

    def __init__(self):
        file_name = f"{os.path.abspath('.').split('AutoTestUI')[0]}AutoTestUI\\log\\{time.strftime('%Y%m%d')}.log"
        self.log = logging.getLogger()
        self.log.setLevel(logging.DEBUG)
        # 日志格式：可以根据需要调整(文件名-函数名)
        log_str = logging.Formatter('%(levelname)s: %(filename)s - %(funcName)s - %(lineno)d - %(asctime)s : %(message)s')

        stream_handle = logging.StreamHandler()
        stream_handle.setLevel(logging.INFO)
        stream_handle.setFormatter(log_str)

        file_handle = logging.FileHandler(file_name, encoding='utf-8')
        file_handle.setLevel(logging.DEBUG)
        file_handle.setFormatter(log_str)

        if not self.log.hasHandlers():
            self.log.addHandler(stream_handle)
            self.log.addHandler(file_handle)

    def debug(self, msg):
        self.log.debug(msg)

    def info(self, msg):
        self.log.info(msg)

    def warning(self, msg):
        self.log.warning(msg)

    def error(self, msg):
        self.log.error(msg)

    def critical(self, msg):
        self.log.critical(msg)