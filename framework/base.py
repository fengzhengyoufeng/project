from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from  framework.logger import Logger
import os
import time
logger= Logger(logger="BasePage").getlogger()
class BasePage(object):

    def __init__(self,driver):
        self.driver=driver

    def sendkeys(self,text,*loc): #输入
        el=self.driver.find_element(*loc)
        el.clear()
        el.send_keys(text)
        try:
            # logger.info("Successful text input")
            logger.info("输入内容:%s",text)
        except:
            logger.info("failed to type in input box with")


    def clear(self,*loc):    #清空
        cl=self.driver.find_element(*loc)
        try:
            cl.clear()
            logger.info("Textbox data has been cleared ")
        except:
            logger.info("failed to clear this box with")

    def back(self):     #后退
        self.driver.back()
        logger.info("Click back on current page")
    def forward(self):  #前进
        self.driver.forward()
        logger.info("Click back on current page")
    def quit(self):     #关闭浏览器
        self.driver.quit()
        logger.info("quit successful")

    def close(self):    #关闭当前页面
        self.driver.close()
        logger.info("close successful")

    def click(self,*loc):   #点击页面元素
        try:
            el = self.driver.find_element(*loc)
            el.click()
            logger.info("successful click")
        except Exception as e:
            logger.info("not finding this element:%s"%e)

            # el = self.driver.find_element(*loc)
            # el.click()
            # # logger.info("click successful")

    def find_element(self,*loc): #
        try:
            WebDriverWait(self.driver,6).until(EC.visibility_of_element_located(loc))
            logger.info("finding this element")
            return self.driver.find_element(*loc)
        except Exception as e:
            logger.info("not finding this element%s"%e)

    def get(self,url):#
        self.driver.get(url)
        logger.info(url)

    def get_windows_img(self):
        file_path = os.path.dirname(os.path.abspath('.')) + ' /screenshots/'
        rq = time.strftime(' %Y%m%d%H%M',time.localtime (time.time()))
        screen_name= file_path + rq+'.png'
        try:
            self.driver.get_screenshot_as_file(screen_name)
            logger.info("Had take screenshots and save to folder : /screenshots")
        except Exception as e:
            self.get_windows_img()
            logger.error("Pailed to take scIeenshot!")

    # def now_window(self):
    #     self.
    def switch_windows(self,num):
        handles = self.driver.window_handles  # 获取当前窗口句柄集合（列表类型）
        self.driver.switch_to.window(handles[num])
        logger.info("Window switch to current")

    def getText(self,*loc):
        ssa=self.find_element(*loc)
        return ssa.text
    def iframe(self,*loc):
        try:
            login=self.find_element(*loc)
            self.driver.switch_to.frame(login)
            logger.info("goto iframe")
        except:
            logger.info("no find the iframe")


