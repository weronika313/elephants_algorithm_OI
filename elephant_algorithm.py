from typing import List

INF = 1000000000


class ElephantAlgorithm:
    def __init__(self, data: dict):
        self.elephants_weight = data.get("elephants_weight")
        self.number_of_elephants = data.get("number_of_elephants")
        self.incorrect_order = data.get("incorrect_order")
        self.permutation = data.get("permutation")
        self.min_weight_in_graph = data.get("min_elephant_weight")
        self.belong_to_considered_cycle = [
            False for i in range(self.number_of_elephants)
        ]
        self.result = 0
        self.min_weight_in_cycle = INF
        self.sum_in_cycle = 0
        self.current_vertex = 0
        self.cycle_length = 0

    def get_minimal_effort(self):
        for beg in range(self.number_of_elephants - 1):
            if not self.belong_to_considered_cycle[beg]:
                self.reset_variables(beg)
                self.find_min_effort_in_cycle(beg)
                self.calculate_result()

        return self.result

    def reset_variables(self, beg):
        self.min_weight_in_cycle = INF
        self.sum_in_cycle = 0
        self.current_vertex = beg
        self.cycle_length = 0

    def find_min_effort_in_cycle(self, i):
        while not self.belong_to_considered_cycle[i]:
            self.min_weight_in_cycle = min(
                self.min_weight_in_cycle, self.elephants_weight[self.current_vertex]
            )
            self.sum_in_cycle += self.elephants_weight[self.current_vertex]
            self.current_vertex = self.permutation[self.current_vertex]
            self.belong_to_considered_cycle[self.current_vertex] = True
            self.cycle_length += 1

    def calculate_result(self):
        min_effort_with_method1 = (
            self.sum_in_cycle + (self.cycle_length - 2) * self.min_weight_in_cycle
        )
        min_effort_with_method2 = (
            self.sum_in_cycle
            + self.min_weight_in_cycle
            + (self.cycle_length + 1) * self.min_weight_in_graph
        )
        self.result += min(min_effort_with_method1, min_effort_with_method2)
