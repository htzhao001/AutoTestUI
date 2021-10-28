# 作者： 迷路的小怪兽
# 创建时间： 2021/10/28 23:25
from src.common.baseflow import BaseFlow
from src.common.basepage import CLICK,SEND_KEYS,JS_SEND_KEYS,JS_CLICK,DOUBLE_CLICK,CONTEXT_CLICK,MOVE_TO
from src.pages.baidu_page import BaiduPage


class PrepareFlow(BaseFlow):

    start_page = 'home_page'

    def execute(self):
        page = BaiduPage(self.driver)
        page.get(self.start_urls)
        self._set_end_page()

    def _set_end_page(self):
        self.end_page = 'home_page'