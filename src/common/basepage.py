# 作者： 迷路的小怪兽
# 创建时间： 2021/10/20 21:41
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from src.common.getlog import MyLog


CLICK = 'click'
SEND_KEYS = 'send_keys'
JS_CLICK = 'js_click'
JS_SEND_KEYS = 'js_send_keys'
DOUBLE_CLICK = 'double_click'
CONTEXT_CLICK = 'context_click'
MOVE_TO = 'move_to'
FIND = 'find'
FINDS = 'finds'


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.log = MyLog()

    def _get_selector(self, selector_text):
        """
        解析定位信息
        :param selector_text:
        :return:
        """
        method = ''
        if '=>' not in selector_text:
            method = By.ID
            selector = selector_text
        else:
            method_text = selector_text.split('=>')[0]
            selector = selector_text.split('=>')[1]
            if method_text == 'xpath' or method_text == 'x':
                method = By.XPATH
            elif method_text == 'id' or method_text == 'i':
                method = By.ID
            elif method_text == 'css' or method_text == 'c':
                method = By.CSS_SELECTOR
            elif method_text == 'text' or method_text == 't':
                method = By.PARTIAL_LINK_TEXT
            elif method_text == 'name' or method_text == 'n':
                method = By.NAME
            elif method_text == 'class' or method_text == 'cl':
                method = By.CLASS_NAME
            elif method_text == 'tagname' or method_text == 'tag':
                method = By.TAG_NAME
            else:
                self.log.error(f'定位信息有误！请检查 {selector_text}')
        self.log.debug(f"已完成定位方式解析,定位方式：{method}; 定位信息：'{selector}'")
        return method, selector

    def _find(self, selector_text):
        """
        查找单个元素
        :param selector_text:
        :return:
        """
        method, selector = self._get_selector(selector_text)
        try:
            ele = self.driver.find_element(method, selector)
            self.log.info(f"已找到元素 '{ele.text}'。")
            return ele
        except Exception as msg:
            self.log.warning(f'查找元素失败！请检查页面是否正常加载或等待时间是否合适。信息：{msg}')

    def _finds(self, selector_text):
        """
        查找一组元素
        :param selector_text:
        :return:
        """
        method, selector = self._get_selector(selector_text)
        try:
            ele_list = self.driver.find_elements(method, selector)
            self.log.info(f"已找到元素组。")
            return ele_list
        except Exception as msg:
            self.log.warning(f'查找元素失败！请检查页面是否正常加载或等待时间是否合适。信息：{msg}')

    def get(self, url):
        """
        访问网址
        :param url:
        :return:
        """
        self.driver.get(url)
        self.log.info(f'已成功访问url：{url}')

    def get_title(self):
        """
        获取当前页面标题
        :return:
        """
        self.log.debug(f"以获取当前页面标题：{self.driver.title} 。")
        return self.driver.title

    # 页面前进
    def forward(self):
        self.log.debug(f"浏览器页面跳转后一页。")
        self.driver.forward()

    # 页面后退
    def back(self):
        self.log.debug(f"浏览器页面跳转前一页。")
        self.driver.back()

    # 跳转frame
    def to_frame(self, frame):
        try:
            self.driver.switch_to.frame(frame)
            self.log.info(f"浏览器页面跳至内嵌frame页面。")
        except Exception as msg:
            self.log.error(f"跳转内嵌frame失败，信息：{msg}")

    # 跳回上一层frame
    def to_parent_frame(self):
        self.driver.switch_to.parent_frame()
        self.log.info(f"浏览器页面跳至上一层frame页面。")

    # 跳回最外层frame
    def out_frame(self):
        self.driver.switch_to.default_content()
        self.log.info(f"浏览器页面跳至最外层frame页面。")

    # 跳转警告窗口
    def to_alert(self):
        try:
            self.driver.switch_to.alert()
            self.log.info(f"浏览器页面跳至警告弹窗。")
        except Exception as msg:
            self.log.error(f"跳转警告弹窗失败，信息：{msg}")

    # 接受警告窗口
    def alert_accept(self):
        self.driver.switch_to.alert.accept()
        self.log.warning(f"警告弹窗已接受。")

    # 取消警告窗口
    def alert_dismiss(self):
        self.driver.switch_to.alert.dismiss()
        self.log.warning(f"警告弹窗已取消。")

    # 执行js语句
    def _js(self, js_):
        try:
            self.driver.execute_script(js_)
            self.log.info(f"已成功执行js语句：{js_}")
        except Exception as msg:
            self.log.error(f"执行语句:'{js_}'失败！报错信息为：{msg}")

    # 页面截图
    def get_screenshots(self, file_path):
        self.driver.get_screenshot_as_file(file_path)
        self.log.info(f"已成功截图当前页面！")

    # 右键动作
    def _context_click(self, selector):
        ele = self._find(selector)
        try:
            ActionChains(self.driver).context_click(ele).perform()
            self.log.info(f"已成功右键点击元素：{ele.text}。")
        except Exception as msg:
            self.log.error(f"右键点击元素 '{ele.text}' 失败！报错信息为：{msg}")

    # 拖动动作
    def _drop_to_point(self, selector, point):
        pass

    # 双击动作
    def _double_click(self, selector):
        ele = self._find(selector)
        try:
            ActionChains(self.driver).double_click(ele).perform()
            self.log.info(f"已成功双击元素：{ele.text}。")
        except Exception as msg:
            self.log.error(f"双击元素 '{ele.text}' 失败！报错信息为：{msg}")

    # 移动至动作
    def _move_to(self, selector):
        ele = self._find(selector)
        try:
            ActionChains(self.driver).move_to_element(ele).perform()
            self.log.info(f"鼠标已成功移动至元素：{ele.text} 处。")
        except Exception as msg:
            self.log.error(f"鼠标移动到 '{ele.text}' 失败！报错信息为：{msg}")

    # 统一动作--点击
    def _click(self, selector):
        ele = self._find(selector)
        try:
            ele.click()
            self.log.info(f"已成功点击元素：{ele.text} 。")
        except Exception as msg:
            self.log.error(f"点击元素： '{ele.text}' 失败！报错信息为：{msg}")

    # 统一动作--输入值
    def _send_keys(self, selector, value):
        ele = self._find(selector)
        try:
            ele.send_keys(value)
            self.log.info(f"已成功在输入框中输入：{value} 。")
        except Exception as msg:
            self.log.error(f"输入内容： '{value}' 失败！报错信息为：{msg}")

    # 统一动作--js点击
    def _js_click(self, selector):
        method, selector_text = self._get_selector(selector)
        if method == By.XPATH:
            js_ = f"document.evaluate('{selector_text}', document).iterateNext().click();"
        elif method == By.CSS_SELECTOR:
            js_ = f"document.querySelector('{selector_text}').click();"
        else:
            js_ = f"console.log('{method}: {selector_text} 无效')"
            self.log.warning(f'定位方式有误！只能使用xpath或者css。当前定位方式为: {method}')
        self._js(js_)

    # 统一动作--js输入值
    def _js_send_keys(self, selector, value):
        """
        使用js语句给输入框输入内容，一般富文本框输入会用到，如果innerText不可以，可以试试其他方法
        :param selector: 定位文本
        :param value: 输入内容
        :return:
        """
        method, selector_text = self._get_selector(selector)
        if method == By.XPATH:
            js_ = f"document.evaluate('{selector_text}', document).iterateNext().innerText() = '{value}';"
        elif method == By.CSS_SELECTOR:
            js_ = f"document.querySelector('{selector_text}').innerText() = '{value}';"
        else:
            js_ = f"console.log('{method}: {selector_text}  输入:{value}失败！')"
            self.log.warning(f'定位方式有误！只能使用xpath或者css。当前定位方式为: {method}')
        self._js(js_)

    # 统一动作装饰器函数
    """
    该装饰器提供了统一的元素交互方式，普通点击与输入，JS的点击与输入，没有关键字则返回原函数内容
    """
    def action(func):
        def deal(self, action_=None, value=None):
            # 若动作词没有输入，则返回定位字符串
            if action_ is None:
                return func(self)

            if action_ == 'click':
                self._click(func(self))
            elif action_ == 'send_keys':
                self._send_keys(func(self), value)
            elif action_ == 'js_click':
                self._js_click(func(self))
            elif action_ == 'js_send_keys':
                self._js_send_keys(func(self), value)
            elif action_ == 'double_click':
                self._double_click(func(self))
            elif action_ == 'context_click':
                self._context_click(func(self))
            elif action_ == 'move_to':
                self._move_to(func(self))
            elif action_ == 'find':
                self._find(func(self))
            elif action_ == 'finds':
                self._finds(func(self))
            else:
                self.log.warning(f'{action_}动作词无效！请检查动作词或向动作库中加入更多的交互动作吧！')

        return deal
