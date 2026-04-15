from collections.abc import Sequence

class QuickSort:
    def __init__(self, arr: Sequence[int | float]):
        self.arr: list[int | float] = list(arr)
        self.length: int = len(arr)

    # 三路快排
    def three_way_sort(self, left_index: int | None = None, right_index: int | None = None) -> list[int | float]:
        if left_index is None:
            left_index = 0
        if right_index is None:
            right_index = self.length - 1

        if right_index - left_index <= 0:
            return self.arr

        pivot = self.arr[left_index]
        lt = left_index   # 小于pivot的右边界
        gt = right_index  # 大于pivot的左边界
        i = left_index    # 遍历指针

        while i <= gt:
            if self.arr[i] < pivot:
                self.arr[i], self.arr[lt] = self.arr[lt], self.arr[i]
                lt += 1
                i += 1
            elif self.arr[i] > pivot:
                self.arr[i], self.arr[gt] = self.arr[gt], self.arr[i]
                gt -= 1
            else:
                i += 1

        self.three_way_sort(left_index, lt - 1)
        self.three_way_sort(gt + 1, right_index)
        return self.arr

# 测试
if __name__ == "__main__":
    test_arr = [4, 8, 4, 8, 1, 1, 4, 8, 4]
    qs = QuickSort(test_arr)
    print("原始数组：", test_arr)
    print("三路快排结果：", qs.three_way_sort())
