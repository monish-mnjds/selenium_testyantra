from Library.Config import *
from Library.file_library import ReadExcelFile
from Library.web_utilities import Lib

read_xl = ReadExcelFile()
web_utls = Lib()
element, keys = read_xl.read_excel(WORK_BOOK, SHEET_NAME)


class AutomatingWebShop:
    def __init__(self, driver, dataset):
        self.driver = driver
        self.dataset = dataset
        self.firstname, self.lastname, self.email, self.password, self.c_password = read_xl.read_test_data(TEST_PATH, TEST_SHEET, self.dataset)

    def click_reg(self):
        # driver.find_element_by_xpath("//a[@class='ico-register']").click()
        web_utls.click_(self.driver, element["clickReg"])

    def click_radio(self):
        # driver.find_element_by_xpath("//input[@id='gender-male']").click()
        web_utls.click_(self.driver, element["clickRadio"])

    def enter_first_name(self):
        # driver.find_element_by_id("FirstName").send_keys("Virat")
        web_utls.sendKeys(self.driver, element["enterFirstname"], self.firstname)

    def enter_last_name(self):
        # driver.find_element_by_id("LastName").send_keys("Kohli")
        web_utls.sendKeys(self.driver, element["enterLastname"], self.lastname)

    def enter_email(self):
        # driver.find_element_by_xpath("//input[@id='Email']").send_keys("viratkohli18@gmail.com")
        web_utls.sendKeys(self.driver, element["enterEmail"], self.email)

    def enter_password(self):
        # driver.find_element_by_xpath("//input[@id='Password']").send_keys("viratvirat18")
        web_utls.sendKeys(self.driver, element["enterPassword"], self.password)

    def confirm_password(self):
        # driver.find_element_by_xpath("//input[@id='ConfirmPassword']").send_keys("viratvirat18")
        web_utls.sendKeys(self.driver, element["confirmPassword"], self.c_password)

    def click_register(self):
        # driver.find_element_by_xpath("//input[@id='register-button']").click()
        web_utls.click_(self.driver, element["clickRegister"])
