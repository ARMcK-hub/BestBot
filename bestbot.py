"""
BestBot
Author: Drew McKinney
Reference: https://github.com/Hari-Nagarajan/fairgame/blob/5e0f60f39dedf02ff6bec9a1131d6ea24c8553ec/utils/json_utils.py#L4
12/12/2020
"""

import requests
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry
from store.bestbuy.bestbuy_item import BestBuyItem

# Config Items
DEFAULT_HEADERS = {
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "accept-encoding": "gzip, deflate, br",
    "accept-language": "en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36",
    "origin": "https://www.bestbuy.com",
}

adapter = HTTPAdapter(
            max_retries=Retry(
                total=3,
                backoff_factor=1,
                status_forcelist=[429, 500, 502, 503, 504],
                method_whitelist=["HEAD", "GET", "OPTIONS", "POST"],
            )
        )

# Retrieve item details
sku = "6429440"

item = BestBuyItem(sku)

'''
look up items of concern in file
see what store they use
build store items
'''



session = requests.Session()
session.mount("https://", adapter)

response = session.get(item.url, headers=DEFAULT_HEADERS)

import json


def find_values(json_repr, id):
    results = []

    def _decode_dict(a_dict):
        try:
            results.append(a_dict[id])
        except KeyError:
            pass
        return a_dict

    json.loads(json_repr, object_hook=_decode_dict)  # Return value ignored.
    return results


with open("new.json", "w") as file:
    json.dump(json.dumps(response.json()), file)

item_json = find_values(
                json.dumps(response.json()), "buttonStateResponseInfos"
            )

# extracting out response details
response_availability = item_json[0][0]["buttonState"]
response_sku = item_json[0][0]["skuId"]

# validating in stock
if response_sku == sku and response_availability in [
    "ADD_TO_CART",
    "PRE_ORDER",
]:
    print("in Stock")

print(response_sku, response_availability)
print(item_json)