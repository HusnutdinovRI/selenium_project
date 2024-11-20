from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from base.base_class import Base

class Shipping_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    first_name = "//input[@id='firstName']"
    last_name = "//input[@id='lastName']"
    street_name = "//input[@id='streetName']"
    appartment_number = "//input[@id='apartment']"
    county = "(//input[@class='vs__search'])[1]"
    city = "(//input[@class='vs__search'])[2]"
    zip_code = "//input[@id='zipCode']"
    telephone = "//input[@id='telephone']"
    go_to_shipping_method = "//button[@type='submit']"
    standart_delivery = "//span[@class='sf-radio__checkmark']"
    continue_to_billing = "//button[@class='form__action-button sf-button']"

    


    # Getters

    def get_first_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.first_name)))
    
    def get_last_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.last_name)))

    def get_street_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.street_name)))

    def get_appartment_number(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.appartment_number)))

    def get_county(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.county)))
    
    def get_city(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.city)))

    def get_zip_code(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.zip_code)))

    def get_telephone(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.telephone)))
    
    def get_go_to_shipping_methode(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.go_to_shipping_method)))

    def get_standart_delivery(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.standart_delivery)))

    def get_continue_to_billing(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.continue_to_billing)))

     
    # Actions

    def input_first_name(self,f_name):
        self.clear_field(self.get_first_name())
        self.get_first_name().send_keys(f_name)
        self.get_first_name().send_keys(Keys.ENTER) 
        print("Input first name")

    def input_last_name(self, l_name):
        self.clear_field(self.get_last_name())
        self.get_last_name().send_keys(l_name)
        self.get_last_name().send_keys(Keys.ENTER) 
        print("Input last_name")

    def input_street_name(self, s_name):
        self.clear_field(self.get_street_name())
        self.get_street_name().send_keys(s_name)
        self.get_street_name().send_keys(Keys.ENTER) 
        print("Input street name")

    def input_appartment_number(self, a_number):
        self.clear_field(self.get_appartment_number())
        self.get_appartment_number().send_keys(a_number)
        self.get_appartment_number().send_keys(Keys.ENTER) 
        print("Input appartment_number")

    def input_county(self, county_value):
        self.clear_field(self.get_county())
        self.get_county().send_keys(county_value)
        self.get_county().send_keys(Keys.ENTER) 
        print("Input county")

    def input_city(self, city_name):
        self.clear_field(self.get_city())
        self.get_city().send_keys(city_name)
        self.get_city().send_keys(Keys.ENTER) 
        print("Input city")
    
    def input_zip_code(self, zip_code_value):
        self.clear_field(self.get_zip_code())
        self.get_zip_code().send_keys(zip_code_value)
        self.get_zip_code().send_keys(Keys.ENTER) 
        print("Input zip code")

    def input_telephone(self, telephone_number):
        self.clear_field(self.get_telephone())
        self.get_telephone().send_keys(telephone_number)
        print("Input telephone")

    def click_go_to_shipping_method(self):
        self.get_go_to_shipping_methode().click()
        print("Click go to shipping method")
    
    def click_standart_delivery(self):
        self.get_standart_delivery().click()
        print("Click standart delivery")

    def click_continue_to_billing(self):
        self.get_continue_to_billing().click()
        print("Click continue to billing")

    
    # Methods

    def enter_shipping_info(self):
        self.input_first_name('Ivan')
        self.input_last_name('Ivanov')
        self.input_street_name('Pushkina')
        self.input_appartment_number('36')
        self.input_county('Malta')
        self.input_city('Balzan')
        self.input_zip_code('555555')
        self.input_telephone('5677777777')

    def select_shipping_method(self):
        self.click_go_to_shipping_method()

    def select_standart_delivery(self):
        self.click_standart_delivery()
    
    def select_continue_to_billing(self):
        self.click_continue_to_billing()




