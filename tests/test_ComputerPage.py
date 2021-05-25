from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import pytest
from selenium.webdriver.support.wait import WebDriverWait

from Pages.EditComputerPage import EditComputerPage
from Pages.HomeDBPage import HomeDBPage
from TestData.HomePageData import HomePageData
from Pages.AddComputerPage import AddComputerPage
from pageObjects.HomePageLocators import HomePageLocators
from utilities.BaseClass import BaseClass


class TestAddComputerPage(BaseClass):

    def test001_verify_add_computer_with_all_details(self, getData):
        log = self.getLogger()
        log.info("first name is "+getData["ComputerName"])
        homepage = HomePageLocators(self.driver)
        homepage.addComputer()
        AddComputerPage(self.driver).enterCreateComputerPageDetails(getData["ComputerName"], getData["IntroducedDate"], getData["DiscontinuedDate"], getData["Company"])
        AddComputerPage(self.driver).clickOnCreateComputerButton()
        wait = WebDriverWait(self.driver, 15)
        alertText = wait.until(EC.element_to_be_clickable((By.XPATH, "//section/div[@class='alert-message warning']"))).text
        assert (getData["ComputerName"] in alertText)


    def test002_verify_click_on_cancel_button_with_data_fields(self, getData):
        homepage = HomePageLocators(self.driver)
        homepage.addComputer()
        AddComputerPage(self.driver).enterCreateComputerPageDetails(getData["ComputerName"], getData["IntroducedDate"],getData["DiscontinuedDate"], getData["Company"])
        AddComputerPage(self.driver).clickOnCancelComputerButton()

    def test003_add_computer_by_name_field(self, getData):
        '''Test add new computer with only computer name value'''
        homepage = HomePageLocators(self.driver)
        homepage.addComputer()
        AddComputerPage(self.driver).enterCreateComputerPageDetails(getData["ComputerName"], None, None, None)
        AddComputerPage(self.driver).clickOnCreateComputerButton()
        wait = WebDriverWait(self.driver, 15)
        alertText = wait.until(EC.element_to_be_clickable((By.XPATH, "//section/div[@class='alert-message warning']"))).text
        assert (getData["ComputerName"] in alertText)


    def test004_cancel_add_computer_by_all_empty_fields(self):
        ''': Test add new computer with empty name'''
        homepage = HomePageLocators(self.driver)
        homepage.addComputer()
        AddComputerPage(self.driver).enterCreateComputerPageDetails(None, None, None, None)
        AddComputerPage(self.driver).clickOnCancelComputerButton()

    def test005_add_computer_by_empty_name_field(self):
        ''': Test add new computer with empty name'''
        homepage = HomePageLocators(self.driver)
        homepage.addComputer()
        AddComputerPage(self.driver).enterCreateComputerPageDetails(None, None, None, None)
        AddComputerPage(self.driver).clickOnCreateComputerButton()
        wait = WebDriverWait(self.driver, 15)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, '//div[@class="clearfix error"]')))
        alertText = element.text
        assert ("Required" in alertText)
        EditComputerPage(self.driver).clickOnCancelComputerButton()

    def test006_verify_edit_computer_with_all_details(self, getData):
        homepage = HomePageLocators(self.driver)
        homepage.addComputer()
        AddComputerPage(self.driver).createComputer(getData["ComputerName"], getData["IntroducedDate"],
                                                    getData["DiscontinuedDate"], getData["Company"])
        HomeDBPage(self.driver).filterComputerByName(getData["ComputerName"])
        HomePageLocators(self.driver).clickOnFirstComputer()
        EditComputerPage(self.driver).enterEditComputerPageDetails(getData["ComputerName"], getData["IntroducedDate"],
                                                                   getData["DiscontinuedDate"], getData["Company"])
        EditComputerPage(self.driver).clickOnSaveButton()
        wait = WebDriverWait(self.driver, 15)
        alertText = wait.until(EC.element_to_be_clickable((By.XPATH, "//section/div[@class='alert-message warning']"))).text
        assert (getData["ComputerName"] in alertText)



    def test007_verify_click_on_cancel_button_with_data_fields_in_EditPage(self, getData):
        homepage = HomePageLocators(self.driver)
        homepage.addComputer()
        AddComputerPage(self.driver).createComputer(getData["ComputerName"], getData["IntroducedDate"],getData["DiscontinuedDate"], getData["Company"])

        HomeDBPage(self.driver).filterComputerByName(getData["ComputerName"])
        HomePageLocators(self.driver).clickOnFirstComputer()
        EditComputerPage(self.driver).enterEditComputerPageDetails(getData["ComputerName"], getData["IntroducedDate"],getData["DiscontinuedDate"], getData["Company"])
        EditComputerPage(self.driver).clickOnCancelComputerButton()

    def test008_edit_computer_by_name_field(self, getData):
        '''Test edit computer with only computer name value'''
        homepage = HomePageLocators(self.driver)
        homepage.addComputer()
        AddComputerPage(self.driver).createComputer(getData["ComputerName"], getData["IntroducedDate"], getData["DiscontinuedDate"], getData["Company"])
        HomeDBPage(self.driver).filterComputerByName(getData["ComputerName"])
        HomePageLocators(self.driver).clickOnFirstComputer()
        EditComputerPage(self.driver).enterEditComputerPageDetails(getData["ComputerName"], None, None, None)
        EditComputerPage(self.driver).clickOnSaveButton()
        wait = WebDriverWait(self.driver, 15)
        alertText = wait.until(EC.element_to_be_clickable((By.XPATH, "//section/div[@class='alert-message warning']"))).text
        assert (getData["ComputerName"] in alertText)

    def test009_edit_computer_by_empty_name_field(self, getData):
        ''': Test edit computer with empty name'''
        homepage = HomePageLocators(self.driver)
        homepage.addComputer()
        AddComputerPage(self.driver).createComputer(getData["ComputerName"], getData["IntroducedDate"],
                                                    getData["DiscontinuedDate"], getData["Company"])
        HomeDBPage(self.driver).filterComputerByName(getData["ComputerName"])
        HomePageLocators(self.driver).clickOnFirstComputer()
        EditComputerPage(self.driver).enterEditComputerPageDetails(None, None, None, None)
        EditComputerPage(self.driver).clickOnSaveButton()
        EditComputerPage(self.driver).clickOnCancelComputerButton()

    def test010_cancel_edit_computer_by_all_empty_fields(self, getData):
        ''' Test edit computer with empty name'''
        homepage = HomePageLocators(self.driver)
        homepage.addComputer()
        AddComputerPage(self.driver).createComputer(getData["ComputerName"], getData["IntroducedDate"],
                                                    getData["DiscontinuedDate"], getData["Company"])
        HomeDBPage(self.driver).filterComputerByName(getData["ComputerName"])
        HomePageLocators(self.driver).clickOnFirstComputer()
        EditComputerPage(self.driver).enterEditComputerPageDetails(None, None, None, None)
        EditComputerPage(self.driver).clickOnCancelComputerButton()
        self.driver.refresh()
        
    def test010_verify_delete_computer(self, getData):
        ''' Test delete computer'''
        homepage = HomePageLocators(self.driver)
        homepage.addComputer()
        AddComputerPage(self.driver).createComputer(getData["ComputerName"], getData["IntroducedDate"],
                                                    getData["DiscontinuedDate"], getData["Company"])
        HomeDBPage(self.driver).filterComputerByName(getData["ComputerName"])
        HomePageLocators(self.driver).clickOnFirstComputer()
        EditComputerPage(self.driver).clickOnDeleteComputerButton()





    @pytest.fixture(params= HomePageData.getTestData("AddComputer"))
    def getData(self, request):
        return request.param


