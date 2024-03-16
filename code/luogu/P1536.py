class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.count = n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            self.parent[root_y] = root_x
            self.count -= 1


while True:
    data = input().split()
    if len(data) == 1 and int(data[0]) == 0:
        break
    n, m = map(int, data)
    uf = UnionFind(n)
    for _ in range(m):
        a, b = map(int, input().split())
        uf.union(a-1, b-1)
    print(uf.count - 1)
