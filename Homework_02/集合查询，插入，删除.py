from collections.abc import Sequence
from typing import Any

class MyCollection:
    def __init__(self, iterable: Sequence[Any]):
        """
        初始化自定义集合，底层使用列表存储
        :param iterable: 可迭代对象，用于初始化集合
        """
        self.iterable = list(iterable)

    def insert_last(self, element: Any) -> bool:
        """
        向集合末尾插入元素，若元素已存在则不插入
        :param element: 待插入的元素
        :return: 插入成功返回True，元素已存在返回False
        """
        # 遍历检查元素是否存在，存在直接返回False
        for item in self.iterable:
            if item == element:
                return False
        # 不存在则插入到末尾
        self.iterable.append(element)
        return True

    def contains(self, element: Any) -> bool:
        """
        查询元素是否存在于集合中
        :param element: 待查询的元素
        :return: 存在返回True，不存在返回False
        """
        # 遍历查找元素，找到返回True，遍历完没找到返回False
        for item in self.iterable:
            if item == element:
                return True
        return False

    def remove(self, element: Any) -> bool:
        """
        从集合中删除元素，若元素不存在则不操作
        :param element: 待删除的元素
        :return: 删除成功返回True，元素不存在返回False
        """
        # 先遍历确认元素是否存在
        for item in self.iterable:
            if item == element:
                self.iterable.remove(element)
                return True
        return False

# 测试代码
if __name__ == "__main__":
    num_list = [5, 8, 15, 28, 34]
    Coll = MyCollection(num_list)
    print(Coll.insert_last(9))
    print(Coll.iterable)              
    print(Coll.remove(9))
    print(Coll.iterable)
    print(Coll.contains(9))
