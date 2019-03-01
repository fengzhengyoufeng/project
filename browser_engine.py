import os.path
from configparser import ConfigParser
from  selenium import webdriver
from framework.logger import Logger

logger=Logger(logger='BasePage').getlogger()

class BrowserEngine(object):
    dir=os.path.dirname(os.path.abspath("."))
    firefox_path =dir+ '/tools/geckodriver.exe'
    Chrome_path = dir+'/tools/geckodriver.exe'
    IE_path = dir+'/tools/IEDriverServer.exe'
    # def __init__(self,driver):
    #     self.driver=driver
    def open_browser(self):
        config=ConfigParser()
        file=os.path.dirname((os.path.abspath('.'))+'/config/config.ini')
        config.read(file)
        browser=config.get('browserType','browserName')
        logger.info('chose browser：%s'%browser)
        url=config.get('testServer','URL')
        logger.info('url：%s'%url)
        if browser=='Firefox':
            self.driver=webdriver.Firefox(self.firefox_path)
            logger.info('starting firefox browser')
        elif browser=='IE':
            self.driver = webdriver.Firefox(self.IE_path)
            logger.info('starting IE browser')
        elif browser=='Chrome':
            self.driver = webdriver.Firefox(self.Chrome_path)
            logger.info('starting Chrome browser')
        self.driver.get(url)
        self.driver.maximize_window()
        logger.info('Maximize thecurrent window')
        self.driver.implicitly_wait(8)
        return  self.driver

    def quit_browser(self):
        logger.info('close and quit the browser')
        self.driver.quit()
