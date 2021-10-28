# 作者： 迷路的小怪兽
# 创建时间： 2021/10/28 23:00
from src.common.mytest import MyTest
from src.common.baseflow import Para
from src.flows.prepare_flow import PrepareFlow
from src.flows.baidu_home_flow import SearchFlow


class TestBaiduFlows(MyTest):

    para = Para(
        keywords='selenium'
    )

    @classmethod
    def setUpClass(cls):
        cls.prepare_flow = PrepareFlow(cls.driver)
        cls.prepare_flow.execute()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_search_flow(self):
        search_flow = SearchFlow(self.driver, self.para)
        search_flow.with_start_page(self.prepare_flow.end_page).execute()
        self.assertEqual_('test', 'test', msg='测试消息', driver=self.driver)