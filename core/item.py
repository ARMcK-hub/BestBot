class Item(object):

    def __init__(self, product_data):
    # id, store_url):
        self.feature_list = []
        for feature in product_data:
            self.__setitem__(feature, product_data[feature])
            self.feature_list.append(feature)

        self.url = self.store_url.format(self.id)
        self.availability = None

    def update_availability(self, item_availability):
        self.availability = item_availability


    def __setitem__(self, key, value):
        setattr(self, key, value)

    def __getitem__(self, key):
        return getattr(self, key)
