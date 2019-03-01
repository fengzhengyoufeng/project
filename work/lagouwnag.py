from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from  selenium.webdriver.support import expected_conditions  as EC
from selenium.webdriver.common.keys import Keys
import os

dir=os.path.dirname(__file__)
chrom_driver_path=dir+"\chromedriver.exe"
driver=webdriver.Chrome(chrom_driver_path)
try:
    driver.implicitly_wait(5)
    driver.get("https://www.lagou.com/zhaopin/Java/?labelWords=label")
    window_list=driver.current_window_handle
    driver.switch_to.window(window_list)
    while True:
        jobs = driver.find_elements_by_css_selector((".p_top h3"))
        for job in jobs:
            job.click()
            driver.switch_to.window(driver.window_handles[1])#切换至新打开的页面
            # driver.find_element_by_css_selector((".position-content-l"))
            job_name=driver.find_element_by_css_selector(".name")
            job_company=driver.find_element_by_css_selector(".company")
            job_money=driver.find_element_by_css_selector("dd .salary")
            print("公司：",job_company.text,"\n工作名：",job_name.text,"\n薪资：",job_money.text,)
            driver.close()#关掉新打开的页面
            driver.switch_to.window(window_list)
        next_page=WebDriverWait(driver,10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR,".item_con_pager .pager_container > *:last-child")))
        next_page_class=next_page.get_attribute("class")
        if "pager_next_disabled"in next_page_class:
                break
finally:
    pass