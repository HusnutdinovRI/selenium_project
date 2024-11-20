from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base

class Login_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    user_name = "//input[@id='email']"
    password = "//input[@id='password']"
    sing_in_button = "//button[@data-testid='login-form-submit']"
    main_word = "//h2[@class='sf-heading__title title']"

    # Getters

    def get_user_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.user_name)))
        
    def get_password(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.password)))

    def get_sing_in_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.sing_in_button)))
    
    def get_main_word(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.main_word)))
    
    # Actions

    def input_user_name(self, user_name):
        self.get_user_name().send_keys(user_name)
        print("Input user_name")

    def input_password(self, password):
        self.get_password().send_keys(password)
        print("Input password")

    def click_sing_in_button(self):
        self.get_sing_in_button().click()
        print("Click Sing In button")


    # Methods

    def autorization(self):
        self.get_current_url()
        self.input_user_name("90tdh@livinitlarge.net")
        self.input_password("1Qazwsxedc")
        self.click_sing_in_button()
        # self.assert_word(self.get_main_word(), 'New Products')

        