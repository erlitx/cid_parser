# CID Parser

## ./bulk_parse.py

Scrapes one or more chipdip.ru product pages and outputs a CSV with the columns:

1. URL of the page being scraped
2. JSON of the product description found
3. Markdown snippet derived from the description

Example usage:

```sh
# Scrape single page
./bulk_parse.py https://www.chipdip.ru/product0/8003076409

# Scrape multiple and save to file
./bulk_parse.py https://www.chipdip.ru/product0/8003076409 https://www.chipdip.ru/product/spu01m-05 > out.csv

# Scrape multiple from file (one URL per line) and save to file
cat examples/product_page_list.txt | xargs ./bulk_parse.py > out.csv
```
