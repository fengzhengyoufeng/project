import unittest
from pageobjects.luntan_homepage import LuntanHomePage
from testsuites.base_testcase import BaseTeseCase
import time
class Test_forum3_earch(BaseTeseCase):
    def test_forum3_earce(self):
        h = LuntanHomePage(self.driver)  # 声明对象
        # h.get("http://127.0.0.1/forum.php")
        h.login_search("admin", "root")
        time.sleep(3)
        h.select_tiezi_search("hao")


if __name__=="__main__":
    unittest.main()