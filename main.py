from utils import get_data, get_filtered_data, get_formatted_data, get_last_values, print_operations

def run():
    d = get_data()
    d = get_filtered_data(d)
    d = get_last_values(d, 5)
    readyline = "".join(print_operations(d))
    print(readyline)

if __name__ == "__main__":
    run()

### second commit
