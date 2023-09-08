from bs4 import BeautifulSoup
import requests
import os
from pprint import pprint

# URL to parse
url = 'https://www.chipdip.ru/product0/8003076409'


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Accept-Language': 'en-US,en;q=0.9',
    'Referer': 'https://www.google.com'
}
response = requests.get(url, headers=headers)
src = response.text


######## READ FROM SAVED FILE #############
# with open ('output1.html') as file:
#     src = file.read()


soup = BeautifulSoup(src, 'lxml')
product = {}
product['tech_params'] = {}
title = soup.find('h1', itemprop='name')
product['title'] = title.text

# Get a technical params table class
params_table = soup.find(class_='product__params')
rows = params_table.find_all('tr')
# download = soup.find(class_='product__documentation ptext')

# Iterate over the table with parameters and get all the keys and values
for item in rows:
    param_name = item.find(class_='product__param-name')
    param_value = item.find(class_='product__param-value')
    if param_name is not None and param_value is not None:
        product['tech_params'][param_name.text] = param_value.text
        #print(f' | {param_name.text} : {param_value.text} |')


pprint(product)


#SAVE RESULT
# current_path = '/home/erlit/parsing/cid_parser/output'
# filename = 'output1.html'

# # Create the full path by joining the current path and filename
# full_path = os.path.join(current_path, filename)
# # Write the html_content to the file
# with open(full_path, 'w', encoding='utf-8') as file:
#     file.write(product)








