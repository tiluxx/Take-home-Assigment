import pandas as pd
from bs4 import BeautifulSoup
from functools import lru_cache
from tqdm import tqdm
from selenium import webdriver

REAL_ESTATE_DATA_TAG = {
    'title': 'js__card-title',
    'price': 're__card-config-price',
    'area': 're__card-config-area',
    'location': 're__card-location',
    'description': 're__card-description',
}


@lru_cache(maxsize=None)
def get_raw_content(cur_url):
    driver = webdriver.Chrome()
    driver.get(cur_url)
    driver.implicitly_wait(5)
    
    res = driver.page_source
    content = BeautifulSoup(res, 'html.parser')
    return content


def scrape_data(base_url, page_routes, limit_page_num=None):
    """
    Scrape data from the given url and return a dictionary containing
    real estate information.
    
    Params:\n
    base_url: The base URL of the website.
    page_routes: The routes of pages to retrieve.
    limit_page_num (optional): The limit number of pages to retrieve. If it is None,
    all pages in the website will be retrieved.
    """
    
    real_estate_data = {
        'titles': [],
        'prices': [],
        'areas': [],
        'locations': [],
        'descriptions': [],
    }
    
    for route in page_routes:
        # Scrape from the first page
        cur_url = '{}/{}'.format(base_url, route)
        content = get_raw_content(cur_url)
        
        titles = content.find_all('span', class_=REAL_ESTATE_DATA_TAG['title'])
        prices = content.find_all('span', class_=REAL_ESTATE_DATA_TAG['price'])
        areas = content.find_all('span', class_=REAL_ESTATE_DATA_TAG['area'])
        descriptions = content.find_all('div', class_=REAL_ESTATE_DATA_TAG['description'])
        
        locations_parent = content.find_all('div', class_=REAL_ESTATE_DATA_TAG['location'])
        # The location in the second span tag
        locations = [location.findChildren()[1] for location in locations_parent]
            
        for title, price, area, description, location in zip(titles, prices, areas, descriptions, locations):
            real_estate_data['titles'].append(title.text.strip())
            real_estate_data['prices'].append(price.text.strip())
            real_estate_data['areas'].append(area.text.strip())
            real_estate_data['locations'].append(description.text.strip())
            real_estate_data['descriptions'].append(location.text.strip())
        
        # Scrape from the other pages
        pagination_nums = content.find_all('a', class_='re__pagination-number')
        if pagination_nums:
            # Get the total of pages in the last pagination number
            pages_num = int(pagination_nums[-1].text.strip().replace(",", "").replace(".", ""))
            if limit_page_num:
                pages_num = min(pages_num, limit_page_num)
                
            for page_num in tqdm(range(2, pages_num + 1)):
                cur_url = '{}/{}/p{}'.format(base_url, route, page_num)
                content = get_raw_content(cur_url)
                
                titles = content.find_all('span', class_=REAL_ESTATE_DATA_TAG['title'])
                prices = content.find_all('span', class_=REAL_ESTATE_DATA_TAG['price'])
                areas = content.find_all('span', class_=REAL_ESTATE_DATA_TAG['area'])
                descriptions = content.find_all('div', class_=REAL_ESTATE_DATA_TAG['description'])
                
                locations_parent = content.find_all('div', class_=REAL_ESTATE_DATA_TAG['location'])
                # The location in the second span tag
                locations = [location.findChildren()[1] for location in locations_parent]
                
                for title, price, area, description, location in zip(titles, prices, areas, descriptions, locations):
                    real_estate_data['titles'].append(title.text.strip())
                    real_estate_data['prices'].append(price.text.strip())
                    real_estate_data['areas'].append(area.text.strip())
                    real_estate_data['locations'].append(description.text.strip())
                    real_estate_data['descriptions'].append(location.text.strip())
    
    return real_estate_data


if __name__ == "__main__":
    BASE_URL = 'https://batdongsan.com.vn'
    REAL_ESTATE_ROUTE = ['nha-dat-ban', 'nha-dat-cho-thue']
    limit_page_num = 10
    scraped_data = pd.DataFrame()
    
    real_estate_data_df = pd.DataFrame(scrape_data(BASE_URL, REAL_ESTATE_ROUTE, limit_page_num))
    scraped_data = pd.concat([scraped_data, real_estate_data_df], ignore_index=True)
    
    excel_file_name = "real_estate_data.xlsx"
    scraped_data.to_excel(excel_file_name, index=False)
    print('Data scraped successfully and stored in {}'.format(excel_file_name))