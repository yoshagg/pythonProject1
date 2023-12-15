from utils import get_data, get_filtered_data, get_formatted_data, hide_card_number, print_operations
from pytest_fixtures import dates, items
import datetime

def test_get_data():
    assert get_data() != None


def test_get_formatted_data(dates):
    assert get_formatted_data(dates[0]) == datetime.datetime(2019, 1, 5, 0, 52, 30, 108534)
    assert get_formatted_data(dates[1]) == datetime.datetime(2019, 7, 13, 18, 51, 29, 313309)


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

def test_hide_card_number(items):
    assert hide_card_number(items[0]["from"]) == "Счет  2** **** 3262"


def test_print_operations(items):
    assert print_operations(items) == ['2018-03-09 23:57:37.537412 Перевод организации \n Счет  2** **** 3262 -> Счет  2** **** 1315\n\n', '2019-01-05 00:52:30.108534 Перевод со счета на счет \n Счет  4** **** 8409 -> Счет  1** **** 8266\n\n', '2019-07-13 18:51:29.313309 Перевод с карты на счет \n Maes tr** **** 7170 -> Счет  9** **** 8612\n\n']
