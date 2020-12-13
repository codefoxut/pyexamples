
class KnapsackProblem:

    def __init__(self, num_of_items, capacity_of_knapsack, weight_of_items, profit_of_items):
        self.num = num_of_items
        self.capacity_of_knapsack = capacity_of_knapsack
        self.weight_of_items = weight_of_items
        self.profit_of_items = profit_of_items
        self.dp_table = [[0 for _ in range(capacity_of_knapsack + 1)]
                         for _ in range(num_of_items + 1)]

    def dynamic_programming_approach(self):

        for i in range(1, self.num + 1):
            for w in range(1, self.capacity_of_knapsack + 1):
                not_taking_item = self.dp_table[i-1][w]
                taking_item = 0

                if self.weight_of_items[i] <= w:
                    taking_item = self.profit_of_items[i] + \
                        self.dp_table[i-1][w - self.weight_of_items[i]]
                self.dp_table[i][w] = max(not_taking_item, taking_item)

    def show_result(self):
        print(self.dp_table)
        print("Total benefit: %d" % self.dp_table[self.num][self.capacity_of_knapsack])
        w = self.capacity_of_knapsack

        for i in range(self.num, 0, -1):
            if self.dp_table[i][w] != 0 and self.dp_table[i][w] != self.dp_table[i-1][w]:
                print("We take item #%d, with  value=%d" % (i, self.weight_of_items[i]))
                w = w - self.weight_of_items[i]


if __name__ == '__main__':
    # problem 1
    n = 5
    c = 10
    weights = [0, 1, 3, 4, 5, 6]
    profits = [0, 1, 4, 5, 7, 10]
    k = KnapsackProblem(n, c, weights, profits)
    k.dynamic_programming_approach()
    k.show_result()
    # problem 2
    n1 = 3
    c1 = 6
    weights1 = [0, 4, 2, 3]
    profits1 = [0, 10, 4, 7]
    k2 = KnapsackProblem(n1, c1, weights1, profits1)
    k2.dynamic_programming_approach()
    k2.show_result()
