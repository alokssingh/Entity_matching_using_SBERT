from selenium_operations import click_element, get_element_text
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import time


if __name__ == "__main__":
    options = Options()
    options.add_argument('--headless=new')
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    driver.get('https://ejatlas.org')

    data = 'dumpsites or landfills'
    xpath_croft_input = '//*[@id="conflict-list"]/div/div/div[2]/div/div/div/div/div/div/input'
    xpath_search_button = '//*[@id="submit_register_search"]/button[2]'
    xpath_table_data = 'MuiTypography-root MuiTypography-body1 css-o7r3lv'
    xpath_table_data = '//*[@class="google-visualization-table-td"][4]'
    next_button_click = '/html/body/div[2]/div[3]/div[2]/div/div[2]/div[2]/div/div/div/div/div/div/button'
    xpath1 = '//*[@id="conflict-list"]/div[2]/div/div/div[1]/div/img'
    l_text = []
    l_impact = []
    l_project_details = []
    l_headline = []

    driver.get('https://ejatlas.org/country/zimbabwe')
    time.sleep(10)
    total = '//*[@id="conflict-list"]/span'
    elem1 = driver.find_elements(By.XPATH, total)
    for el in elem1:
        ll = el.text
    total_cases = int(ll.split(" ")[0])

    count = 0

    for i in range(1, total_cases+1):
        driver.get('https://ejatlas.org/country/zimbabwe')
        time.sleep(10)

        if i < total_cases and i >= 10:
            for itr in range(0, i, 10):
                els = driver.find_elements(By.XPATH, '//*[@id="conflict-list"]/div/div')
                try:
                    driver.execute_script('arguments[0].scrollBy(0, 10000);', els[-1])
                    time.sleep(10)
                except Exception as err:
                    pass

        time.sleep(3)

        xx = f'//*[@id="conflict-list"]/div[2]/div/div/div[{i}]/div/img'
        elem = driver.find_elements(By.XPATH, xx)

        for ele in elem:
            try:
                ele.click()
            except:
                pass
        time.sleep(5)

        try:
            WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div[6]/button'))).click()
        except:
            pass

        try:
            for button in driver.find_elements(By.XPATH, '//button[text()="See more"]'):
                button.click()
                time.sleep(5)
        except:
            pass

        elem1= driver.find_elements(By.XPATH, '//*[@id="conflict-detail"]/div[2]/div[2]/div/div/div/div/div/p/span')

        for j in elem1:
            l_text.append(j.text)

        time.sleep(5)

        x1 = '//*[@id="conflict-detail"]/div[7]/div[2]/div/div/div/div/div'
        elem111= driver.find_elements(By.XPATH, x1)
        for jj in elem111:
            l_impact.append(jj.text)

        x2 = '//*[@id="conflict-detail"]/div[5]/div[2]/div/div/div/div/div'
        elem112= driver.find_elements(By.XPATH, x2)
        for jj in elem112:
            l_project_details.append(jj.text)

        x3 = '//*[@id="conflict-detail"]/div[1]/div[1]/h5'
        elem113= driver.find_elements(By.XPATH, x3)
        for jj in elem113:
            print(jj.text)
            l_headline.append(jj.text)

        print(len(l_text))
        print(len(l_impact))
        print(len(l_project_details))
        print(len(l_headline))

        if len(l_text) != len(l_impact) or len(l_text) != len(l_project_details) or len(l_text) != len(l_headline):
            print("Error: Lengths of lists do not match")
            break  # Exit the loop if the lengths of lists do not match

        time.sleep(5)
        driver.execute_script("window.history.go(-1)")
        time.sleep(5)

    # Create DataFrame and save to Excel
    data_dict = {'headline': l_headline, 'impact': l_impact, 'text': l_text, 'project_details': l_project_details}
    df = pd.DataFrame(data_dict)
    df.to_excel("zimbabwe_30_april.xlsx")

    driver.quit()
