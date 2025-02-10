from selenium_operations import initialize_driver, click_element, get_element_text
import pandas as pd
from selenium.webdriver.common.by import By

if __name__ == "__main__":
    driver = initialize_driver()
    driver.get('https://globalplasticwatch.org/map')

    xpathnew1 = '/html/body/div[3]/div[1]/div[2]/div[1]/form/div[2]/div/button[2]'

    for ii in range(113):
        click_element(driver, xpathnew1)
        country_name_xpath = f"//*[@class='dropdown__option js-dropdown-option'][{ii}]"
        country_name = get_element_text(driver, country_name_xpath)[0]
        print(ii, country_name)
        click_element(driver, country_name_xpath)

        tile_elements = driver.find_elements(By.XPATH, '//*[@class="tile"]')
        texts_name = get_element_text(driver, '//div[@class="tile"]/div/div[2]/div[1]/div[1]')
        texts_gps = get_element_text(driver, '//div[@class="tile"]/div/div[2]/div[1]/div[2]')
        texts_area = get_element_text(driver, '//div[@class="tile"]/div/div[2]/div[2]/div[1]')
        texts_water = get_element_text(driver, '//div[@class="tile"]/div/div[2]/div[2]/div[2]')

        print(len(texts_name))
        print(len(texts_gps))
        print(len(texts_area))
        #         print(len(texts_water))

        dict_country = {
            'country': [country_name] * len(texts_name),
            'name': texts_name,
            'gps': texts_gps,
            'area': texts_area,
            #             'water': texts_water
        }

        df_new = pd.DataFrame(data=dict_country)
        filename = f'Global_Plastic_Waste_Json_{country_name}.xlsx'
        df_new.to_excel(filename, index=False)

    driver.quit()
