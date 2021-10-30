# 作者： 迷路的小怪兽
# 创建时间： 2021/10/20 21:41
import time
from src.common.getlog import MyLog


urls = {
    '': '没有起始URL，请检查',
    'home_page': 'http://www.baidu.com/',
    'first_page': 'xxxx',
}


class Para:

    username = 'xxxx'
    password = 'xxxx'

    def __init__(self, **kws):
        for key, value in kws.items():
            command = f"self.{key} = '{value}'"
            exec(command)


class BaseFlow:

    start_page = ''
    end_page = ''

    # 初始化驱动和起始url
    def __init__(self, name, driver, para=None):
        self.flow_name = name
        self.driver = driver
        if para is not None:
            self.para = para
        else:
            self.para = Para()
        self.start_urls = urls[self.start_page]
        self.log = MyLog()

    # 流程的装饰器，用于日志记录流程开始与结束
    def flow_log(func):
        def log_(self):
            self.log.info(f"流程：'{self.flow_name}' 开始执行！")
            func(self)
            self.log.info(f"流程：'{self.flow_name}' 执行结束！")

        return log_

    # 流程执行函数,子类的此函数必须使用flow_log装饰
    def execute(self):
        pass

    # 流程结束返回断言需要的内容作为流程对象的属性
    def _get_output(self):
        pass

    # 流程结束设置流程结束页面
    def _set_end_page(self):
        pass

    # 判断是否起始页面
    def _is_start_page(self, page):
        if self.start_page == page:
            return True
        else:
            return False

    # 有当前页面返回到首页
    def _back_to_homepage(self):
        self.driver.get(urls['home_page'])

    # 由首页跳转到起始页
    def _homepage_to_start_page(self):
        pass

    # 以上一流程的结束页经处理跳转到当前流程的起始页
    def with_start_page(self, page):
        if not self._is_start_page(page):
            self._back_to_homepage()
            time.sleep(1)
            self._homepage_to_start_page()

        return self


