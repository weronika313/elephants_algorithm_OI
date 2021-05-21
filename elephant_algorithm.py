from typing import List
INF = 1000000000

class ElephantAlgorithm:
    def __init__(self, data:dict):
        self.elephants_weight = data.get('elephants_weight')
        self.number_of_elephants = data.get('number_of_elephants')
        self.incorrect_order = data.get('incorrect_order')
        self.permutation = data.get('permutation')
        self.min_weight_in_graph = data.get('min_elephant_weight')
        self.belong_to_considered_cycle = [False for i in range(self.number_of_elephants)]
        self.result = 0

    def get_minimal_effort(self):
        for i in range(self.number_of_elephants-1):
            if not self.belong_to_considered_cycle[i]:
                min_weight_in_cycle = INF
                sum_in_cycle = 0
                current_vertex = i
                cycle_length = 0

                while(1):

                    min_weight_in_cycle = min(min_weight_in_cycle, self.elephants_weight[current_vertex])
                    sum_in_cycle += self.elephants_weight[current_vertex]
                    current_vertex = self.permutation[current_vertex]
                    self.belong_to_considered_cycle[current_vertex] = True
                    cycle_length += 1
                    if current_vertex == i:
                        break

                self.calculate_result(sum_in_cycle, cycle_length, min_weight_in_cycle)

        return self.result

    def calculate_result(self, sum_in_cycle, cycle_length, min_weight_in_cycle):
        min_effort_with_method1 = sum_in_cycle + (cycle_length - 2) * min_weight_in_cycle
        min_effort_with_method2 = sum_in_cycle + min_weight_in_cycle + (cycle_length + 1) * self.min_weight_in_graph

        self.result += min(min_effort_with_method1, min_effort_with_method2)





