from collections import deque
from collections import defaultdict

class Solution(object):
    def sumOfDistancesInTree(self, n, edges):
        graph = defaultdict(set)
        for u, v in edges:
            graph[u].add(v)
            graph[v].add(u)

        count = [1] * n  # 서브트리 크기
        result = [0] * n

        # 1st pass: post-order → count[], result[0]
        def dfs1(node, parent):
            for child in graph[node]:
                if child != parent:
                    dfs1(child, node)
                    count[node] += count[child]
                    result[node] += result[child] + count[child]

        # 2nd pass: pre-order → 나머지 result[]
        def dfs2(node, parent):
            for child in graph[node]:
                if child != parent:
                    result[child] = result[node] - count[child] + (n - count[child])
                    dfs2(child, node)

        dfs1(0, -1)
        dfs2(0, -1)
        return result