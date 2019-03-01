import unittest
from testsuites.base_testcase import BaseTeseCase
from pageobjects.baidu_homepage import HomePage


class BaiduSearch(BaseTeseCase):
    def test_baidu_search(self):
        home_page=HomePage(self.driver)#声明对象
        # h.get("https://www.baidu.com")
        home_page.search("selenium")#执行搜索功能




if __name__=="__main__":
    unittest.main()