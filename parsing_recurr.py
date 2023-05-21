from bs4 import BeautifulSoup
import requests
import pprint
from pprint import pprint
import time

parsing_result = []
counter = 0

def get_product_preview_info(url, counter=0):
    print(f'1. - Request to ----- {url}')
    headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Accept-Language': 'en-US,en;q=0.9',
    'Referer': 'https://www.google.com'
}
    response = requests.get(url, headers=headers)
 #   time.sleep(3)
    src = response.content
    soup = BeautifulSoup(src, 'lxml')
    # Get main products container (1 pattern)
    product_column = soup.find(class_="items-column")

    # Get product containers (2 pattern options available)
    all_product_names = product_column.find_all(class_='with-hover')         # Pattern #1
    if all_product_names:
        product_container = all_product_names
    else:
        product_container = product_column.find_all(class_="item__content")     # Patter #2

    for index, item in enumerate(product_container):
        product_template = {}
        product_template['num'] = counter
        counter += 1
        # Get product names
        product_name = item.find(class_='link')
        product_template['display_name'] = product_name.text

        # Get product URL
        product_url =  'https://www.chipdip.ru' + product_name.get('href')
        product_template['url'] = product_url

        # Get info about product qty (4 patterns available)
        qty_class_patterns = ['item__avail item__avail_awaiting', 
                        'item__avail item__avail_order nw',
                        'item__avail item__avail_available nw',
                        'item__avail item__avail_no nw',
                        'item__avail item__avail_delivery']
        for pattern in qty_class_patterns:
            qty_info = item.find(class_=pattern)
            if qty_info:
                qty = qty_info 
        product_template['qty'] = qty.text
    #   print(index, product_name.text, qty.text)
        parsing_result.append(product_template)
        print(product_template)
    #pprint(parsing_result)
    # Check if Next page url exist and return one if any
    next_page = soup.find(class_='link no-visited pager__control pager__next')
    if next_page:
        next_page_url = 'https://www.chipdip.ru' + next_page.get('href')
        print(f'---------- NEXT PAGE FOUND-------- {next_page_url}')
        get_product_preview_info(next_page_url, counter)
    else:
        print('NO NEXT PAGE')
        with open('output3.txt', 'w') as file:
            pprint(parsing_result, stream=file)
        return pprint(parsing_result)

# Get src from file
# with open ('output8.html') as file:
#     src = file.read()
# soup = BeautifulSoup(src, 'lxml')

# Get src from URL
url = 'https://www.chipdip.ru/catalog/sensor-detector-interfaces?ps=x3'
get_product_preview_info(url)




'''QTY patterns

QTY Available, waiting
<div class="item__avail-w"><span class="item__avail item__avail_awaiting"><span class="nw">4-6 дней,</span> <span class="nw">1 шт.</span></span></div>
------------
No QTY, preorder
<div class="av_w2"><span class="item__avail item__avail_order nw" title="Для отправки запроса добавьте товар в корзину и оформите заказ">По запросу</span></div>
<td class="h_av"><div class="av_w"><span class="item__avail item__avail_order nw" title="Для отправки запроса добавьте товар в корзину и оформите заказ">По запросу</span></div></td>
----------------

QTY Available, no waiting
<div class="item__avail-w"><span class="item__avail item__avail_available nw">13 шт.</span></div>
-----------

No info
<td class="h_av"><div class="av_w"><span class="item__avail item__avail_no nw"></span></div></td> 
----------------

<div class="av_w2"><span class="item__avail item__avail_delivery"><span class="nw">3-4 дня,</span> <span class="nw">160 шт.<span class="with-icon has-alt-items" title="Имеются альтернативные предложения"></span></span></span></div>
------


<span class="item__avail item__avail_awaiting"> get qty and lead time
<span class="item__avail item__avail_order nw"> return "По запросу"
<span class="item__avail item__avail_available nw"> get qty
<span class="item__avail item__avail_no nw"> retun "Not available"


'''




