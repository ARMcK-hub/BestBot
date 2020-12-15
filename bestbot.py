"""
BestBot
Author: Drew McKinney
Reference: https://github.com/Hari-Nagarajan/fairgame/blob/5e0f60f39dedf02ff6bec9a1131d6ea24c8553ec/utils/json_utils.py#L4
12/12/2020
"""
from data.product import product_data
from data.notifications import notification_data

from time import sleep
from store.bestbuy.bestbuy_item import BestBuyItem
from core.network.adapter import get_adapter
from core.contact_methods.email_contact import EmailContact
from core.contact_methods.phone_contact import PhoneContact


# lookup notify info & create notify objects
contact_list = []
for contact_method in notification_data:
    if contact_method == "email":
        contact = EmailContact(notification_data[contact_method])
    elif contact_method == "phone":
        contact = PhoneContact(notification_data[contact_method])
    else:
        raise Exception("Invalid contact method input. Check data->notifications.py to ensure all methods are 'email' or 'phone'.")
    contact_list.append(contact)


# lookup products info & create product objects
# @TODO create strat per item
product_list = []
for product in product_data:
    item = BestBuyItem(product_data[product])
    product_list.append(item)

# loop executors
for product in product_list:
    product.get_page()
    product.parse_page()
    product.check_availability()
    if product.get_availability() == True:
        print(f"adding {product.Name} to cart")
    else:
        print(f"{product.Name} OOS")
    sleep(5)

