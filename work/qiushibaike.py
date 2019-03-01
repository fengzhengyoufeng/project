from selenium import webdriver
import os
# 使用CSS选择器获取所有的笑话
dir=os.path.dirname(__file__)
chrom_driver_path = dir + "\chromedriver.exe"
driver = webdriver.Chrome(chrom_driver_path)
driver.maximize_window()
driver.implicitly_wait(5)
driver.get("https://www.qiushibaike.com/text/")
num=driver.find_element_by_css_selector(".pagination li:nth-last-child(2)").text
sum=int(num)
for i in range(1,sum+1):
    print("--------------第",i,"页---------------")
    jokes = driver.find_elements_by_css_selector(".content")
    writter = driver.find_elements_by_css_selector("h2")
    haoxiaoshu = driver.find_elements_by_css_selector(".stats-vote ")
    for a in range(0, len(jokes)):
        print("作者：\t", end="")
        print(writter[a].text)
        print(jokes[a].text)
        print(haoxiaoshu[a].text)
        print("\n")
    next_page = driver.find_element_by_css_selector(".pagination li:last-of-type")
    if next_page.text=="下一页":
        next_page.click()
    else:
        driver.quit()
