from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium import webdriver

WAITING_TIME = 0


def initialize_driver():
    options = Options()
    options.add_argument('--headless=new')
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    return driver


def click_element(driver, xpath):
    elem = WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.XPATH, xpath)))
    elem.click()
    time.sleep(5)

def get_element_text(driver, xpath):
    elem = driver.find_elements(By.XPATH, xpath)
    return [e.text for e in elem]
