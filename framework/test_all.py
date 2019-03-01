import unittest
import  HTMLTestRunner
import os
from testsuites.test_forum1_search import Test_forum1_earch
from testsuites.test_forum2_search import  Test_forum2_earch
from testsuites.test_forum3_search import Test_forum3_earch
from testsuites.test_forum4_search import Test_forum4_earch

#设置报告文件的保存路径
cur_path=os.path.dirname(os.path.dirname(__file__))
report_path=os.path.join(cur_path,"report")
if not os.path.exists(report_path): os.mkdir(report_path)#如果不存在就创建一个
#构造测试事件
suite= unittest.TestSuite()
suite.addTest(unittest.makeSuite(Test_forum1_earch))
suite.addTest(unittest.makeSuite(Test_forum2_earch))
suite.addTest(unittest.makeSuite(Test_forum3_earch))
suite.addTest(unittest.makeSuite(Test_forum4_earch))

if __name__=="__main__":
    '''测试'''
    html_report = report_path + r"\result.html"
    fp = open(html_report, "wb")
    runner=HTMLTestRunner.HTMLTestRunner(stream=fp,verbosity=2,title="单元测试报告",description="用例执行情况")
    runner.run(suite)

