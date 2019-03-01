import unittest
#测试用例的目录
text_dir="./"
#加载测试用例
suite=unittest.TestLoader().discover(text_dir,pattern="*test.py")
if __name__=="__main__":
    #执行测试用例
    runner=unittest.TextTestRunner(verbosity=2)#verbosity=2详细输出执行  verbosity=0 不输出 verbosity=1简略输出
    runner.run(suite)
