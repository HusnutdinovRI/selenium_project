from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base

class Nike_airmax_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    color_choice = "//img[@custion-id='Black & White']"
    size_choice = "//button[@color='10']"
    add_to_cart_button = "//button[@class='sf-add-to-cart__button rounded-md sf-button']"
    checkout_button = "//button[@class='sf-button color-secondary text-sm rounded sf-button']"
    product_name = "//h1[@class='sf-heading__title h2 text-left']"
    product_price = "//span[@class='sf-price__regular']"
    
    # Getters

    def get_product_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.product_name)))
    
    def get_product_price(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.product_price)))

    def get_color_choice(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.color_choice)))
    
    def get_size_choice(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.size_choice)))

    def get_add_to_cart_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.add_to_cart_button)))
    
    def get_checkout_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.checkout_button)))
    
     
    # Actions

    def click_color_choice(self):
        self.get_color_choice().click()
        print("Click color choice")

    def click_size_choice(self):
        self.get_size_choice().click()
        print("Click size choice")
        
    def click_add_to_cart_button(self):
        self.get_add_to_cart_button().click()
        print("Click add to cart button")

    def click_checkout_button(self):
        self.get_checkout_button().click()
        print("Click checkout button")


    # Methods

    def select_color_choice(self):
        self.click_color_choice()

    def select_size_choice(self):
        self.click_size_choice()

    def select_add_to_cart_button(self):
        self.click_add_to_cart_button()

    def select_checkout_button(self):
        self.click_checkout_button()

    def product_name_text(self):
        return self.get_product_name().text

    def product_price_text(self):
        return self.get_product_price().text
