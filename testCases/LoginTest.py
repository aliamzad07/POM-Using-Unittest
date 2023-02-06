import time
import unittest
import HtmlTestRunner
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import sys
sys.path.append("D:\Automation Projects\POM_using_unittest")
from pageObjects.LoginPage import LoginPage

class LoginTest(unittest.TestCase):
    baseURL="https://admin-demo.nopcommerce.com/login"
    username= "admin@yourstore.com"
    password= "admin"
    serv_obj= Service("..\\drivers\\chromedriver.exe")
    driver= webdriver.Chrome(service=serv_obj)

    @classmethod
    def setUp(self):
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

    def test_login(self):
        lp = LoginPage(self.driver)
        lp.setUserName(self.username)
        lp.setPassword(self.password)
        lp.clickLogin()
        time.sleep(5)
        title1= self.driver.title
        self.assertEqual("Dashboard / nopCommerce administration",title1, "Webpage is not matching")

    @classmethod
    def tearDown(self):
        self.driver.close()



if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='.\\reports'))

