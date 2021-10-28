# 作者： 迷路的小怪兽
# 创建时间： 2021/10/28 22:49
from src.common.baseflow import BaseFlow
from src.pages.baidu_page import BaiduPage
from src.common.basepage import CLICK,SEND_KEYS,JS_CLICK,JS_SEND_KEYS,DOUBLE_CLICK,CONTEXT_CLICK,MOVE_TO


class SearchFlow(BaseFlow):

    start_page = 'home_page'

    def execute(self):
        home_page = BaiduPage(self.driver)
        home_page.baidu_search_input(SEND_KEYS, self.para.keywords)
        home_page.baidu_search_btn(CLICK)
        self._set_end_page()
        self._get_output()

    def _set_end_page(self):
        self.end_page = 'search_page'

    # def _get_output(self):
    #     self.key = 'value'