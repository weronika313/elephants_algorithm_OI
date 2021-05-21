class FileReader:
    def __init__(self, file_name):
        self.file_name = file_name
        self.lines = None
        self.number_of_elephants = None
        self.incorrect_order = None
        self.permutation = None
        self.elephants_weights = None
        self.min_elephant_weight = 1000000000

    def read_file(self):
        try:
            file = open(self.file_name, "r")
            self.lines = file.readlines()
            file.close()
            self.extract_data_from_file()
            return self.get_data()

        except FileNotFoundError:
            print(f"The file {self.file_name} doesn't exist")
        except PermissionError:
            print(f"You don't have permission to read this file {self.file_name}")
        except Exception as e:
            print(e)

    def get_data(self):
        data = {
            "number_of_elephants": self.number_of_elephants,
            "elephants_weight": self.elephants_weights,
            "incorrect_order": self.incorrect_order,
            "permutation": self.permutation,
            "min_elephant_weight": self.min_elephant_weight,
        }

        return data

    def extract_data_from_file(self):
        self.get_number_of_elephants()
        self.create_lists()
        self.get_elephants_weight()
        self.get_incorrect_order()
        self.get_permutation()

    def create_lists(self):
        self.elephants_weights = [0 for i in range(self.number_of_elephants)]
        self.permutation = [-1 for i in range(self.number_of_elephants)]
        self.incorrect_order = [-1 for i in range(self.number_of_elephants)]

    def get_number_of_elephants(self):
        try:
            number_of_elephants_line = self.lines[0]
            self.number_of_elephants = int(number_of_elephants_line.strip())
        except ValueError:
            print("Cannot convert number of elephants to int")

    def get_elephants_weight(self):
        elephants_weights_line = self.lines[1]
        elephants_weights_line.strip()
        elephants_weights_line = elephants_weights_line.split(" ")
        try:
            for i, weight in enumerate(elephants_weights_line):
                self.elephants_weights[i] = int(weight)
                self.min_elephant_weight = min(self.min_elephant_weight, int(weight))

        except ValueError:
            print("Cannot convert elephant weight to int")
        except IndexError:
            print("Too many elephants weight")

    def get_incorrect_order(self):
        incorrect_order_line = self.lines[2]
        incorrect_order_line.strip()
        incorrect_order_line = incorrect_order_line.split(" ")
        try:
            for i, number in enumerate(incorrect_order_line):
                self.incorrect_order[i] = int(number) - 1
        except ValueError:
            print("Cannot convert value from incorrect order to int")
        except IndexError:
            print("Too many items in incorrect order line")

    def get_permutation(self):
        correct_order_line = self.lines[3]
        correct_order_line.strip()
        correct_order_line = correct_order_line.split(" ")
        try:
            for i, number in enumerate(correct_order_line):
                self.permutation[int(number) - 1] = self.incorrect_order[i]
        except ValueError:
            print("Cannot convert value from incorrect order to int")
        except IndexError:
            print("Too many items in incorrect order line")
