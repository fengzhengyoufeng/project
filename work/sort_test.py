import unittest
from work.sort import *
from ddt import  ddt,data,unpack
@ddt
class SortTestcase(unittest.TestCase):
    def setUp(self):
        print("测试开始----------")

    @data([0,0,0],[1,0,2],[1,1,10],[1,2,20])
    @unpack
    def test_sort(self,a,b,except_value):
        result=sort(a,b)
        self.assertAlmostEqual(result,except_value,msg=result)

    def tearDown(self):
        print("测试结束。。。。。。。")