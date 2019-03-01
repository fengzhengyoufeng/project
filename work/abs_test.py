import unittest
from work.abs import *
from ddt import ddt,data,unpack

@ddt
class absTestCase(unittest.TestCase):
    @classmethod
    def setUp(cls):
        print("测试开始")

    @data([-1,1],[1,1],[0,0])
    @unpack
    def test_abs(self,n,except_value):
        result=abs(n)
        self.assertAlmostEqual(result,except_value,msg=result)
    @classmethod
    def tearDown(cls):
        print("测试结束")