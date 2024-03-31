import random
import math
import time


class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def create_binary_tree():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)
    return root


def count_leaves_recursive(root):
    if root is None:
        return 0
    if root.left is None and root.right is None:
        return 1
    return count_leaves_recursive(root.left) + count_leaves_recursive(root.right)


def count_leaves_iterative(root):
    if root is None:
        return 0
    stack = [root]
    count = 0
    while stack:
        node = stack.pop()
        if node.left is None and node.right is None:
            count += 1
        if node.right is not None:
            stack.append(node.right)
        if node.left is not None:
            stack.append(node.left)
    return count


def greedy_knapsack(values, weights, capacity):
    n = len(values)
    ratios = [(values[i] / weights[i], i) for i in range(n)]
    ratios.sort(reverse=True)
    total_value = 0
    total_weight = 0
    selected_items = []

    for ratio, i in ratios:
        if total_weight + weights[i] <= capacity:
            total_value += values[i]
            total_weight += weights[i]
            selected_items.append(i)

    return total_value, selected_items


def dynamic_knapsack(values, weights, capacity):
    n = len(values)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - weights[i - 1]] + values[i - 1])
            else:
                dp[i][w] = dp[i - 1][w]

    total_value = dp[n][capacity]

    w = capacity
    selected_items = []
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            selected_items.append(i - 1)
            w -= weights[i - 1]

    selected_items.reverse()
    return total_value, selected_items


def simulated_annealing_knapsack(values, weights, capacity, temperature=100, cooling_rate=0.99):
    current_solution = [0] * len(values)
    current_value = 0

    for i in range(len(values)):
        current_solution[i] = random.randint(0, 1)
        current_value += current_solution[i] * values[i]

    best_solution = current_solution[:]
    best_value = current_value

    while temperature > 1:
        neighbor_solution = current_solution[:]
        index = random.randint(0, len(values) - 1)
        neighbor_solution[index] = 1 - neighbor_solution[index]

        neighbor_value = 0
        for i in range(len(values)):
            neighbor_value += neighbor_solution[i] * values[i]

        if neighbor_value > current_value or random.random() < math.exp(
                (neighbor_value - current_value) / temperature):
            current_solution = neighbor_solution[:]
            current_value = neighbor_value

        if current_value > best_value:
            best_solution = current_solution[:]
            best_value = current_value

        temperature *= cooling_rate

    selected_items = [i for i in range(len(best_solution)) if best_solution[i] == 1]
    return best_value, selected_items


def branch_and_bound_knapsack(values, weights, capacity):
    n = len(values)
    sorted_items = sorted(range(n), key=lambda i: values[i] / weights[i], reverse=True)

    def bound(i, current_weight, current_value):
        total_weight = current_weight
        total_value = current_value
        while i < n and total_weight + weights[sorted_items[i]] <= capacity:
            total_weight += weights[sorted_items[i]]
            total_value += values[sorted_items[i]]
            i += 1
        if i < n:
            total_value += (capacity - total_weight) * (values[sorted_items[i]] / weights[sorted_items[i]])
        return total_value

    def knapsack_helper(i, current_weight, current_value):
        if current_weight > capacity:
            return float('-inf')

        if i == n:
            return current_value

        if current_weight + weights[sorted_items[i]] > capacity:
            return current_value + (capacity - current_weight) * (values[sorted_items[i]] / weights[sorted_items[i]])

        with_item = knapsack_helper(i + 1, current_weight + weights[sorted_items[i]],
                                    current_value + values[sorted_items[i]])
        without_item = knapsack_helper(i + 1, current_weight, current_value)

        return max(with_item, without_item)

    max_value = knapsack_helper(0, 0, 0)
    selected_items = []
    current_weight = 0
    current_value = 0

    for i in range(n):
        if current_weight + weights[sorted_items[i]] <= capacity and current_value + values[sorted_items[i]] <= max_value:
            current_weight += weights[sorted_items[i]]
            current_value += values[sorted_items[i]]
            selected_items.append(sorted_items[i])

    return current_value, selected_items


# Создаем данные для задачи о рюкзаке
N = 10
values = [random.randint(1, 100) for _ in range(N)]
weights = [random.randint(1, 10) for _ in range(N)]
capacity = sum(weights) // 2  # Выбираем емкость рюкзака как половину суммы весов объектов

# Сравниваем результаты для всех методов
methods = {
    "Greedy": greedy_knapsack,
    "Dynamic Programming": dynamic_knapsack,
    "Simulated Annealing": simulated_annealing_knapsack,
    "Branch and Bound": branch_and_bound_knapsack
}

for method_name, method_func in methods.items():
    start_time = time.time()
    result = method_func(values, weights, capacity)
    end_time = time.time()
    print(
        f"{method_name}: Total Value = {result[0]}, Selected Items = {result[1]}, Time = {end_time - start_time} seconds")
