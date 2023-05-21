from bs4 import BeautifulSoup
import requests
import pprint

########### MICROCONTROLLERS ##################################################
# url = 'https://www.chipdip.ru/catalog/ic-microcontrollers?p.0=ST+Microelectronics&ps=x3'
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
#     'Accept-Language': 'en-US,en;q=0.9',
#     'Referer': 'https://www.google.com'
# }
# response = requests.get(url, headers=headers)

# html_content = response.text

# with open('output.html', 'w', encoding='utf-8') as file:
#     file.write(html_content)

# print(html_content)

# with open ('output2.html') as file:
#     src = file.read()

# soup = BeautifulSoup(src, 'lxml')

# # Get all inside class = 'name'
# all_products = soup.find_all(class_='name')
#     # for each item in result get what is inside class = 'link' 
#     # this is the product name and a link)
# for item in all_products:
#     product = item.find(class_='link')
#     link = item.find('a')
#     url = link.get('href')
#     print(product.text, 'https://www.chipdip.ru'+str(url))


################MEMORY GROUP############################
url = 'https://www.chipdip.ru/catalog/v-f-and-f-v-converters?ps=x3&page=2'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Accept-Language': 'en-US,en;q=0.9',
    'Referer': 'https://www.google.com'
}
response = requests.get(url, headers=headers)

html_content = response.text

with open('output_bad2.html', 'w', encoding='utf-8') as file:
    file.write(html_content)

#print(html_content)

# with open ('output2.html') as file:
#     src = file.read()

# soup = BeautifulSoup(src, 'lxml')

# # Get all inside class = 'name'
# all_products = soup.find_all(class_='item__name')
#     # for each item in result get what is inside class = 'link' 
#     # this is the product name and a link)
# for item in all_products:
#     product = item.find(class_='link')
#     link = item.find('a')
#     url = link.get('href')
#     print(product.text, 'https://www.chipdip.ru'+str(url))


#with open ('output3.html') as file:
#    src = file.read()


#soup = BeautifulSoup(src, 'lxml')

# Get all with attr id starting with 'item'
#all_products = soup.select('[id^="item"]')
#all_products = soup.select('[id="item"]')



# for item in all_products:
#     # Get all object in class "link" (usually it's a container for products)
#     product = item.find(class_='link')
#     available = item.find(class_="item__avail item__avail_available nw")     # get a container with "Available NOW"
#     if not available:                                                        # check if container exist (sometimes not)
#         available = 0           # set to 0 if not exist
#         order_available = item.find(class_='item__avail item__avail_order nw')
#         #if order_available: 
#            # available = order_available.text
#     else:
#         available = available.text # if exist set to a value
#     link = item.find('a')
#     url = link.get('href')
#     print(f'{product.text} - https://www.chipdip.ru{url} - {available}')
