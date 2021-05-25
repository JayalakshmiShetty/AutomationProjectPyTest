from selenium.webdriver.common.by import By


class AddComputerPageLocators:
    """Constructor of the class"""



    def __init__(self, driver):
        self.driver = driver

    tboxComputerName = (By.XPATH, "//input[@id='name']")
    tboxDiscontinuedDate = (By.ID, "discontinued")
    tboxIntroducedDate = (By.ID, "introduced")
    btnCompany = (By.ID, "company")
    btnCreateComputer = (By.XPATH, "//input[@type='submit']")
    btnCancel = (By.XPATH, "//a[contains(text(),'Cancel')]")
    alertMsg = (By.XPATH, "//div[@class='clearfix error']")
    btnAddComp = (By.ID, "add")
    errorMsg = (By.XPATH, "//div[@class='clearfix error']/div/span")



    def getAddComputer(self):
        return self.driver.find_element(*AddComputerPageLocators.btnAddComp)

    def getComputerName(self):
        return self.driver.find_element(*AddComputerPageLocators.tboxComputerName)

    def getIntroduceDate(self):
        return self.driver.find_element(*AddComputerPageLocators.tboxIntroducedDate)

    def getDiscontinueDate(self):
        return self.driver.find_element(*AddComputerPageLocators.tboxDiscontinuedDate)

    def getCompany(self):
        return self.driver.find_element(*AddComputerPageLocators.btnCompany)

    def getCreateComputer(self):
        return self.driver.find_element(*AddComputerPageLocators.btnCreateComputer)

    def getCancelComputer(self):
        return self.driver.find_element(*AddComputerPageLocators.btnCancel)

    def getAlertMessage(self):
        return self.driver.find_element(*AddComputerPageLocators.alertMsg)

    def assertmsg(self):
        return self.alertMsg.text
