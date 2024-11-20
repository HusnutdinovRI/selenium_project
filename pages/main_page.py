from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from  selenium.common.exceptions import NoSuchWindowException, TimeoutException
from base.base_class import Base

class Main_page(Base):

    base_url = 'https://www.hudsonstore.com/mt'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    login_button = "(//span[@class='sf-image--wrapper'])[4]"
    men_clothing_link = "//a[@href='/mt/c/men.html']"

    # Getters

    def get_login_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.login_button)))
    
    def get_men_cloting_link(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.men_clothing_link)))

    # Actions

    def click_login_button(self):
        self.get_login_button().click()
        print("Click login button")

    def click_men_clothing_link(self):
        self.get_men_cloting_link().click()
        print("Click men clothing link")

    # Methods

    def open_page(self):
        self.driver.get(self.base_url)
        self.driver.maximize_window()

    def select_login_button(self):
        self.get_current_url()
        self.click_login_button()
        self.assert_url("https://www.hudsonstore.com/mt/login")

    def select_men_clothing_link(self):
        self.get_current_url()
        self.click_men_clothing_link()


    