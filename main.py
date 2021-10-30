# 作者： 迷路的小怪兽
# 创建时间： 2021/10/20 21:33
import os
import time
import unittest
from lib.HTMLTestReportCN import HTMLTestRunner


def run():
    report_dir = f"{os.path.abspath('.').split('AutoTestUI')[0]}AutoTestUI\\reports\\reports\\{time.strftime('%Y%m%d')}"
    if not os.path.exists(report_dir):
        os.makedirs(report_dir)
    report_name = f"{report_dir}\\UI-test_report-{time.strftime('%H%M%S')}.html"
    with open(report_name, 'w', encoding='utf-8') as fp:
        runner = HTMLTestRunner(fp,
                                title='自动化UI测试报告',
                                description='win10 64bit 谷歌浏览器95',
                                tester='迷路的小怪兽')
        discover = unittest.defaultTestLoader.discover(start_dir='./src/cases',
                                                       pattern='test_baidu_home*')
        runner.run(discover)

if __name__ == '__main__':
    run()