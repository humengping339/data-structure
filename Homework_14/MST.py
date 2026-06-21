import heapq
from collections import defaultdict

class Graph:
    def __init__(self, vertices):
        self.V = vertices  # 顶点数量
        self.graph = []    # 用于 Kruskal (存储边列表)
        self.adj_list = defaultdict(list) # 用于 Prim (存储邻接表)

    def add_edge(self, u, v, w):
        """添加无向带权边"""
        self.graph.append([w, u, v])
        self.adj_list[u].append((v, w))
        self.adj_list[v].append((u, w))

    # ================= Prim 算法 =================
    def prim_mst(self, start_node='A'):
        print(f"--- Prim 算法 (起始点: {start_node}) ---")
        mst_edges = []
        visited = set()
        min_heap = []
        total_cost = 0

        # 1. 将起始点加入堆
        visited.add(start_node)
        for neighbor, weight in self.adj_list[start_node]:
            heapq.heappush(min_heap, (weight, start_node, neighbor))

        while min_heap and len(visited) < self.V:
            weight, u, v = heapq.heappop(min_heap)

            if v not in visited:
                visited.add(v)
                mst_edges.append((u, v, weight))
                total_cost += weight

                # 将新加入顶点的邻居边加入堆
                for next_neighbor, next_weight in self.adj_list[v]:
                    if next_neighbor not in visited:
                        heapq.heappush(min_heap, (next_weight, v, next_neighbor))

        print(f"MST 边集合: {mst_edges}")
        print(f"总权值: {total_cost}\n")
        return total_cost

    # ================= Kruskal 算法 =================
    def kruskal_mst(self):
        print("--- Kruskal 算法 ---")
        mst_edges = []
        parent = {}
        rank = {}
        total_cost = 0

        # 初始化并查集
        # 从 graph 中提取所有顶点
        all_nodes = set()
        for _, u, v in self.graph:
            all_nodes.add(u)
            all_nodes.add(v)

        for node in all_nodes:
            parent[node] = node
            rank[node] = 0

        # 1. 按权重对边进行排序
        self.graph.sort(key=lambda item: item[0])

        # 2. 遍历排序后的边
        for weight, u, v in self.graph:
            root_u = self.find(parent, u)
            root_v = self.find(parent, v)

            # 如果两个顶点不在同一个集合中（不构成环），则选中该边
            if root_u != root_v:
                mst_edges.append((u, v, weight))
                total_cost += weight
                self.union(parent, rank, root_u, root_v)

        print(f"MST 边集合: {mst_edges}")
        print(f"总权值: {total_cost}\n")
        return total_cost

    # 并查集辅助函数：查找根节点（路径压缩）
    def find(self, parent, i):
        if parent[i] == i:
            return i
        parent[i] = self.find(parent, parent[i])
        return parent[i]

    # 并查集辅助函数：合并集合（按秩合并）
    def union(self, parent, rank, x, y):
        xroot = self.find(parent, x)
        yroot = self.find(parent, y)

        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
        else:
            parent[yroot] = xroot
            rank[xroot] += 1


# ================= 主程序执行 =================
if __name__ == "__main__":
    # 根据图片构建图：6个顶点 A-F
    g = Graph(6)

    # 录入图片中的边数据
    edges_data = [
        ('A', 'B', 2),
        ('A', 'D', 3),
        ('B', 'C', 4),
        ('B', 'E', 1),
        ('C', 'F', 5),
        ('D', 'E', 6),
        ('E', 'F', 2)
    ]

    for u, v, w in edges_data:
        g.add_edge(u, v, w)

    # 运行 Prim 算法
    g.prim_mst('A')

    # 运行 Kruskal 算法
    g.kruskal_mst()
