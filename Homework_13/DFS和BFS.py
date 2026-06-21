from collections import deque

class Graph:
    def __init__(self):
        self.adj = {
            'A': ['B', 'C'],
            'B': ['A', 'D'],
            'C': ['A', 'D', 'E'],
            'D': ['B', 'C', 'E'],
            'E': ['C', 'D']
        }

    # 深度优先 DFS
    def dfs(self, start):
        visited = set()
        res = []
        def dfs_helper(node):
            visited.add(node)
            res.append(node)
            # 按字母顺序遍历邻接点
            for neighbor in self.adj[node]:
                if neighbor not in visited:
                    dfs_helper(neighbor)
        dfs_helper(start)
        return res

    # 广度优先 BFS
    def bfs(self, start):
        visited = set()
        q = deque([start])
        visited.add(start)
        res = []
        while q:
            cur = q.popleft()
            res.append(cur)
            for neighbor in self.adj[cur]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    q.append(neighbor)
        return res

if __name__ == "__main__":
    g = Graph()
    print("DFS遍历序列：", " → ".join(g.dfs('A')))
    print("BFS遍历序列：", " → ".join(g.bfs('A')))
