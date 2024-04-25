import requests
from bs4 import BeautifulSoup


# init the class with the list to use, url page, and soup object
class WebScraping:
    def __init__(self, url):
        self.url = url
        self.response = requests.get(url=self.url)
        self.data = self.response.text
        self.soup = BeautifulSoup(self.data, "html.parser")
        self.floors_url_list = []
        self.floors_address_list = []
        self.floor_price_list = []

    # return a list with the urls
    def get_url(self):
        floors_anchor = self.soup.select(selector="li .StyledPropertyCardDataWrapper a")
        for url in floors_anchor:
            self.floors_url_list.append(url.get("href"))
        return self.floors_url_list

    # return a list with the address
    def get_address(self):
        floors_anchor = self.soup.select(selector="li .StyledPropertyCardDataWrapper a")
        for address in floors_anchor:
            text = address.getText()
            text_without_spaces = text.replace(" ", "")
            clean_text = text_without_spaces.replace("\n", "")
            self.floors_address_list.append(clean_text)
        return self.floors_address_list

    # return a list with the prices
    def get_price(self):
        floors_price_data = self.soup.select(selector=".PropertyCardWrapper__StyledPriceLine")
        for price in floors_price_data:
            text = price.getText()
            clean_text = text[:6]
            self.floor_price_list.append(clean_text)
        return self.floor_price_list
