class HashTable:
    """
    基于真实哈希函数实现的哈希表（链地址法解决冲突）
    核心功能：插入键值对、根据键查找值、删除键值对、查看哈希表结构
    """
    def __init__(self, capacity=10):
        """
        哈希表构造函数
        :param capacity: 哈希表初始容量（桶的数量，默认10）
        """
        # 哈希表容量：决定哈希地址的取值范围
        self.capacity = capacity
        # 初始化哈希表：用列表模拟哈希桶，每个桶是空链表（列表）
        self.hash_table = [[] for _ in range(self.capacity)]
        # 记录哈希表中有效键值对的数量
        self.size = 0

    def _hash_func(self, key):
        """
        【核心】真实哈希函数：调用Python内置hash()，再对容量取模得到合法哈希地址
        :param key: 哈希键（支持数字、字符串、元组等可哈希类型）
        :return: 哈希地址（0 ~ capacity-1）
        """
        # 第一步：用真实哈希函数计算key的哈希值
        raw_hash = hash(key)
        # 第二步：取模运算，将哈希值映射到哈希表的合法索引范围
        hash_address = raw_hash % self.capacity
        return hash_address

    def put(self, key, value):
        """
        向哈希表插入/修改键值对
        :param key: 键
        :param value: 值
        """
        # 1. 计算key对应的哈希地址
        hash_addr = self._hash_func(key)
        # 2. 定位到对应的哈希桶（链表）
        target_bucket = self.hash_table[hash_addr]

        # 3. 遍历链表，检查key是否已存在（存在则更新值）
        for index, (exist_key, exist_value) in enumerate(target_bucket):
            if exist_key == key:
                # 键已存在，更新对应的值
                target_bucket[index] = (key, value)
                return

        # 4. key不存在，在链表尾部追加新键值对，表长度+1
        target_bucket.append((key, value))
        self.size += 1

    def get(self, key):
        """
        根据键查找对应的值
        :param key: 要查找的键
        :return: 找到返回对应值，没找到返回None
        """
        # 1. 计算哈希地址
        hash_addr = self._hash_func(key)
        # 2. 定位目标哈希桶
        target_bucket = self.hash_table[hash_addr]

        # 3. 遍历链表查找key
        for exist_key, exist_value in target_bucket:
            if exist_key == key:
                return exist_value
        # 遍历完未找到，返回None
        return None

    def delete(self, key):
        """
        删除指定键的键值对
        :param key: 要删除的键
        :return: 删除成功返回True，键不存在返回False
        """
        # 1. 计算哈希地址
        hash_addr = self._hash_func(key)
        # 2. 定位目标哈希桶
        target_bucket = self.hash_table[hash_addr]

        # 3. 遍历链表查找并删除
        for index, (exist_key, exist_value) in enumerate(target_bucket):
            if exist_key == key:
                del target_bucket[index]
                self.size -= 1
                return True
        # 未找到要删除的键
        return False

    def print_table(self):
        """打印整个哈希表的结构（直观展示哈希桶和冲突情况）"""
        print("===== 哈希表结构 =====")
        for addr, bucket in enumerate(self.hash_table):
            print(f"哈希地址{addr}: {bucket}")
        print(f"哈希表总元素数量：{self.size}\n")


#  测试代码
if __name__ == "__main__":
    # 1. 创建哈希表对象（默认容量10）
    ht = HashTable()
    # 2. 插入键值对（包含会产生哈希冲突的键，测试冲突解决）
    ht.put("张三", 95)
    ht.put("李四", 88)
    ht.put("王五", 92)
    ht.put("张三", 98)   # 测试键已存在，更新值
    ht.put(1001, "学生A")
    ht.put(1002, "学生B")
    # 3. 打印哈希表结构
    ht.print_table()
    # 4. 测试查找功能
    print("查找键'张三'的值：", ht.get("张三"))
    print("查找键'不存在的键'的值：", ht.get("不存在的键"))
    # 5. 测试删除功能
    print("删除键'李四'：", ht.delete("李四"))
    ht.print_table()
