import unittest
from pageobjects.luntan_homepage import LuntanHomePage
from testsuites.base_testcase import BaseTeseCase
import time
class Test_forum2_earch(BaseTeseCase):
    def test_forum1_earce(self):
        h = LuntanHomePage(self.driver)  # 声明对象
        h.login_search("admin", "root")
        time.sleep(3)
        h.delete_tiezi()#删除帖子
        h.into_guanlizhongxin()#进入管理中心
        h.add_bankuai_search("asdfwe")#添加板块
        h.logout_search() # 退出
        h.login_search("zhang","123456")#普通用户登录
        time.sleep(3)
        h.people_fatie("小红花","小兵今天上课得到了一朵小红花")#发帖
        time.sleep(3)
        h.huitie_search("好样的")

if __name__==__file__:
    unittest.main()