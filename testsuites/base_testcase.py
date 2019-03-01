from selenium import webdriver
from framework.browser_engine import *
import unittest

browser=BrowserEngine()
class BaseTeseCase(unittest.TestCase):
    def setUp(self):
        self.driver=browser.open_browser()


    def tearDown(self):
        self.driver=browser.quit_browser()
