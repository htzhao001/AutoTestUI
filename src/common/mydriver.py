# 作者： 迷路的小怪兽
# 创建时间： 2021/10/20 21:40
from selenium import webdriver
import os
from src.common.getlog import MyLog


class MyDriver:
    """
    初始化浏览器驱动，打开浏览器
    """
    mode = 'normal'

    def __init__(self, mode=None, wait_time=10):
        """
        设置浏览器模式与默认等待时间
        :param mode: 浏览器模式，‘headless’为无界面模式
        :param wait_time: 元素隐式等待时间
        """
        if mode is not None:
            self.mode = mode
        self.wait_time = wait_time
        self.log = MyLog()

    def chrome_browser(self, driver_path=None):
        """
        打开浏览器
        :param driver_path: 浏览器驱动路径
        :return: 浏览器对象
        """
        if driver_path is not None:
            exe_path = driver_path
        else:
            exe_path = os.path.abspath('.').split('AutoTestUI')[0] + \
                       'AutoTestUI\\lib\\chromedriver.exe'

        if self.mode.lower() == 'headless':
            option = webdriver.ChromeOptions()
            option.add_argument('--headless')

            driver = webdriver.Chrome(executable_path=exe_path,
                                      chrome_options=option)
        else:
            driver = webdriver.Chrome(executable_path=exe_path)

        driver.implicitly_wait(self.wait_time)
        driver.maximize_window()

        self.log.info('谷歌浏览器已打开！')
        return driver
