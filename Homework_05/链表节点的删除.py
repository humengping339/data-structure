# 链表结点类
class Node:
    def __init__(self, data: str | int | float):
        self.data = data
        self.next_node = None
    def __repr__(self) -> str:
        return f"Node({self.data!r})"
# 链表类
class LinkedList:
    def __init__(self):
        self.first_node = None
    def __repr__(self) -> str:
        if not self.first_node:
            return "LinkedList([])"
        nodes = []
        current = self.first_node
        while current:
            nodes.append(str(current.data))
            current = current.next_node
        return f"LinkedList([{','.join(nodes)}])"

# 链表节点删除
def remove_at_index(self, index: int) -> str | int | float | None:
    # 空链表
    if not self.first_node:
        return None
    # 删除头结点 O(1)
    if index == 0:
        removed_data = self.first_node.data
        self.first_node = self.first_node.next_node
        return removed_data
    # 找到待删除节点的前一个节点
    current_node = self.first_node
    current_index = 0
    while current_index < index - 1:
        if not current_node:
            return None
        current_node = current_node.next_node
        current_index += 1
    # 越界判断
    if not current_node or not current_node.next_node:
        return None
    # 删除节点
    removed_data = current_node.next_node.data
    current_node.next_node = current_node.next_node.next_node
    return removed_data

LinkedList.remove_at_index = remove_at_index

# 链表构建
if __name__ == "__main__":
    # 创建结点
    node_1 = Node("have")
    node_2 = Node("a")
    node_3 = Node("fun")
    node_4 = Node("time")

    # 连接结点
    node_1.next_node = node_2
    node_2.next_node = node_3
    node_3.next_node = node_4

    # 创建链表，指定头结点
    list_ = LinkedList()
    list_.first_node = node_1

    # 测试删除
    print("原链表：", list_)
    print("删除索引4：", list_.remove_at_index(4))  # 索引越界
    print("删除后：", list_)
    print("删除索引1：", list_.remove_at_index(1))  # 删除 a
    print("删除后：", list_)
    print("删除索引0：", list_.remove_at_index(0))  # 删除 have
    print("删除后：", list_)
