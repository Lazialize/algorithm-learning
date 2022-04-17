import sys
from typing import List


class DFS:
    def __init__(self, node_number: int) -> None:
        self.seen = [False for _ in range(node_number)]
        self.todo = []
        self.node_number = node_number

    def initialize(self):
        self.seen = [False for _ in range(self.node_number)]
        self.todo = []

    def search(self, graph: List[List[int]], index: int):
        """深さ優先探索"""
        self.seen[index] = True

        for next_node_index in graph[index]:
            if self.seen[next_node_index]:
                continue
            self.search(graph, next_node_index)


sys.setrecursionlimit(200000)
N, M, s, t = map(int, input().split())

graph = [[] for _ in range(N)]

for _ in range(M):
    a, b = map(int, input().split())

    graph[a].append(b)
    graph[b].append(a)

dfs = DFS(N)
dfs.search(graph, s)

print("Yes" if dfs.seen[t] else "No")
