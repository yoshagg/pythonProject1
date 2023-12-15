from utils import get_data, get_filtered_data, get_formatted_data, get_last_values, print_operations
from pytest_fixtures import dates, items

def test_get_data():
    assert get_data() != None


def test_get_formatted_data(dates):
    assert get_formatted_data(dates[0]) == "2019-01-05 00:52:30.108534"
    assert get_formatted_data(dates[1]) == "2019-07-13 18:51:29.313309"


def test_get_filtered_data(items):
    assert get_filtered_data(items) == [{
        "id": 921286598,
        "state": "EXECUTED",
        "date": "2018-03-09T23:57:37.537412",
        "operationAmount": {
            "amount": "25780.71",
            "currency": {
                "name": "руб.",
                "code": "RUB"
            }
        },
        "description": "Перевод организации",
        "from": "Счет 26406253703545413262",
        "to": "Счет 20735820461482021315"
    },
        {
            "id": 207126257,
            "state": "EXECUTED",
            "date": "2019-07-15T11:47:40.496961",
            "operationAmount": {
                "amount": "92688.46",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Открытие вклада",
            "to": "Счет 35737585785074382265"
        },
        {
            "id": 667307132,
            "state": "EXECUTED",
            "date": "2019-07-13T18:51:29.313309",
            "operationAmount": {
                "amount": "97853.86",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод с карты на счет",
            "from": "Maestro 1308795367077170",
            "to": "Счет 96527012349577388612"
        }
    ]
