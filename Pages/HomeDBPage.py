
from selenium.webdriver.support.select import Select
from selenium import webdriver
import psycopg2.errorcodes


from TestData.HomePageData import HomePageData
from pageObjects.HomePageLocators import HomePageLocators
from utilities.BaseClass import BaseClass


class HomeDBPage(BaseClass):

    def __init__(self, driver):
        self.driver = driver
        self.homepage = HomePageLocators(self.driver)

    def filterComputerByName(self, computerName):
        self.homepage.getSearchTextbox().send_keys(computerName)
        self.homepage.getFilterSearchButton().click()
        self.homepage.getFilterSearchButton()
        self.driver.refresh()

    def clickOnFilteredComputer(self, computerName):
        self.homepage.getFilteredComputer().click()



    # def newFormSubmission(self):
    #     # log = self.getLogger()
    #
    #     hp1= HomePageLocators(self.driver)
    #     # log.info("first name is "+getData["firstname"])
    #     # homeP.search_text_in_filter()
    #     hp1.getFilterSearchButton().click()
    #       # homepage.getName().send_keys(getData["firstname"])
    #     # homepage.getEmail().send_keys(getData["lastname"])
    #     # homepage.getCheckBox().click()
    #     #psycopg2.errorcodes.UNIQUE_VIOLATION
    #     # self.selectOptionByText(homepage.getGender(), "Female")
    #     #
    #     #
    #     # homepage.submitForm().click()
    #     #
    #     # alertText = homepage.getSuccessMessage().text
    #     #
    #     # assert ("Success" in alertText)
    #     self.driver.refresh()



