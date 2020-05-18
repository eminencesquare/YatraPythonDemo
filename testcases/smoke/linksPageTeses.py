import unittest

import time

from helpers.driver import driver
from homePageTests import MyTestCase


class linkVerification(unittest.TestCase):

 def testName1(self):
     print("finish")
     time.sleep(20)
     driver.find_element_by_css_selector('a[title="Flights"]').click()
     time.sleep(2)
     driver.find_element_by_xpath("//span[contains(text(),'Book Flights, Hotels and Holiday Packages')]").is_displayed()
     driver.find_element_by_css_selector("#booking_engine_hotels").click()
     time.sleep(5)
     driver.find_element_by_css_selector("#booking_engine_holidays").click()
     driver.find_element_by_css_selector("#booking_engine_buses").click()
     driver.back()
     driver.find_element_by_css_selector("#booking_engine_insurance").click()
     driver.back()
     driver.find_element_by_css_selector("#booking_engine_adventures").click()
     time.sleep(5)
     more= driver.find_element_by_css_selector(".list-more-tab")
     time.sleep(20)
if __name__ == '__main__':
    MyTestCase.testName()
    linkVerification.testName1()
