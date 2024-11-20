from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base

class User_account_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    continue_shipping = "//button[@class='form__action-button sf-button']"

    # Getters

    def get_continue_shipping(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.continue_shipping)))
    
     
    # Actions

    def click_continue_shipping(self):
        self.get_continue_shipping().click()
        print("Click continue shipping")


    # Methods

    def select_continue_shipping(self):
        self.click_continue_shipping()
