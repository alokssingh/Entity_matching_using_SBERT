from selenium_operations import initialize_driver, click_element, get_element_text
from data_processing import load_json, serialize_to_excel
import time


if __name__ == "__main__":
    d = load_json('sources_2024-03-19T12_31_32.668Z.json')

    driver = initialize_driver()

    name = []
    sector = []
    plumes = []
    emission_rate = []
    current_url = []
    search_link = []
    lat_lon = []

    for i in range(1, 5):
        query = d['features'][i]['properties']['source_name']
        coordinates = d['features'][i]['geometry']['coordinates']
        url = "https://data.carbonmapper.org/?details=" + query
        print(i, url)
        search_link.append(url)
        lat_lon.append(coordinates)
        driver.get(url)

        time.sleep(5)
        try:
            checkbox_xpath = '//*[@id="modals"]/div/div/div[2]/div/label'
            click_element(driver, checkbox_xpath)

            button_xpath = '//*[@id="modals"]/div/div/div[2]/div/button'
            click_element(driver, button_xpath)
        except Exception as err:
            pass

        time.sleep(5)
        click_sub_button = f'//*[@id="main"]/div[1]/div/article/section[1]/div[4]/button[2]'
        click_element(driver, click_sub_button)

        time.sleep(5)
        current_url.append(driver.current_url)
        click_sector = '//*[@id="main"]/div[1]/div/article/section[1]/h2'
        name.append(get_element_text(driver, click_sector))

        click_sector = f'//*[@id="main"]/div[1]/div/article/div/section[2]/table[3]/tbody/tr[1]/td'
        sector.append(get_element_text(driver, click_sector))

        click_sector = '//*[@id="main"]/div[1]/div/article/div/section[2]/table[2]/tbody/tr[1]/td'
        plumes.append(get_element_text(driver, click_sector))

        click_sector = '//*[@id="main"]/div[1]/div/article/div/section[2]/table[3]/tbody/tr[2]/td'
        emission_rate.append(get_element_text(driver, click_sector))

    dd = {
        'Link': search_link,
        'Names': name,
        'Sector': sector,
        'Number of Plumes': plumes,
        'Source_Emission Rate': emission_rate,
        'lat_lon': lat_lon,
        'current_url': current_url
    }

    serialize_to_excel(dd, "carbon_mapper.xlsx")

    driver.quit()
