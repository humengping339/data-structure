class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 插入节点构建BST
def insert_bst(root, val):
    if root is None:
        return TreeNode(val)
    if val < root.val:
        root.left = insert_bst(root.left, val)
    else:
        root.right = insert_bst(root.right, val)
    return root

# 中序前驱：左子树最大值
def get_predecessor(node):
    cur = node.left
    while cur.right:
        cur = cur.right
    return cur

# 中序后继：右子树最小值
def get_successor(node):
    cur = node.right
    while cur.left:
        cur = cur.left
    return cur

# 中序前驱法删除节点
def delete_node_predecessor(root, target):
    if root is None:
        return None
    # 查找待删节点
    if target < root.val:
        root.left = delete_node_predecessor(root.left, target)
    elif target > root.val:
        root.right = delete_node_predecessor(root.right, target)
    else:
        # 叶子/单分支
        if root.left is None:
            return root.right
        if root.right is None:
            return root.left
        # 替换为前驱
        pre_node = get_predecessor(root)
        root.val = pre_node.val
        root.left = delete_node_predecessor(root.left, pre_node.val)
    return root

# 中序后继法删除节点
def delete_node_successor(root, target):
    if root is None:
        return None
    if target < root.val:
        root.left = delete_node_successor(root.left, target)
    elif target > root.val:
        root.right = delete_node_successor(root.right, target)
    else:
        if root.left is None:
            return root.right
        if root.right is None:
            return root.left
        # 替换为后继
        suc_node = get_successor(root)
        root.val = suc_node.val
        root.right = delete_node_successor(root.right, suc_node.val)
    return root

# 打印和截图同款树形，斜线位置适中居中
def print_tree_visual(root):
    if not root:
        print("空树")
        return
    from collections import deque
    node_map = {}
    queue = deque()
    # 根节点横坐标居中
    start_x = 30
    queue.append((root, 0, start_x))
    node_map[(0, start_x)] = str(root.val)
    max_level = 0

    # 遍历记录所有节点坐标
    while queue:
        node, level, x = queue.popleft()
        max_level = max(max_level, level)
        # 每层节点横向间距，保证斜线适中不拥挤
        gap = 12 // (level + 1)
        if node.left:
            l_x = x - gap
            queue.append((node.left, level + 1, l_x))
            node_map[(level + 1, l_x)] = str(node.left.val)
        if node.right:
            r_x = x + gap
            queue.append((node.right, level + 1, r_x))
            node_map[(level + 1, r_x)] = str(node.right.val)

    # 逐层打印节点行 + 斜线行
    for level in range(max_level + 1):
        node_line = [" "] * 60
        slash_line = [" "] * 60
        # 获取当前层全部节点
        current_nodes = [(lvl, x, val) for (lvl, x), val in node_map.items() if lvl == level]
        for lvl, x, val_str in current_nodes:
            # 写入节点数字
            val_len = len(val_str)
            pos = x - val_len // 2
            for i, c in enumerate(val_str):
                if 0 <= pos + i < 60:
                    node_line[pos + i] = c
            # 绘制居中斜线
            gap = 12 // (level + 1)
            left_child_key = (level + 1, x - gap)
            right_child_key = (level + 1, x + gap)
            if left_child_key in node_map:
                slash_line[x - 1] = "/"
            if right_child_key in node_map:
                slash_line[x + 1] = "\\"
        # 打印节点行
        print("".join(node_line).rstrip())
        # 非最后一层打印斜线行
        if level != max_level:
            print("".join(slash_line).rstrip())

# ===================== 作业 =====================
if __name__ == "__main__":
    values = [50, 30, 70, 20, 40, 60, 80]
    print("===== 题1：构建 BST =====")
    print("插入序列: [50, 30, 70, 20, 40, 60, 80]")
    root1 = None
    for v in values:
        root1 = insert_bst(root1, v)
    print("最终 BST 形态：")
    print_tree_visual(root1)

    print("\n===== 题2：删除根节点 50（中序前驱法） =====")
    root_pre = None
    for v in values:
        root_pre = insert_bst(root_pre, v)
    root_pre = delete_node_predecessor(root_pre, 50)
    print("删除后的 BST 形态 (用 40 替换 50)：")
    print_tree_visual(root_pre)

    print("\n===== 题2：删除根节点 50（中序后继法） =====")
    root2 = None
    for v in values:
        root2 = insert_bst(root2, v)
    root2 = delete_node_successor(root2, 50)
    print("删除后的 BST 形态 (用 60 替换 50)：")
    print_tree_visual(root2)
