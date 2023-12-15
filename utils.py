import json
from datetime import datetime


def get_data():
    with open("operations.json", "r", encoding="utf-8") as file:
        return json.load(file)


def get_filtered_data(data):
    data = [x for x in data if "state" in x and x["state"] == "EXECUTED"]
    return data


def get_last_values(data, last_values_count=5):
    data = sorted(data, key=lambda x: x["date"], reverse=True)
    return data[:last_values_count]


def get_formatted_data(date: str):
    return datetime.strptime(date, '%Y-%m-%dT%H:%M:%S.%f')


def hide_card_number(numbers, to=False):
    if not to:
        return f"{numbers[:4]} {numbers[4:6]}** **** {numbers[-4:]}"
    else:
        return f"** {numbers[-4:]}"


def print_operations(data):
    operations = []
    for operation in data:
        if "from" in operation:
            date = get_formatted_data(operation['date'])
            operations.append(f"""{date} {operation['description']} \n {hide_card_number(operation["from"])}"""
                              f""" -> {hide_card_number(operation['to'])}\n\n""")
                             ## f"""{operation["amount"]} {operation['name']}\n\n""")
        else:
            pass
    return operations
