from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pageObjects import EditComputerPageLocators
from pageObjects.AddComputerPageLocators import AddComputerPageLocators


class HomePageLocators:

    def __init__(self, driver):
        self.driver = driver

    shop = (By.CSS_SELECTOR, "a[href*='shop']")
    name = (By.CSS_SELECTOR, "[name='name']")
    email = (By.NAME, "email")
    check = (By.ID, "exampleCheck1")
    gender= (By.ID, "exampleFormControlSelect1")
    submit = (By.XPATH, "//input[@value='Submit']")
    successMessage = (By.CSS_SELECTOR, "[class*='alert-success']")
    tboxSearch = (By.XPATH, "//input[@id='searchbox']")
    btnSearchSubmit = (By.ID, "searchsubmit")
    filterComps = (By.XPATH, "//table[@class='computers zebra-striped']//tbody")
    btnNext = (By.XPATH, "//li[@class='next']")
    btnAddComp = (By.ID, "add")
    filteredComp = (By.XPATH, "//table[@class='computers zebra-striped']//tbody//tr[1]/td[1]/a")

    def addComputer(self):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.element_to_be_clickable((By.ID, "add")))
        element.click()
        return AddComputerPageLocators

    def clickOnFirstComputer(self):
        wait = WebDriverWait(self.driver, 10)
        fistSearch = wait.until(EC.element_to_be_clickable((By.XPATH, "//table[@class='computers zebra-striped']//tbody//tr[1]/td[1]/a")))
        fistSearch.click()
        return EditComputerPageLocators


    def getName(self):
        return self.driver.find_element(*HomePageLocators.name)


    def getEmail(self):
        return self.driver.find_element(*HomePageLocators.email)

    def getCheckBox(self):
        return self.driver.find_element(*HomePageLocators.check)

    def getGender(self):
        return self.driver.find_element(*HomePageLocators.gender)

    def submitForm(self):
        return self.driver.find_element(*HomePageLocators.submit)

    def getSuccessMessage(self):
        return self.driver.find_element(*HomePageLocators.successMessage)

    def getFilteredComputer(self):
        return self.driver.find_element(*HomePageLocators.filterComps)

    def getSearchTextbox(self):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id='searchbox']")))

        return element

    def getAddComputerButton(self):
        return self.driver.find_element(*HomePageLocators.btnAddComp)

    def getFilterSearchButton(self):
        return self.driver.find_element(*HomePageLocators.btnSearchSubmit)

    # def typeInSearchFilter(self, text):
    #     self.driver.find_element(*HomePageLocators.tboxSearch).sendkeys(text)
