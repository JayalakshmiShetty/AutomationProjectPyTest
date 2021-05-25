import inspect
import logging

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

@pytest.mark.usefixtures("setup")
class BaseClass:

    def getLogger(self):
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)
        fileHandler = logging.FileHandler('logfile.log')
        formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
        fileHandler.setFormatter(formatter)

        logger.addHandler(fileHandler)  # filehandler object

        logger.setLevel(logging.DEBUG)
        return logger

    def verifyLinkPresence(self, text):
        element = WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT, text)))

    def selectOptionByText(self,locator,text):
        sel = Select(locator)
        if text is not None:
            sel.select_by_visible_text(text)

    def open_web_page(self, url):
        """
        Open the web page as per given url
        :param url:
        :return:
        """
        self.driver.get(url)

    def find_element(self, locator):
        """
        :param locator:
        :return:
        """
        return self.driver.find_element(*locator)

    def find_elements(self, locator):
        """
        :param locator:
        :return:
        """

        return self.driver.find_elements(*locator)

    def click(self, locator):
        """
        :param locator:
        :return:
        """
        self.find_element(locator).click()

    def clear_text_box(self, locator):
        if  self.find_element(locator).text is not None:
            self.find_element(locator).clear()

    def fill_text_box(self, locator, text):
        """
        :param locator:
        :param text:
        :return:
        """
        self.clear_text_box(locator)
        if text is not None:
            self.find_element(locator).send_keys(text)


    def press_enter_key(self, locator):
        """
        :param locator:
        :return:
        """
        self.find_element(locator).send_keys(Keys.ENTER)

    def wait_text_visible(self, text, time_out=10):
        """
        :param text:
        :param time_out
        :return:
        """
        try:
            element = WebDriverWait(self.driver, timeout=time_out).until(
                lambda element: self.driver.find_element(By.XPATH, "//*contains(text(),'%s')" % text))
            if element:
                return True
        except:
            return False

    def is_element_present(self, locator):
        """
        :param locator:
        :return:
        """
        try:
            self.find_element(locator)
            return True
        except NoSuchElementException:
            return False
