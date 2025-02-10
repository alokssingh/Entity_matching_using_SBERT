from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium import webdriver


def click_element(driver, xpath):
    elem = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, xpath)))
    elem.click()
    time.sleep(5)


def get_element_text(driver, xpath):
    elem = driver.find_elements(By.XPATH, xpath)
    return [e.text for e in elem]
