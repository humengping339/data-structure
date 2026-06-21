class TreeItem:
    def __init__(self, data=0, l_node=None, r_node=None):
        self.data = data
        self.l_node = l_node
        self.r_node = r_node


def list_build_tree(data_list):
    """将层序遍历列表（包含 None 空标记）构建为链式二叉树"""
    if not data_list or data_list[0] is None:
        return None

    top = TreeItem(data_list[0])
    task_queue = [top]
    cursor = 1
    while task_queue and cursor < len(data_list):
        current = task_queue.pop(0)

        # 构建左分支节点
        if cursor < len(data_list) and data_list[cursor] is not None:
            current.l_node = TreeItem(data_list[cursor])
            task_queue.append(current.l_node)
        cursor += 1

        # 构建右分支节点
        if cursor < len(data_list) and data_list[cursor] is not None:
            current.r_node = TreeItem(data_list[cursor])
            task_queue.append(current.r_node)
        cursor += 1

    return top


def show_tree_structure(root_item):
    """格式化打印二叉树可视化结构，节点对齐并生成父子连线"""
    if not root_item:
        return

    # 分层存储每层节点
    layer_container = []
    queue_task = [(root_item, 0)]
    while queue_task:
        node, layer_idx = queue_task.pop(0)
        if len(layer_container) <= layer_idx:
            layer_container.append([])
        layer_container[layer_idx].append(node)
        if node:
            queue_task.append((node.l_node if node.l_node else None, layer_idx + 1))
            queue_task.append((node.r_node if node.r_node else None, layer_idx + 1))

    total_layer = len(layer_container) - 1

    # 计算整体画布最大宽度
    canvas_width = 2 ** (total_layer + 1)

    # 保存每个节点的画布坐标
    coord_record = {}

    def depth_scan(node, pos_x, pos_y, span):
        if not node or pos_y > total_layer:
            return
        coord_record[(pos_x, pos_y)] = str(node.data)
        if node.l_node:
            depth_scan(node.l_node, pos_x - span // 2, pos_y + 1, span // 2)
        if node.r_node:
            depth_scan(node.r_node, pos_x + span // 2, pos_y + 1, span // 2)

    # 根节点居中开始递归计算坐标
    depth_scan(root_item, canvas_width // 2, 0, canvas_width // 2)

    output_lines = []

    for y in range(total_layer + 1):
        node_text = [' '] * (canvas_width + 1)
        link_text = [' '] * (canvas_width + 1)

        for (x, ly), val_str in coord_record.items():
            if ly == y:
                # 写入节点字符
                for i, ch in enumerate(val_str):
                    node_text[x + i] = ch

                # 遍历查找子节点绘制斜线
                for (child_x, child_y), child_val in coord_record.items():
                    if child_y == y + 1:
                        # 左子节点
                        if child_x < x and abs(child_x + len(child_val) // 2 - x) < 5:
                            line_pos = x - 1
                            if line_pos >= 0:
                                link_text[line_pos] = '/'
                        # 右子节点
                        elif child_x > x and abs(child_x + len(child_val) // 2 - (x + len(val_str) - 1)) < 5:
                            line_pos = x + len(val_str)
                            if line_pos < len(link_text):
                                link_text[line_pos] = '\\'

        line_node = ''.join(node_text).rstrip()
        line_link = ''.join(link_text).rstrip()

        if line_node:
            output_lines.append(line_node)
        if line_link and y < total_layer:
            output_lines.append(line_link)

    # 逐行打印结果
    for line in output_lines:
        if line.strip():
            print(line)


# 原始输入数组
input_arr = [10, 5, 15, 3, 7, None, 20]

# 构建二叉树
tree_root = list_build_tree(input_arr)

print("还原后的二叉树形态：")
print()
show_tree_structure(tree_root)
