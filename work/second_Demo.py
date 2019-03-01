from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import os

dir = os.path.dirname(__file__)
chrom_driver_path = dir + "\chromedriver.exe"
driver = webdriver.Chrome(chrom_driver_path)

try:
    driver.implicitly_wait(5)
    driver.get("https://www.baidu.com")

    send=driver.find_element_by_name("wd")
    send.send_keys("java")
    driver.find_element_by_id("su").click()
    print("百度首页已经打开：",driver.title)
    nums=driver.find_element_by_class_name("nums_text")

    wait_seconds=10
    driver.execute_script("window.alert(\"{}, {}秒后关闭\")".format(nums.text.replace("\n", "$"), wait_seconds))
finally:
    time.sleep(5)
    driver.quit()


