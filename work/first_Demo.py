from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os


# 打开www.python.orj页面，并通过断言判断是否成功打开对应页面
# dir =os.path.dirname(__file__)
# chrom_driver_path = dir+"\chromedriver.exe"
# driver= webdriver.Chrome(chrom_driver_path)
# driver.get("https://www.python.org")
# assert "python" in driver.title
# print("登录成功")

# driver= webdriver.Chrome(".\chromedriver.exe")
# driver.get("https://www.baidu.com")
# a=driver.title
# if "百度" in a:
#     print("登录成功")
# else:
#     print("登录失败")
# 打开 www.yahoo.com 页面,进行页面判断，在搜索输入框中，输入seleniumhq 与回车键，进行搜索
dir = os.path.dirname(__file__)
chrom_driver_path=dir+"\chromedriver.exe"
driver=webdriver.Chrome(chrom_driver_path)
driver.get("http://www.yahoo.com")
sousuo=driver.find_element_by_name("p")
sousuo.send_keys(("seleniumhp")+Keys.RETURN)
# driver.find_element_by_name("p").send_keys("seleniumhp")
# driver.find_element_by_id("uh-search-button").click()
driver.close()#driver.quit()
print("搜索成功")

# #firfox自动化控制
# dir = os.path.dirname(__file__)
# ie_driver_path = dir + ".\geckodriver.exe"
# driver=webdriver.Firefox(ie_driver_path)
# driver.get("http://www.baidu.com")
# assert "Python" in driver.title

#IE自动化控制
# dir = os.path.dirname(__file__)
# ie_driver_path = dir + "\IEDriverServer.exe"
# driver=webdriver.Ie(ie_driver_path)
# driver.get("http://www.baidu.com")
# assert "Python" in driver.title
#  打开 www.baidu.com 页面，激活当前窗口，并输出百度首页已打开； 通过 id 查找搜索框，键入 java 并提交搜索；
# 获取页面中“百度已为您找到相关结果约 xxx 个”； 执行 js 脚本，显示一个框提示用户已经找到相关结果。
# driver = webdriver.Chrome(".\chromedriver.exe")
# driver.get("https://www.baidu.com")
# print("百度首页已打开")
# driver.find_element_by_id("kw").send_keys("java")
# driver.find_element_by_id("su").click()
#
