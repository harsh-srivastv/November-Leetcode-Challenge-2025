class Solution:
    def processQueries(self, c: int, connections: List[List[int]], queries: List[List[int]]) -> List[int]:
        uf = UnionFind(c+1)
        for a, b in connections:
            uf.union(a, b)

        groups = defaultdict(deque)
        for i in range(1, c+1):
            groups[uf.find(i)].append(i)

        online = [True] * (c+1)
        ans = []
        for q_type, x in queries:
            if q_type == 2:
                online[x] = False
                continue

            if online[x]:
                ans.append(x)
                continue

            g = uf.find(x)
            q = groups[g]
            while q and not online[q[0]]:
                q.popleft()

            if q:
                ans.append(q[0])
            else:
                ans.append(-1)

        return ans


class UnionFind:
    def __init__(self, n):
        self.parent = [0] * n
        self.component_cnt = n 
        for i in range(n):
            self.parent[i] = i

    def union(self, x, y):
        px = self.find(x)
        py = self.find(y)
        if px != py:
            self.parent[px] = py
            self.component_cnt -= 1

    def find(self, x):
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]