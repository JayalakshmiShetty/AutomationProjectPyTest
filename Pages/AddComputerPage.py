from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium import webdriver
import psycopg2.errorcodes
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from pageObjects.AddComputerPageLocators import AddComputerPageLocators

from TestData.HomePageData import HomePageData
from pageObjects.HomePageLocators import HomePageLocators
from utilities.BaseClass import BaseClass
from pageObjects.AddComputerPageLocators import AddComputerPageLocators


class AddComputerPage(BaseClass):

    def __init__(self, driver):
        self.driver = driver
        self.addComputerPage = AddComputerPageLocators(self.driver)


    def enterCreateComputerPageDetails(self, computerName, IntroduceDate, DiscontinueDate, Company):
        self.driver.refresh()
        wait = WebDriverWait(self.driver, 15)
        element_present = EC.presence_of_element_located((By.XPATH, "//input[@type='submit']"))
        WebDriverWait(self.driver, 15).until(element_present)
        self.fill_text_box(self.addComputerPage.tboxComputerName, computerName)
        self.fill_text_box(self.addComputerPage.tboxIntroducedDate, IntroduceDate)
        self.fill_text_box(self.addComputerPage.tboxDiscontinuedDate, DiscontinueDate)
        self.selectOptionByText(self.addComputerPage.getCompany(), Company)


    def clickOnCreateComputerButton(self):
        wait = WebDriverWait(self.driver, 10)
        createComputerBtn=wait.until(EC.presence_of_element_located((By.XPATH, "//input[@type='submit']")))
        createComputerBtn.click()


    def clickOnCancelComputerButton(self):

        self.addComputerPage.getCancelComputer().click()

    def testing(self):
        alertText = AddComputerPageLocators.alertMsg.text

        assert ("Required" in alertText)

    def createComputer(self, computerName, IntroduceDate, DiscontinueDate, Company):
        # HomePageLocators(self.driver).addComputer()
        self.enterCreateComputerPageDetails(computerName, IntroduceDate, DiscontinueDate, Company)
        self.clickOnCreateComputerButton()





