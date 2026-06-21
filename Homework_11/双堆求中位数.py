import heapq

class MedianFinder:
    def __init__(self):
        # left_heap 大顶堆(存负数)，保存前半部分小数
        self.left_heap = []
        # right_heap 小顶堆，保存后半部分大数
        self.right_heap = []

    def addNum(self, num: int) -> None:
        # 1. 先判断插入哪个堆
        if not self.left_heap or num <= -self.left_heap[0]:
            heapq.heappush(self.left_heap, -num)
        else:
            heapq.heappush(self.right_heap, num)

        # 2. 平衡两个堆的长度，差值不能超过1
        left_len = len(self.left_heap)
        right_len = len(self.right_heap)
        # 左堆过多，移最大元素到右堆
        if left_len - right_len > 1:
            val = -heapq.heappop(self.left_heap)
            heapq.heappush(self.right_heap, val)
        # 右堆过多，移最小元素到左堆
        elif right_len - left_len > 1:
            val = heapq.heappop(self.right_heap)
            heapq.heappush(self.left_heap, -val)

    def findMedian(self) -> float:
        left_len = len(self.left_heap)
        right_len = len(self.right_heap)
        # 总数奇数，取更长堆的堆顶
        if left_len > right_len:
            return -self.left_heap[0]
        elif right_len > left_len:
            return self.right_heap[0]
        # 总数偶数，两堆顶平均
        else:
            return (-self.left_heap[0] + self.right_heap[0]) / 2


# 作业测试示例
if __name__ == "__main__":
    mf = MedianFinder()
    mf.addNum(1)
    mf.addNum(2)
    print("当前中位数：", mf.findMedian())  # 输出1.5
    mf.addNum(3)
    print("当前中位数：", mf.findMedian())  # 输出2.0

    mf2 = MedianFinder()
    test_nums = [6, 1, 3, 5, 7, 2, 4]
    for n in test_nums:
        mf2.addNum(n)
        print(f"插入{n}，中位数={mf2.findMedian()}")
