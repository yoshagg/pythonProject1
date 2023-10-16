import json, datetime

def get_data(data):
    with open (f"{data}", "r", encoding="utf-8") as file:
        d = json.load(file)
    return d

def get_filtered_data(data):
    data = [x for x in data if "state" in x and x["state"] == "EXECUTED"]
    return data

def get_last_values(data, last_values_count):
    data = sorted(data, lambda x: x["data"], reversed=True)
    data = data[:last_values_count]
    return data

def get_formatted_data(data):
    data_list = []
    date = datetime.strptime(row['date']), __format '%Y-%m-%dT%H:%M-%S%f')

#print(get_data("operations.json"))
