from selenium import webdriver
import os,time
#登录论坛
dir=os.path.dirname(__file__)
chrom_driver_path=(dir+"\chromedriver.exe")
driver=webdriver.Chrome(chrom_driver_path)
try:
    driver.implicitly_wait(5)
    driver.get("http://127.0.0.1/forum.php")
    driver.find_element_by_name("username").send_keys("admin")
    driver.find_element_by_name("password").send_keys("root")
    driver.find_element_by_css_selector("button em").click()
    name=driver.find_element_by_css_selector(".vwmy").text
    #默认板块发帖
    if "admin" in name:
        driver.find_element_by_xpath('//*[@id="category_1"]/table/tbody/tr[1]/td[2]/h2/a').click()
        window_list=driver.current_window_handle
        driver.switch_to.window(window_list)
        driver.find_element_by_class_name("px").send_keys("第一个帖子")
        driver.find_element_by_name("message").send_keys("大家好，初次见面请多关照")
        driver.find_element_by_css_selector(".ptm button").click()
    time.sleep(5)
    driver.find_element_by_css_selector(".pt").send_keys("回复一下")#输入回复
    driver.find_element_by_xpath('//*[@id="fastpostsubmit"]').click()#发表回复
    time.sleep(5)
    driver.find_element_by_xpath('//*[@id="um"]/p[1]/a[7]').click()#退出登录
    time.sleep(5)
finally:
    driver.quit()