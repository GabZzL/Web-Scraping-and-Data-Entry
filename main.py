from scraping_data import WebScraping
from fill_out_data import GoogleForms

# set up the urls to use
ZILLOW_URL = "zillow_url"
FORM_URL = "form_url"

# use the WebScraping class to get the lists with the rooms information
scraping = WebScraping(ZILLOW_URL)
url_data = scraping.get_url()
address_data = scraping.get_address()
price_data = scraping.get_price()

# create a single list with the rooms information
rooms_list = [(url, address, price) for url, address, price in zip(url_data, address_data, price_data)]

# create a new form object, send the form url and the rooms list
# the method fill_out automatically will respond the answers in the form
form = GoogleForms(FORM_URL)
form.fill_out(rooms_list)
