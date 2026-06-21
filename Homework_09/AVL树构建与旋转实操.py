class AVLNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.height = 0  # 记录当前节点高度

# 获取节点高度
def get_height(node):
    if node is None:
        return -1
    return node.height

# 计算平衡因子 BF = 左子树高 - 右子树高
def get_balance(node):
    if node is None:
        return 0
    return get_height(node.left) - get_height(node.right)

# 右旋 LL失衡修复
def right_rotate(z):
    y = z.left
    T3 = y.right
    # 旋转
    y.right = z
    z.left = T3
    # 更新高度
    z.height = 1 + max(get_height(z.left), get_height(z.right))
    y.height = 1 + max(get_height(y.left), get_height(y.right))
    return y

# 左旋 RR失衡修复
def left_rotate(z):
    y = z.right
    T2 = y.left
    # 旋转
    y.left = z
    z.right = T2
    # 更新高度
    z.height = 1 + max(get_height(z.left), get_height(z.right))
    y.height = 1 + max(get_height(y.left), get_height(y.right))
    return y

# AVL插入递归函数，自动平衡
def avl_insert(root, val):
    # 1. 标准BST插入
    if root is None:
        return AVLNode(val)
    if val < root.val:
        root.left = avl_insert(root.left, val)
    elif val > root.val:
        root.right = avl_insert(root.right, val)
    else:
        return root  # 重复值不插入

    # 2. 更新当前节点高度
    root.height = 1 + max(get_height(root.left), get_height(root.right))

    # 3. 获取平衡因子判断失衡
    bf = get_balance(root)

    # LL 左左失衡 → 右旋
    if bf > 1 and val < root.left.val:
        print(f"失衡类型：LL，旋转轴：{root.val}，执行右旋")
        return right_rotate(root)
    # RR 右右失衡 → 左旋
    if bf < -1 and val > root.right.val:
        print(f"失衡类型：RR，旋转轴：{root.val}，执行左旋")
        return left_rotate(root)
    # LR 左右失衡 → 先左旋左孩子，再右旋根
    if bf > 1 and val > root.left.val:
        print(f"失衡类型：LR，旋转轴：{root.val}，先左旋左子节点，再右旋")
        root.left = left_rotate(root.left)
        return right_rotate(root)
    # RL 右左失衡 → 先右旋右孩子，再左旋根
    if bf < -1 and val < root.right.val:
        print(f"失衡类型：RL，旋转轴：{root.val}，先右旋右子节点，再左旋")
        root.right = right_rotate(root.right)
        return left_rotate(root)

    # 无失衡，直接返回
    return root

# 中序遍历（验证BST有序）
def inorder_traverse(root, res=None):
    if res is None:
        res = []
    if root:
        inorder_traverse(root.left, res)
        res.append(root.val)
        inorder_traverse(root.right, res)
    return res

# 带斜线+平衡因子标注的可视化打印
def print_avl_tree(root):
    if not root:
        print("空树")
        return
    from collections import deque
    node_info = dict()  # key:(level,x)  value:(val, balance_factor)
    q = deque()
    start_x = 35
    q.append((root, 0, start_x))
    node_info[(0, start_x)] = (root.val, get_balance(root))
    max_level = 0

    # BFS记录所有节点坐标、值、平衡因子
    while q:
        node, level, x = q.popleft()
        max_level = max(max_level, level)
        gap = 14 // (level + 1)
        if node.left:
            lx = x - gap
            q.append((node.left, level+1, lx))
            node_info[(level+1, lx)] = (node.left.val, get_balance(node.left))
        if node.right:
            rx = x + gap
            q.append((node.right, level+1, rx))
            node_info[(level+1, rx)] = (node.right.val, get_balance(node.right))

    # 逐层打印
    for lv in range(max_level + 1):
        node_line = [" "] * 70
        slash_line = [" "] * 70
        layer_nodes = [(l, x, val, bf) for (l, x), (val, bf) in node_info.items() if l == lv]
        for l, x, val, bf in layer_nodes:
            text = f"{val}({bf})"
            text_len = len(text)
            pos = x - text_len // 2
            for i, c in enumerate(text):
                if 0 <= pos + i < 70:
                    node_line[pos + i] = c
            # 绘制斜线
            gap = 14 // (lv + 1)
            left_key = (lv+1, x - gap)
            right_key = (lv+1, x + gap)
            if left_key in node_info:
                slash_line[x - 1] = "/"
            if right_key in node_info:
                slash_line[x + len(str(val))] = "\\"
        print("".join(node_line).rstrip())
        if lv != max_level:
            print("".join(slash_line).rstrip())

# ===================== 作业 =====================
if __name__ == "__main__":
    insert_seq = [30, 20, 10, 25, 40, 35, 50]
    avl_root = None
    print("======= AVL树分步插入演示 插入序列：[30, 20, 10, 25, 40, 35, 50] =======\n")
    for num in insert_seq:
        print(f"---------- 插入节点 {num} ----------")
        avl_root = avl_insert(avl_root, num)
        print("当前AVL树（节点格式：值(平衡因子)）：")
        print_avl_tree(avl_root)
        print()

    print("======= 最终AVL树中序遍历（验证BST有序） =======")
    in_order_list = inorder_traverse(avl_root)
    print("中序遍历结果：", in_order_list)
