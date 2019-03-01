# import unittest
# from testsuites.base_testcase import BaseTeseCase
# from pageobjects.luntan_homepage import LuntanHomePage
# import time
# class luntanSearch(BaseTeseCase):
#     def test_luntan_seacrch(self):
#         h = LuntanHomePage(self.driver)  # 声明对象
#         h.get("http://127.0.0.1/forum.php")
#         h.login_search("admin","root")
#         time.sleep(3)
#         # h.fatie_search("小兵回家","小兵今天很棒哦！都能找到家了呢")
#         # h.huitie_search("我也发现了")
#         # h.logout_search()
#         # h.delete_tiezi()#删除帖子
#         # h.into_guanlizhongxin()
#         # h.add_bankuai_search()
#         # h.logout_search()#退出
#         # h.login_search("zhang","123456")#普通用户登录
#         # time.sleep(5)
#         # h.people_fatie("小红花","小兵今天上课得到了一朵小红花")
#         # h.huitie_search("好样的")
#         # h.toupiao_search("该不该休息","不该","该")
#         # h.get_piao_tittle_search()
#         # h.toupiao_bili_search()
#         h.select_tiezi_search("haotest")
#
# if __name__ == "__main__":
#     unittest.main()