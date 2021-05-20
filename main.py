import sys
from elephant import Elephant


def get_number_of_elephants(file):
    try:
        number_of_elephants = file.readline()
        number_of_elephants = int(number_of_elephants.strip())
        return number_of_elephants
    except ValueError:
        print("Cannot convert number of elephants to int")


def get_elephants(file):
    elephants_weight = file.readline()
    elephants_weight.strip()
    elephants_weight = elephants_weight.split(" ")
    try:
        elephants = [Elephant(count, int(weight)) for count, weight in enumerate(elephants_weight)]
        return elephants
    except ValueError:
        print("Cannot convert elephant weight to int")


def get_incorrect_order(file):
    incorrect_order_line = file.readline()
    incorrect_order_line.strip()
    incorrect_order_line = incorrect_order_line.split(" ")
    try:
        incorrect_order = [int(number) for number in incorrect_order_line]
        return incorrect_order
    except ValueError:
        print("Cannot convert value from incorrect order to int")


def get_correct_order(file):
    correct_order_line = file.readline()
    correct_order_line.strip()
    correct_order_line = correct_order_line.split(' ')
    try:
        correct_order = [int(number) for number in correct_order_line]
        return correct_order
    except ValueError:
        print("Cannot convert value from correct order to int")


def read_data(file_name):
    try:
        file = open(file_name, 'r')
        data = {
            'number_of_elephants': get_number_of_elephants(file),
            'elephants': get_elephants(file),
            'incorrect_order': get_incorrect_order(file),
            'correct_order': get_correct_order(file)
        }

        return data

    except FileNotFoundError:
        print(f"The file {file_name} doesn't exist")
    except PermissionError:
        print(f"You don't have permission to read this file {file_name}")
    except Exception as e:
        print(e)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    data = read_data("data.txt")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
