from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pandas as pd

url = 'https://www1.nseindia.com/live_market/dynaContent/live_watch/equities_stock_watch.htm'
chrome_driver_path = 'chromedriver.exe'

chrome_options = Options()
#chrome_options.add_argument('--headless')

webdriver = webdriver.Chrome(
  executable_path=chrome_driver_path, options=chrome_options
)

with webdriver as driver:
    driver.set_page_load_timeout(10)
    try:
        driver.get(url)
    except:
        print('completed')
        
    content = driver.find_element_by_id("dataDiv")
    df_list = pd.read_html(content.get_attribute('innerHTML'))
    df = df_list[-1]
    df.to_csv('data.csv')
    driver.close()
