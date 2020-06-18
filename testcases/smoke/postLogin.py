import unittest
from helpers.TestUtiles import driver
from homePageTests import MyTestCase
import time
from selenium.webdriver import ActionChains
xpath= driver.find_element_by_xpath
css=driver.find_element_by_css_selector
Account = xpath("//a[contains(text(),'My Account')]")
signInBtn = css("#signInBtn")
loginBtn = css("#login-input")
loginContinueBtn = css("#login-continue-btn")
passward = css(".text-box-full.mt10.wd100")
submit = css("#login-submit-btn")
title = css('a[title="disha"]')
class postLoginVerivication(unittest.TestCase):
    def sign_in(self):
        hover = ActionChains(driver).move_to_element(Account)
        hover.perform()
        signInBtn.click()
        time.sleep(1)
        loginBtn.send_keys("kauldisha24@gmail.com")
        loginContinueBtn.click()
        time.sleep(2)
        passward.send_keys("Ohmygod24")
        time.sleep(2)
        submit.click()
        time.sleep(5)
        title.is_displayed()
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