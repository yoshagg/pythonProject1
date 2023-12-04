from utils import get_data, get_filtered_data, get_last_values, print_operations

def test_get_data():
    assert get_data() != None

def test_get_filtered_data():
    d = get_data()
    assert get_filtered_data(d)




