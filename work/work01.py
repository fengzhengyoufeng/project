# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# import os
# import re
#
# # 我们要在百度首页找到所有的链接，并输出链接文字。
# dir=os.path.dirname(__file__)
# chrom_driver_path = dir + "\chromedriver.exe"
# driver = webdriver.Chrome(chrom_driver_path)
# driver.get("https://www.baidu.com")
# chaolianjie=driver.find_elements_by_tag_name("a")
# print("所有的超链接如下：\n")
# for a in chaolianjie:
#     print(a.text)
#
# # 在百度页面-联系我们网页中，摘取全部邮箱，使用代码来实现上述过程
# dir=os.path.dirname(__file__)
# chrom_driver_path = dir + "\chromedriver.exe"
# driver = webdriver.Chrome(chrom_driver_path)
# driver.implicitly_wait(5)# 操作等待超时时间
# driver.get("https://www.baidu.com")
# driver.maximize_window()#最大化窗口
# driver.find_element_by_link_text("关于百度").click()
# driver.find_element_by_link_text("联系我们").click()
# for handle in driver.window_handles:
#     driver.switch_to_window(handle)
# mail=driver.find_elements_by_class_name("mail-content-text")
# for a in mail:
#     str=a.text
#     if "@"in str:
#         print(str)
#
#
# #利用正则表达式方法


