import requests
from bs4 import BeautifulSoup
from .parser import parse_product_page

class Scraper:
    def __init__(self):
        self.base_url = "https://example-ecommerce.com"
    
    def scrape_data(self):
        products = []
        for i in range(1, 3):  # Example: scrape first 2 pages
            url = f"{self.base_url}/products?page={i}"
            response = requests.get(url)
            soup = BeautifulSoup(response.content, 'html.parser')
            products.extend(parse_product_page(soup))
        return products
