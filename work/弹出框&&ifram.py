from selenium import webdriver
import time
# driver=webdriver.Chrome(".\\chromedriver.exe")
# driver.get("https://mail.163.com/")
# login=driver.find_element_by_tag_name("iframe")
# driver.switch_to.frame(login)
# driver.find_element_by_name("email").send_keys("16546846")


#弹出框
driver=webdriver.Chrome(".\\chromedriver.exe")
driver.get("https://www.baidu.com/")
time.sleep(2)
driver.execute_script("window.alert('请输入您的密码')")
time.sleep(2)

driver.switch_to.alert.accept()#点击弹出框中的确定按钮
driver.switch_to.alert.dismiss()#点击弹出框上的关闭按钮