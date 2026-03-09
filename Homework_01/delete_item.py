from typing import Iterable, Any

class DeleteItem:
    """
    从列表中删除指定索引元素的类
    """

    def __init__(self, iterable: Iterable[Any]):
        """
        :param iterable: 可迭代对象，从中删除元素
        """
        self.iterable = list(iterable)

    def delete(self, index_to_delete: int) -> None:
        """
        从列表中删除指定索引位置的元素
        :param index_to_delete: 要删除的元素索引
        """
        # 获取当前可迭代对象的长度
        length_of_iterable: int = len(self.iterable)

        # 从前往后移动元素，覆盖掉要删除的元素
        # 注意：必须从前往后移动，否则会覆盖掉还未处理的元素
        for i in range(index_to_delete, length_of_iterable - 1):
            self.iterable[i] = self.iterable[i + 1]

        # 删除列表最后一个多余的元素
        self.iterable.pop()

# 示例使用
if __name__ == "__main__":
    # 初始化一个水果列表
    fruits = ["apple", "banana", "cherry", "orange", "mango"]
    # 创建DeleteItem实例
    delete_item = DeleteItem(fruits)
    # 删除索引1的元素
    delete_item.delete(1)
    # 打印结果
    print(delete_item.iterable)  
