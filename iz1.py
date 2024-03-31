import matplotlib.pyplot as plt
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


# Создание трех бинарных деревьев для тестирования
tree1 = create_binary_tree()
tree2 = create_binary_tree()
tree3 = create_binary_tree()

# Списки для хранения времени выполнения каждой функции
recursive_times = []
iterative_times = []

# Измерение времени выполнения для каждой функции на каждом дереве
for tree in [tree1, tree2, tree3]:
    start_time = time.time()
    count_leaves_recursive(tree)
    end_time = time.time()
    recursive_times.append(end_time - start_time)

    start_time = time.time()
    count_leaves_iterative(tree)
    end_time = time.time()
    iterative_times.append(end_time - start_time)

# Построение графика
plt.plot(recursive_times, label='Recursive')
plt.plot(iterative_times, label='Iterative')
plt.xlabel('Tree')
plt.ylabel('Time (s)')
plt.title('Comparison of Recursive and Iterative Leaf Counting')
plt.legend()
plt.show()
