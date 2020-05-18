import unittest
from testcases.smoke import homePageTests
from helpers.driver import driver
from homePageTests import MyTestCase
import time

class postLoginVerivication(unittest.TestCase):

    def signIn(self):
      driver.find_element_by_xpath("//a[contains(text(),'My Account')]").click()
      driver.find_element_by_css_selector("#signInBtn").click()
      time.sleep(10)
      driver.find_element_by_css_selector("#login-input").send_keys("7415009986")
      driver.find_element_by_css_selector("login-continue-btn").click()
      driver.find_element_by_css_selector("#login-password").send_keys("Ohmygod24")
      driver.find_element_by_css_selector("login-continue-btn").click()
      driver.find_element_by_css_selector('a[title="disha"]').is_displayed()
    time.sleep(20)
    # def header(self):
    #
    #
    #
    # def footer(self):


if __name__ == '__main__':
    MyTestCase.testName()
    postLoginVerivication.signIn()
    # postLoginVerivication.header()
    # postLoginVerivication.footer()