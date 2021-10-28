# 作者： 迷路的小怪兽
# 创建时间： 2021/10/28 22:46
from src.common.basepage import BasePage


class BaiduPage(BasePage):

    @BasePage.action
    def baidu_search_input(self):
        return 'kw'

    @BasePage.action
    def baidu_search_btn(self):
        return 'su'