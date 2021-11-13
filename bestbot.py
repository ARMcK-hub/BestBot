"""
BestBot
Author: Drew McKinney
Reference: https://github.com/Hari-Nagarajan/fairgame/blob/5e0f60f39dedf02ff6bec9a1131d6ea24c8553ec/utils/json_utils.py#L4
12/12/2020
"""

from store.bestbuy.bestbuy_item import BestBuyItem
from core.contact_methods import EmailContact, PhoneContact
from core.utils import ConfigurationProvider, write_log, clear_log, next_time
from time import time, sleep

class ProductFoundException(Exception):
    pass

Config = ConfigurationProvider().config

product_data = Config["products"]
notification_data = Config["contacts"]

# initializing runtime log
clear_log()
sleep(2)
write_log("Script Initiated")


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
write_log("Contacts Set", [c.contact for c in contact_list])


# lookup products info & create product objects
# @TODO create strat per item
product_list = []
for product in product_data:
    item = BestBuyItem(product)
    product_list.append(item)
write_log("Products Set", [p.name for p in product_list])


# loop executors
try:
    while True:
        loop_start = int(time())
        write_log("Started Loop")

        # looking through product list for availability
        for product in product_list:
            product.get_page()
            product.parse_page()
            product.check_availability()
            if product.get_availability() == True:
                write_log("IN STOCK!", product.name)

                # sending notifications
                for contact in contact_list:
                    write_log("Notification Sent", contact.contact)
                    contact.construct_message(product)
                    contact.notify()
                raise ProductFoundException
            else:
                write_log("OOS", product.name)

        # wait for next sys minute
        if (time() < loop_start + 60) or (int(time()) % 60 == 0) :
            write_log("Wait Initiated")
            next_time(60)

# handeling script termination on product found
except ProductFoundException:
    write_log("Terminating Script", "Product Found")

# handeling script failure notification
except Exception as e:
    write_log("Terminating Script", e)
    for contact in contact_list:
        write_log("Notification Sent", contact.contact)
        contact.construct_except_message(e)
        contact.notify()
