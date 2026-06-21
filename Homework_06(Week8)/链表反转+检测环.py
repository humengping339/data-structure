# 定义链表节点
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# 单链表操作类
class LinkedList:
    def __init__(self):
        self.head = None

    # 尾部添加节点，用于快速构建链表
    def append(self, val):
        new_node = ListNode(val)
        if not self.head:
            self.head = new_node
            return
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = new_node

    # 打印链表（无环时使用）
    def print_list(self):
        res = []
        cur = self.head
        while cur:
            res.append(str(cur.val))
            cur = cur.next
        print("[" + ", ".join(res) + "]")

    # 作业1：链表反转 reverse()
    def reverse(self):
        prev = None
        cur = self.head
        while cur:
            # 保存下一个节点
            next_temp = cur.next
            # 反转当前节点指向
            cur.next = prev
            # 双指针后移
            prev = cur
            cur = next_temp
        # 反转后 head 变为原最后一个节点
        self.head = prev

    # 作业2：判断链表是否存在环 has_cycle()
    def has_cycle(self):
        slow = self.head
        fast = self.head
        while fast and fast.next:
            slow = slow.next         # 慢指针走1步
            fast = fast.next.next    # 快指针走2步
            if slow == fast:
                return True  # 快慢相遇，存在环
        return False  # 快指针走到末尾，无环


# ===================== 测试示例 =====================
if __name__ == "__main__":
    # 测试1：链表反转 reverse()
    print("===== 测试链表反转 =====")
    link1 = LinkedList()
    # 构建 [a,b,c] 这里用数字1,2,3代替a,b,c
    link1.append("a")
    link1.append("b")
    link1.append("c")
    print("原链表：", end="")
    link1.print_list()
    link1.reverse()
    print("反转后：", end="")
    link1.print_list()

    # 测试2：无环链表 has_cycle()
    print("\n===== 测试无环链表判环 =====")
    link2 = LinkedList()
    link2.append(1)
    link2.append(2)
    link2.append(3)
    link2.append(4)
    print("是否有环：", link2.has_cycle())

    # 测试3：构造有环链表 has_cycle()
    print("\n===== 测试环形链表判环 =====")
    link3 = LinkedList()
    link3.append(10)
    link3.append(20)
    link3.append(30)
    link3.append(40)
    # 手动制造环：尾节点指向第二个节点
    cur = link3.head
    ring_node = None
    idx = 0
    while cur.next:
        if idx == 1:
            ring_node = cur
        cur = cur.next
        idx += 1
    cur.next = ring_node
    print("是否有环：", link3.has_cycle())
