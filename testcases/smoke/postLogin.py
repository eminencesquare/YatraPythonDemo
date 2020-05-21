import unittest
from helpers.driver import driver
from homePageTests import MyTestCase
import time
from selenium.webdriver import ActionChains

class postLoginVerivication(unittest.TestCase):
    def sign_in(self):
        Account = driver.find_element_by_xpath("//a[contains(text(),'My Account')]")
        hover = ActionChains(driver).move_to_element(Account)
        hover.perform()
        driver.find_element_by_css_selector("#signInBtn").click()
        time.sleep(1)
        driver.find_element_by_css_selector("#login-input").send_keys("kauldisha24@gmail.com")
        driver.find_element_by_css_selector("#login-continue-btn").click()
        time.sleep(2)
        driver.find_element_by_css_selector(".text-box-full.mt10.wd100").send_keys("Ohmygod24")
        time.sleep(2)
        driver.find_element_by_css_selector("#login-submit-btn").click()
        time.sleep(5)
        driver.find_element_by_css_selector('a[title="disha"]').is_displayed()
        time.sleep(2)

    # def header(self):
    #   time.sleep(20)
    #
    # def footer(self):
    #    time.sleep(20)

if __name__ == '__main__':
    MyTestCase.testName()
    plv=postLoginVerivication

    plv.sign_in()
    # postLoginVerivication.header()
    # postLoginVerivication.footer()