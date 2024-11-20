from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base

class Men_clothing(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    price_radio_100_150 = "(//span[@class='sf-radio__checkmark'])[3]"
    slider_size = "(//div[@class='sf-scrollable__content'])[2]"
    show_more_size = "(//button[@class='sf-button--text sf-scrollable__view-all sf-button'])[2]"
    size_10 = "(//span[@class='sf-checkbox__checkmark'])[19]"
    nike = "//button[@color='NIKE']"
    white_black_color = "(//span[@class='image_swatch swatch_color relative'])[1]"
    apply_filter_button = "//button[@class='sf-button--full-width sf-button']"
    nike_airmax = "(//span[@class='sf-product-card__title'])[1]"

    # Getters

    def get_price_radio_100_150(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.price_radio_100_150)))

    def get_show_more_size(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.show_more_size)))

    def get_size_10(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.size_10)))
    
    def get_nike(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.nike)))
    
    def get_white_black_color(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.white_black_color)))

    def get_apply_filter_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.apply_filter_button)))
    
    def get_nike_airmax(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.nike_airmax)))
    
    # Actions

    def click_price_radio_100_150(self):
        self.get_price_radio_100_150().click()
        print("Click radio_100_150")

    def click_show_more_size(self):
        self.get_show_more_size().click()
        print("Click show more size")

    def click_size_10(self):
        self.get_size_10().click()
        print("Click size_10 chekbox")

    def click_nike(self):
        self.get_nike().click()
        print("Click nike button")
        
    def click_white_black_color(self):
        self.get_white_black_color().click()
        print("Click white_black_color chekbox")       

    def click_apply_filter_button(self):
        self.get_apply_filter_button().click()
        print("Click apply filter button")   

    def click_nike_airmax(self):
        self.get_nike_airmax().click()
        print("Click nike airmax")   

    # Methods

    def select_price_radio_100_150(self):
        self.click_price_radio_100_150()

    def select_show_more_size(self):
        self.click_show_more_size()

    def select_size_10(self):
        # self.scroll_to_size_10()
        self.click_size_10()

    def select_nike(self):
        self.click_nike()

    def select_white_black_color(self):
        self.click_white_black_color()

    def select_apply_filter_button(self):
        self.click_apply_filter_button()
    
    def select_nike_airmax(self):
        self.click_nike_airmax()