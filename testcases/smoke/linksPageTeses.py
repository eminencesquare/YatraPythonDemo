import unittest
import time
from helpers.TestUtiles import driver
from homePageTests import MyTestCase
from selenium.webdriver import ActionChains
xpath= driver.find_element_by_xpath
css=driver.find_element_by_css_selector
flight = css('a[title="Flights"]')
bookFlights = xpath("//span[contains(text(),'Book Flights, Hotels and Holiday Packages')]")
bookingHotels = css("#booking_engine_hotels")
bookingHolidays = css("#booking_engine_holidays")
bookingBuses = css("#booking_engine_buses")
bookingInsurance = css("#booking_engine_insurance")
bookingAdventures = css("#booking_engine_adventures")

class linkVerification(unittest.TestCase):

 def test_name1(self):
     print("finish")
     time.sleep(20)
     flight.click()
     time.sleep(2)
     bookFlights.is_displayed()
     bookingHotels.click()
     time.sleep(5)
     bookingHolidays.click()
     bookingBuses.click()
     driver.back()
     bookingInsurance.click()
     driver.back()
     bookingAdventures.click()
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
