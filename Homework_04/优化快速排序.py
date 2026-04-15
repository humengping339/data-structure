from collections.abc import Sequence
import random

class QuickSort:
    def __init__(self, arr: Sequence[int | float]):
        self.arr: list[int | float] = list(arr)
        self.length: int = len(arr)

    def partition(self, left_index: int, right_index: int) -> int:
        pivot_index = right_index
        pivot = self.arr[pivot_index]
        right_pointer = right_index - 1
        left_pointer = left_index

        while True:
            while left_pointer <= right_pointer and self.arr[left_pointer] < pivot:
                left_pointer += 1
            while left_pointer <= right_pointer and self.arr[right_pointer] > pivot:
                right_pointer -= 1
            if left_pointer >= right_pointer:
                break
            self.arr[left_pointer], self.arr[right_pointer] = self.arr[right_pointer], self.arr[left_pointer]

        self.arr[left_pointer], self.arr[pivot_index] = self.arr[pivot_index], self.arr[left_pointer]
        return left_pointer

    # 随机轴分区
    def randomized_partition(self, left_index: int, right_index: int) -> int:
        rand_idx = random.randint(left_index, right_index)
        self.arr[rand_idx], self.arr[right_index] = self.arr[right_index], self.arr[rand_idx]
        return self.partition(left_index, right_index)

    def sort(self, left_index: int | None = None, right_index: int | None = None) -> list[int | float]:
        if left_index is None:
            left_index = 0
        if right_index is None:
            right_index = self.length - 1

        if right_index - left_index <= 0:
            return self.arr

        pivot_position = self.randomized_partition(left_index, right_index)
        self.sort(left_index, pivot_position - 1)
        self.sort(pivot_position + 1, right_index)
        return self.arr

# 测试
if __name__ == "__main__":
    test_arr = [0, 6, 2, 1, 8, 4]
    qs = QuickSort(test_arr)
    print("原始数组：", test_arr)
    print("随机轴快排结果：", qs.sort())
