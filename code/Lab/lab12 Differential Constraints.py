
edges = []


def add_edge(edges, begin, end, weight):
    edges.append((begin, end, weight))


n, m = map(int, input().split())  # 数据读入
sources = [False for _ in range(n+1)]
for i in range(m):
    begin, end, weight = map(int, input().split())
    sources[end] = True
    add_edge(edges, begin, end, -weight)  # 边初始化

vertices = [float('-inf') for _ in range(n+1)]  # 点初始化
for i in range(1, n+1):
    if sources[i] == False:
        vertices[i] = 0


def bellmanFord(n, vertices, edges):
    flag = True
    for _ in range(n-1):
        flag = True
        for begin, end, weight in edges:
            if vertices[begin] != float('-inf') and vertices[begin] + weight > vertices[end]:
                flag = False
                vertices[end] = vertices[begin] + weight
        if flag:
            break

    return flag


if bellmanFord(n, vertices, edges):
    print('YES')
else:
    print('NO')
