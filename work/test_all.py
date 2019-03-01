import unittest
import  HTMLTestRunner
import os
from work.abs_test import absTestCase
from work.sort_test import SortTestcase
#设置报告文件的保存路径
cur_path=os.path.dirname(os.path.dirname(__file__))
report_path=os.path.join(cur_path,"report")
if not os.path.exists(report_path): os.mkdir(report_path)
#构造测试事件
suite= unittest.TestSuite()
suite.addTest(unittest.makeSuite(absTestCase))
suite.addTest(unittest.makeSuite(SortTestcase))

if __name__=="__main__":
    html_report = report_path + r"\result.html"
    fp = open(html_report, "wb")
    runner=HTMLTestRunner.HTMLTestRunner(stream=fp,verbosity=2,title="单元测试报告",description="用例执行情况")
    runner.run(suite)

