class Item():

    def __init__(self, id, store_url):
        self.id = id
        self.url = store_url.format(id)
        self.availability = None

    def update_availability(self, item_availability):
        self.availability = item_availability