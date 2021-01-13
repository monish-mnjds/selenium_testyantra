

class Lib:

    def sendKeys(self, driver, element, string):
        loc_type, loc_value = element
        driver.find_element(loc_type, loc_value).send_keys(string)

    def click_(self, driver, element):
        loc_type, loc_value = element
        driver.find_element(loc_type, loc_value).click()
