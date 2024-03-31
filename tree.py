import time


class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


def create_binary_search_tree(keys):
    if not keys:
        return None

    root = TreeNode(keys[0])
    for key in keys[1:]:
        insert_node(root, key)
    return root


def insert_node(root, key):
    if root is None:
        return TreeNode(key)
    if key < root.key:
        root.left = insert_node(root.left, key)
    elif key > root.key:
        root.right = insert_node(root.right, key)
    return root


def count_nodes(root):
    if root is None:
        return 0
    else:
        return 1 + count_nodes(root.left) + count_nodes(root.right)


def count_nodes_iterative(root):
    if root is None:
        return 0

    stack = [root]
    node_count = 0

    while stack:
        current_node = stack.pop()
        node_count += 1

        if current_node.right:
            stack.append(current_node.right)
        if current_node.left:
            stack.append(current_node.left)

    return node_count


def indirect_count_nodes(root):
    return _indirect_count_nodes(root)


def _indirect_count_nodes(node):
    if node is None:
        return 0
    else:
        return 1 + indirect_count_nodes(node.left) + indirect_count_nodes(node.right)


def inorder_traversal(root):
    if root:
        inorder_traversal(root.left)
        print(root.key, end=" ")
        inorder_traversal(root.right)


num_nodes = 50
keys = [i for i in range(1, num_nodes + 1)]

root = create_binary_search_tree(keys)

print("Элементы дерева (в порядке возрастания):")
inorder_traversal(root)
print("")

start_time = time.time()
node_count = count_nodes(root)
end_time = time.time()
rec_time = end_time - start_time
print("Количество вершин в дереве рекурсивно:", node_count, ". Со временем:", rec_time)

start_time = time.time()
node_count = count_nodes_iterative(root)
end_time = time.time()
iter_time = end_time - start_time
print("Количество вершин в дереве итеративно:", node_count, ". Со временем:", iter_time)

start_time = time.time()
node_count = indirect_count_nodes(root)
end_time = time.time()
cos_iter_time = end_time - start_time
print("Количество вершин в дереве косвенно рекурсивно:", node_count, ". Со временем:", cos_iter_time)

