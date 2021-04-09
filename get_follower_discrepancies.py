from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time


username = 'dayoajayi'
password = ''

def login():
    driver.find_element_by_name("username").send_keys(username)
    driver.find_element_by_name("password").send_keys(password)
    driver.find_element_by_name("password").send_keys(u'\ue007')

def click_button_with_css(driver, css_selector):
    element = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, css_selector)))
    element.click()

def navigate_to_followers():
    dropdown_css = f'[alt*="{username}"]'
    profile_css = f'[href*="{username}"]'
    click_button_with_css(driver, dropdown_css)
    click_button_with_css(driver, profile_css)

def __main__():
    driver = webdriver.Chrome(ChromeDriverManager().install())        
    driver.get('https://instagram.com/accounts/login?source=auth-switcher')
    time.sleep(1)    
    login(driver)
    navigate_to_followers(driver)
    return

__main__()