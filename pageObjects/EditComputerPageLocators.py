from selenium.webdriver.common.by import By


class EditComputerPageLocators:
    """Constructor of the class"""



    def __init__(self, driver):
        self.driver = driver

    tboxComputerName = (By.XPATH, "//input[@id='name']")
    tboxDiscontinuedDate = (By.ID, "discontinued")
    tboxIntroducedDate = (By.ID, "introduced")
    btnCompany = (By.ID, "company")
    btnSaveComputer = (By.XPATH, "//input[@type='submit']")
    btnCancel = (By.XPATH, "//a[contains(text(),'Cancel')]")
    alertMsg = (By.XPATH, "//div[@class='clearfix error']")
    btnDeleteComputer= (By.XPATH, "//input[@value='Delete this computer']")





    def getComputerName(self):
        return self.driver.find_element(*EditComputerPageLocators.tboxComputerName)

    def getIntroduceDate(self):
        return self.driver.find_element(*EditComputerPageLocators.tboxIntroducedDate)

    def getDiscontinueDate(self):
        return self.driver.find_element(*EditComputerPageLocators.tboxDiscontinuedDate)

    def getCompany(self):
        return self.driver.find_element(*EditComputerPageLocators.btnCompany)

    def getSaveComputer(self):
        return self.driver.find_element(*EditComputerPageLocators.btnSaveComputer)

    def getCancelComputer(self):
        return self.driver.find_element(*EditComputerPageLocators.btnCancel)

    def getAlertMessage(self):
        return self.driver.find_element(*EditComputerPageLocators.alertMsg)

    def getDeleteComputer(self):
        return self.driver.find_element(*EditComputerPageLocators.btnDeleteComputer)


