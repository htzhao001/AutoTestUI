# 作者： 迷路的小怪兽
# 创建时间： 2021/10/30 13:01
from src.common.baseflow import BaseFlow


class AfterMathFlow(BaseFlow):

    @BaseFlow.flow_log
    def execute(self):
        self.driver.quit()
