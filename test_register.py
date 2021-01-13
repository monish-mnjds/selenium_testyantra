import pytest
from Library.Config import *
from Page.automating_webshop import AutomatingWebShop
from Library.base_fixture import DriverInit
from Library.file_library import ReadExcelFile

readxl = ReadExcelFile()
element, test_data = readxl.read_excel(TEST_PATH, TEST_SHEET)


class TestRegister(DriverInit):
    @pytest.mark.parametrize('test_arg', test_data)
    def test_fun(self, test_arg):
        aw = AutomatingWebShop(self.driver, test_arg)
        aw.click_reg()
        aw.click_radio()
        aw.enter_first_name()
        aw.enter_last_name()
        aw.enter_email()
        aw.enter_password()
        aw.confirm_password()
        aw.click_register()
