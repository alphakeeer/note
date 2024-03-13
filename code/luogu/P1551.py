class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            self.parent[root_y] = root_x


n, m, p = map(int, input().split())
u = UnionFind(n+1)
for _ in range(m):
    a, b = map(int, input().split())
    u.union(a, b)
for _ in range(p):
    a, b = map(int, input().split())
    if u.find(a) == u.find(b):
        print("Yes")
    else:
        print("No")
