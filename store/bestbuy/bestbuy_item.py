from core.item import Item
from core.network.adapter import get_adapter
from core.utils.find_values import find_values
from requests import Session
from json import dump, dumps


class BestBuyItem(Item):
    # Config Items
    DEFAULT_HEADERS = {
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36",
        "origin": "https://www.bestbuy.com",
    }

    def __init__(self, product_data):
        self.store_url = "https://www.bestbuy.com/api/tcfb/model.json?paths=%5B%5B%22shop%22%2C%22scds%22%2C%22v2%22%2C%22page%22%2C%22tenants%22%2C%22bbypres%22%2C%22pages%22%2C%22globalnavigationv5sv%22%2C%22header%22%5D%2C%5B%22shop%22%2C%22buttonstate%22%2C%22v5%22%2C%22item%22%2C%22skus%22%2C{}%2C%22conditions%22%2C%22NONE%22%2C%22destinationZipCode%22%2C%22%2520%22%2C%22storeId%22%2C%22%2520%22%2C%22context%22%2C%22cyp%22%2C%22addAll%22%2C%22false%22%5D%5D&method=get"
        super(BestBuyItem, self).__init__(product_data)

    def get_page(self):

        adapter = get_adapter()
        session = Session()
        session.mount("https://", adapter)
        self.response = session.get(self.url, headers=BestBuyItem.DEFAULT_HEADERS)
        return

    def parse_page(self):
        item_json = find_values(
                        dumps(self.response.json()), "buttonStateResponseInfos"
                    )
        
        # extracting out response details
        self.response_availability = item_json[0][0]["buttonState"]
        self.response_sku = item_json[0][0]["skuId"]
    
    def check_availability(self):
        # validating in stock
        if self.response_sku == self.id and self.response_availability in [
            "ADD_TO_CART",
            "PRE_ORDER",
        ]:
            self.update_availability(True)
        else:
            self.update_availability(False)
        return self.get_availability()


    def get_availability(self):
        return self.availability


    def get_cart_url(self):
        cart_url = f"https://secure.newegg.com/Shopping/AddToCart.aspx?ItemList={self.id}"
    
    def filter_items():
        pass
