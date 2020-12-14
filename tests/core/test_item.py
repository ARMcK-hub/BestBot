from core.item import Item

def test_can_create():

    test_id = "test_id"
    test_store_url = "test_store_url"

    Item(test_id, test_store_url)

    assert True