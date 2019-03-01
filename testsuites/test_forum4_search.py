import unittest
from pageobjects.luntan_homepage import LuntanHomePage
from testsuites.base_testcase import BaseTeseCase
import time
class Test_forum4_earch(BaseTeseCase):
    def test_forum4_earce(self):
        h = LuntanHomePage(self.driver)  # 声明对象
        # h.get("http://127.0.0.1/forum.php")
        h.login_search("admin", "root")
        time.sleep(3)
        h.toupiao_search("该不该休息","不该","该")
        h.get_piao_tittle_search()
        h.toupiao_bili_search()



if __name__=="__main__":
    unittest.main()