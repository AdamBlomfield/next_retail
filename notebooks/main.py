from bs4 import BeautifulSoup # Webscraping
import requests
import re
import pandas as pd # Dataframes
from collections import Counter # Combining dictionary values
from datetime import date # Input date the data is scraped
import time # to repeat the scraping every set amount of time
rounding = 2

# Custom Functions
import sys
sys.path.append('../')
from custom_functions.functions_for_parsing import strip_string_to_digits_only, sku_meta_data

# Repeat every 24 hours
if __name__ == '__main__':
    while True:
        # Blank DataFrame to store results
        meta_data_df = pd.DataFrame(columns=('Date', 'Total', 'New', 'In Stock', 'Restocked', 'Out of Stock'))

        # Timestamp of date of scraping
        todays_date = {'Date': date.today()}
        year = date.today().year
        month = date.today().month
        day = date.today().day
        todays_date_short = year, month, day

        # Combine the meta_data for sku from webpages scraped
        womens_meta_data = sku_meta_data('https://www.next.co.uk/shop/gender-women/sizetype-')
        mens_meta_data = sku_meta_data('https://www.next.co.uk/shop/gender-men/sizetype-')
        print("Scraping meta data for today {}".format(todays_date_short))
        all_meta_data = {}
        for key, value in womens_meta_data.items():
            all_meta_data[key] = womens_meta_data[key] + mens_meta_data[key]

        # Combine the Date with the meta_data
        todays_meta_data = {**todays_date, **all_meta_data}

        # Update meta data df
        meta_data_df = meta_data_df.append(todays_meta_data, ignore_index=True)

        # Append the new data to meta_data csv
        print("Appending today's meta data for to meta_data.csv file")
        meta_data_df.to_csv('../data/meta_data.csv', mode='a', header=True)
        print("Scraping Complete\n")

        # Wait to do next scrape
        time_wait = 24
        print(f'Waiting {time_wait} hours...')
        time.sleep(time_wait * 3600)

