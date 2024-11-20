from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from  selenium.common.exceptions import NoSuchWindowException, TimeoutException
from base.base_class import Base

class Chekout_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    total_price = "(//span[@class='sf-property__value'])[3]"
    product_title = "//div[@class='product-title']"

    # Getters

    def get_total_price(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.total_price)))
    
    def get_product_title(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.product_title)))
     
    # Actions


    # Methods

    def assert_product_name(self, product_name):
        print(product_name, self.get_product_title().text)
        assert product_name == self.get_product_title().text
        print("Product name correct")

    def assert_product_price(self, product_price):
        print(product_price, self.get_total_price().text )
        assert product_price == self.get_total_price().text
        print("Product price correct")
