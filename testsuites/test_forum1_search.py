import unittest
from pageobjects.luntan_homepage import LuntanHomePage
from testsuites.base_testcase import BaseTeseCase
import time
class Test_forum1_earch(BaseTeseCase):
    def test_forum1_earce(self):
        h = LuntanHomePage(self.driver)  # 声明对象
        h.login_search("admin", "root")
        time.sleep(3)
        h.fatie_search("abs","士大夫各色如何如何速度非常")
        h.huitie_search("我也发现了")
        h.logout_search()



if __name__=="__file__":
    unittest.main()