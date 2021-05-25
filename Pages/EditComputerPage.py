from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium import webdriver
import psycopg2.errorcodes
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


from TestData.HomePageData import HomePageData
from pageObjects.EditComputerPageLocators import EditComputerPageLocators

from utilities.BaseClass import BaseClass



class EditComputerPage(BaseClass):

    def __init__(self, driver):
        self.driver = driver
        self.editComputerPage = EditComputerPageLocators(self.driver)


    def enterEditComputerPageDetails(self, computerName, IntroduceDate, DiscontinueDate, Company):
        self.driver.refresh()
        wait = WebDriverWait(self.driver, 15)
        txtComputerName = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id='name']")))
        txtComputerName.click()
        self.fill_text_box(self.editComputerPage.tboxComputerName, computerName)
        self.fill_text_box(self.editComputerPage.tboxIntroducedDate, IntroduceDate)
        self.fill_text_box(self.editComputerPage.tboxDiscontinuedDate, DiscontinueDate)
        self.selectOptionByText(self.editComputerPage.getCompany(), Company)

    def clickOnCancelComputerButton(self):
        self.editComputerPage.getCancelComputer().click()

    def clickOnDeleteComputerButton(self):
        self.editComputerPage.getCancelComputer().click()


    def clickOnSaveButton(self):
        self.editComputerPage.getSaveComputer().click()





