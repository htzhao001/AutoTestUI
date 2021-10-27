# 作者： 迷路的小怪兽
# 创建时间： 2021/10/20 21:40
import unittest
import time
import inspect
import os
from src.common.mydriver import MyDriver


class MyTest(unittest.TestCase):

    # 这里直接把浏览器给初始化，就不用在每个用例的setUpClass中重复初始化
    driver = MyDriver().chrome_browser()

    # 增加截图装饰器--内容比较
    def photo(func):
        def take_pic(self, first, second, msg, driver):
            try:
                func(self, first, second, msg)
            except AssertionError as e:
                file_dir = f"{os.path.abspath('.').split('AutoTestUI')[0]}AutoTestUI\\reports\\screenshots\\{time.strftime('%Y%m%d')}\\"
                if not os.path.exists(file_dir):
                    os.makedirs(file_dir)
                file_name = f'{file_dir}{inspect.stack()[1][3]}-{time.strftime("%H%M%S")}.png'
                driver.get_screenshot_as_file(file_name)

                raise AssertionError
        return take_pic

    # 增加截图装饰器--表达式
    def photo_1(func):
        def take_pic(self, expr, msg, driver):
            try:
                func(self, expr, msg)
            except AssertionError as e:
                file_dir = f"{os.path.abspath('.').split('AutoTestUI')[0]}AutoTestUI\\reports\\screenshots\\{time.strftime('%Y%m%d')}\\"
                if not os.path.exists(file_dir):
                    os.makedirs(file_dir)
                file_name = f'{file_dir}{inspect.stack()[1][3]}-{time.strftime("%H%M%S")}.png'
                driver.get_screenshot_as_file(file_name)

                raise AssertionError

        return take_pic

    # 装饰各个断言方法
    @photo
    def assertEqual_(self, first, second, msg):
        self.assertEqual(first, second, msg)

    @photo
    def assertNotEqual_(self, first, second, msg):
        self.assertNotEqual(first, second, msg)

    @photo
    def assertIn_(self, first, second, msg):
        self.assertIn(first, second, msg)

    @photo
    def assertNotIn_(self, first, second, msg):
        self.assertNotIn(first, second, msg)

    @photo_1
    def assertTrue_(self, expr, msg):
        self.assertTrue(expr, msg)

    @photo_1
    def assertFalse_(self, expr, msg):
        self.assertFalse(expr, msg)