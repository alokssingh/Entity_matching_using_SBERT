from selenium_operations import initialize_driver, click_element, send_keys_to_element
import pandas as pd
import time
from selenium.webdriver.common.by import By


def lat_lon_extraction(get_url):
    try:
        aa = get_url.split("3d")
        bb = aa[-1].split("!4d")
        lat = float(bb[0])
        temp = bb[-1].split("!")
        lon = float(temp[0])
        return lat, lon
    except Exception as e:
        return None, None


def main():
    driver = initialize_driver()
    url = "https://www.google.com/maps"
    driver.get(url)

    XPATH_COOKIES = '//*[@id="yDmH0d"]/c-wiz/div/div/div/div[2]/div[1]/div[3]/div[1]/div[1]/form[1]/div/div/button'
    XPATH_SEARCH = '//*[@id="searchboxinput"]'
    XPATH_SEARCH_CLICK = '//*[@id="searchbox-searchbutton"]'
    type_search = '/html/body/div[3]/div[9]/div[9]/div/div/div[1]/div[2]/div/div[1]/div/div/div[2]/div/div[1]/div[2]/div/div[2]/span/span/span'
    name = '//*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[2]/div/div[1]/div[1]/h1'

    elem = click_element(driver, XPATH_COOKIES)

    # Load data from Excel file
    data = pd.read_excel("final_merged_city_farm_no_duplicates.xlsx")
    data["New_full_address"] = data['address1'].astype(str) + ", " + data['address2'].astype(str) + ", " + data[
        'address3'].astype(str)
    keyword = data['New_full_address'].to_list()

    data_l = []

    for i in keyword[:5]:
        print(i)
        driver.get(url)
        elem = click_element(driver, XPATH_SEARCH)
        send_keys_to_element(driver, XPATH_SEARCH, i)
        elem = click_element(driver, XPATH_SEARCH_CLICK)
        time.sleep(10)

        try:
            elem = driver.find_element(By.XPATH, name)
            company_name = elem.text
        except Exception as err:
            company_name = None

        try:
            elem = driver.find_element(By.XPATH, type_search)
            type_name = elem.text
        except Exception as err:
            type_name = None

        try:
            address = driver.find_element(By.CSS_SELECTOR, "[data-item-id='address']")
            address1 = address.text
        except Exception as err:
            address1 = None

        try:
            website = driver.find_element(By.CSS_SELECTOR, "[data-item-id='authority']")
            authority = website.text
        except Exception as err:
            authority = None

        get_url = driver.current_url
        data_l.append([i, company_name, type_name, address1, authority, get_url])

    cols = ["keyword_search", "company_name", "type_name", "address", "website", "URL"]
    df = pd.DataFrame(data_l, columns=cols)

    df["lat-lon"] = df["URL"].apply(lat_lon_extraction)
    df.to_excel("gmap_address_lat_lon.xlsx", index=False)


if __name__ == "__main__":
    main()