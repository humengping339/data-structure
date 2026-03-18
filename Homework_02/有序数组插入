from typing import Any
from collections.abc import Sequence

class OrderedArrayInsert:
    def __init__(self, iterable: Sequence[Any]):
        """
        初始化有序数组插入类
        :param iterable: 可迭代对象，将被转换为列表存储
        """
        self.iterable = list(iterable)  # 将输入的可迭代对象转换为列表，作为底层存储结构

    def insert(self, element: Any) -> None:
        """
        向有序数组中插入元素，保持数组有序性
        :param element: 待插入的元素
        :return: 无返回值
        """
        insert_index = 0  # 初始化插入位置索引，默认从0开始
        current_len = len(self.iterable)  # 获取当前数组的长度

        # 遍历数组，找到第一个大于待插入元素的位置，即为插入位置
        for index, value in enumerate(self.iterable):
            if element < value:
                insert_index = index  # 记录当前索引为插入位置
                break  # 找到位置后终止遍历
        else:
            # 若遍历完所有元素仍未找到更大的值，说明待插入元素最大，插入位置为数组末尾
            insert_index = current_len

        # 提前在数组末尾追加一个空字符串，为插入元素预留空间（模拟数组扩容）
        self.iterable.append("")

        # 从后往前移动元素，为待插入元素腾出位置
        # 注意：必须从后往前遍历，否则会覆盖未移动的元素
        for i in range(current_len, insert_index, -1):
            self.iterable[i] = self.iterable[i - 1]  # 将前一个位置的元素后移一位
        # 将待插入元素放入预留的插入位置
        self.iterable[insert_index] = element

# 测试代码
OrderedArray = [5, 17, 26, 38, 58, 77]
New_OrderedAarray = OrderedArrayInsert(OrderedArray)
New_OrderedAarray.insert(29)
print(New_OrderedAarray.iterable)
New_OrderedAarray.insert(84)
print(New_OrderedAarray.iterable)
