import sys
from elephant_algorithm import ElephantAlgorithm
from read_file import FileReader

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    file_reader = FileReader("data.txt")
    data = file_reader.read_file()

    el_alg = ElephantAlgorithm(data)
    print(el_alg.get_minimal_effort())




# See PyCharm help at https://www.jetbrains.com/help/pycharm/
