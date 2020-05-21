import unittest
import time
from helpers.driver import driver
from homePageTests import MyTestCase
from selenium.webdriver import ActionChains



class linkVerification(unittest.TestCase):

 def test_name1(self):
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
     handles = driver.window_handles
     size = len(handles)
     print(size)
     driver.switch_to.window(handles[1])
     driver.close()
     print("22")
     driver.switch_to.window(handles[0])
     # driver.find_element_by_css_selector(".i.we_close").click()
     more= driver.find_element_by_css_selector('.list-more-tab')
     hover = ActionChains(driver).move_to_element(more)
     hover.perform()
     time.sleep(2)


def header(self):
    time.sleep(20)
if __name__ == '__main__':
    MyTestCase.test_name()
    linkVerification.test_name1()
