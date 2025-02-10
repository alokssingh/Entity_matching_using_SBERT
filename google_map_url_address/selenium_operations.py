from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager


def initialize_driver():
    options = Options()
    options.add_argument('--headless')
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    return driver


def click_element(driver, xpath):
    elem = WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.XPATH, xpath)))
    elem.click()
    return elem


def send_keys_to_element(driver, xpath, keys):
    elem = driver.find_element(By.XPATH, xpath)
    elem.send_keys(keys)
    return elem
