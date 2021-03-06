# AutoTestUI
本项目是基于业务流程的自动化UI测试项目，在原来市场常见的框架上加以创新与改进而来。
希望在阅读完本项目，能够对你的自动化知识有一些帮助。
由于作者水平与认知有限，目前本项目还不够完善，有部分功能和流程会存在一些不足。
欢迎您提出自己宝贵的建议，联系方式：921043431@qq.com

本项目整体思路是：用例执行是基于业务流程的描述。
我们在编写功能测试用例时，一般情况下都是业务流程的组合，很少有人会把每一步详细步骤都写出来，
那样会大大降低写用例的效率，拖慢工作进度，而且给用例执行人员的阅读也带来了一定的麻烦。
用例编写要求简洁明要，以最少的文字描述清楚测试条件步骤等内容。
例如：1、登陆系统；2、在某区域搜索指定内容查看结果。这种业务流程更符合我们在实际测试的应用。
我们的用例在编写时，测试步骤应该是这个样子的：用什么参数执行什么流程、用什么参数执行什么流程…
本框架就是基于此思路来开发的。

# 版本v1.0：
1、增加断言失败自动截图功能：
    重写了断言方法，新的断言方法增加了下划线后缀
    增加了断言失败自动截图的装饰器
    使用装饰器装饰重写的新断言方法

2、统一了元素交互动作的调用方式：
    页面元素函数返回值变化为定位文本字符串
    页面元素函数需要元素交互操作装饰器装饰
    页面基类增加元素交互动作变量
    页面基类增加元素交互操作装饰器

3、增加了业务流程模块：
    增加了业务流程基类
    增加流程开始结束日志记录的装饰器
    子类execute函数需要使用日志记录装饰器装饰
