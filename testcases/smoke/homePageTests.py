import unittest
from helpers.TestUtiles import driver
import time
from selenium import webdriver
xpath= driver.find_element_by_xpath
search_box = xpath("//input[contains(@class,'gLFyf gsfi')]")
yatra = xpath('//h3[contains(text(),"Yatra.com:")]')

class MyTestCase(unittest.TestCase):
    def test_name(self) :
      chrome_options = webdriver.ChromeOptions()
      prefs = {"profile.default_content_setting_values.notifications" : 1}
      chrome_options.add_experimental_option("prefs", prefs)
      driver = webdriver.Chrome(chrome_options=chrome_options , executable_path='c:\chromedriver.exe')
      driver.get("https://www.google.com")
      driver.save_screenshot("screenshot.png")
      driver.maximize_window()
      driver.delete_all_cookies()
      time.sleep(2)
      search_box.send_keys("https://yatra.com")
      search_box.submit()
      yatra.click()
      time.sleep(2)

if __name__ == '__main__':
  MyTestCase.test_name()
