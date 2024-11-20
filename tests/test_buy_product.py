import time
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from pages.main_page import Main_page
from pages.login_page import Login_page
from pages.men_clothing_page import Men_clothing
from pages.nike_air import Nike_airmax_page
from pages.user_account_page import User_account_page
from pages.shipping_page import Shipping_page
from pages.chekout_page import Chekout_page


def test_by_product_1():
    driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
   
    print("Start Test 1")

    mp = Main_page(driver) # Открываем главную страницу и открываем
    mp.open_page()         # страницу для авторизация
    mp.select_login_button()

    lp = Login_page(driver) #Авторизируемся
    lp.autorization()
    time.sleep(5)

    mp.select_men_clothing_link() #Выбираем товар по фильтрам

    mcp = Men_clothing(driver)
    mcp.select_price_radio_100_150()
    mcp.scroll_browser(driver, 0, 300)
    mcp.select_show_more_size()
    mcp.scroll_browser(driver, 0, 600)
    mcp.select_size_10()
    mcp.scroll_browser(driver, 0, 5800)
    mcp.select_nike()
    mcp.select_white_black_color()
    mcp.select_apply_filter_button()
    mcp.select_nike_airmax()

    na = Nike_airmax_page(driver) 
    time.sleep(5)
    product_name = na.product_name_text()
    product_price = na.product_price_text()
    na.scroll_browser(driver, 0, 400)
    na.select_color_choice()
    na.select_size_choice()
    na.select_add_to_cart_button()
    na.select_checkout_button()

    ua = User_account_page(driver) #Оформляем покупку товара
    ua.select_continue_shipping()

    shp = Shipping_page(driver)
    time.sleep(5)
    shp.enter_shipping_info()
    shp.scroll_browser(driver, 0, 400)
    shp.select_standart_delivery()
    shp.select_continue_to_billing()
    time.sleep(5)
    shp.select_continue_to_billing()

    cp = Chekout_page(driver)
    time.sleep(5)
    cp.assert_product_name(product_name)
    cp.assert_product_price(product_price)
    cp.get_screenshot()

    print("Finish Test 1")
    driver.quit()
