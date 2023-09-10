#!/usr/bin/env python3

import argparse
import csv
import sys
import requests
import json

from dataclasses import dataclass
from typing import Dict

from bs4 import BeautifulSoup
from pprint import pprint


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("url", nargs="+", help="Full product URL on www.chipdip.ru. Example: https://www.chipdip.ru/product0/8003076409")
    return parser.parse_args()


@dataclass
class Product:
    title: str
    tech_params: Dict[str, str]

    def to_json(self):
        return json.dumps({
            "title": self.title,
            "tech_params": self.tech_params
        }, ensure_ascii=False, indent=4)

    def to_markdown(self):
        spec_md = '\n'.join([f"- {key}: {value}" for (key, value) in self.tech_params.items()])
        return '\n'.join([
            '## Характеристики',
            '',
            spec_md,
        ])


def scrape_product_page(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
        'Accept-Language': 'en-US,en;q=0.9',
        'Referer': 'https://www.google.com'
    }

    response = requests.get(url, headers=headers)
    html = response.text

    soup = BeautifulSoup(html, 'lxml')
    title = soup.find('h1', itemprop='name').text

    # Get a technical params table class
    params_table = soup.find(class_='product__params')
    rows = params_table.find_all('tr')

    # Iterate over the table with parameters and get all the keys and values
    tech_params = {}
    for item in rows:
        param_name = item.find(class_='product__param-name')
        param_value = item.find(class_='product__param-value')
        if param_name is not None and param_value is not None:
            tech_params[param_name.text] = param_value.text

    return Product(title, tech_params)


def main():
    args = parse_args()
    csv_writer = csv.writer(sys.stdout)
    for url in args.url:
        product = scrape_product_page(url)
        csv_writer.writerow((url, product.to_json(), product.to_markdown()))


if __name__ == '__main__':
    main()
