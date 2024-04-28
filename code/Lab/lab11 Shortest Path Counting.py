import queue
# 数据记录与建图
modulo = 100003
n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


def solution(n, modulo, graph):
    dist = [float('inf')]*(n+1)  # 最短路径经过的节点数
    dist[1] = 0
    paths = [0]*(n+1)            # 最短路径数目
    paths[1] = 1
    que = queue.Queue()
    que.put(1)
    while not que.empty():
        cur = que.get()
        son = graph[cur]
        for i in son:
            if dist[i] > dist[cur]+1:   #当子结点的距离大于现结点+1时更新
                dist[i] = dist[cur]+1
                paths[i] = paths[cur]
                paths[i] %= modulo
                que.put(i)
            elif dist[i] == dist[cur]+1:#当刚好相连时增加path
                paths[i] += paths[cur]
                paths[i] %= modulo
    return paths


ans = solution(n, modulo, graph)
for i in range(1, n+1):
    print(ans[i])


# from collections import deque

# n, m = map(int, input().split())
# li = [[] for _ in range(n + 1)]
# for _ in range(m):
#     a, b = map(int, input().split())
#     li[a].append(b)
#     li[b].append(a)

# def bfs(li, n):
#     ans = [0] * (n + 1)
#     ans[1] = 1
#     dis = [float('inf')] * (n + 1)
#     dis[1] = 0
#     queue = deque([1])
#     while queue:
#         node = queue.popleft()
#         for neighbor in li[node]:
#             if dis[neighbor] == float('inf'):
#                 dis[neighbor] = dis[node] + 1
#                 ans[neighbor] = ans[node]
#                 queue.append(neighbor)
#             elif dis[neighbor] == dis[node] + 1:
#                 ans[neighbor] += ans[node]
#     return ans[1:]

# result = bfs(li, n)
# for i in result:
#     print(i)


'''
5 7
1 2
1 3
2 4
3 4
2 3
4 5
4 5

'''
'''
9 12
1 2
1 3
2 4
2 5
3 6
4 5
4 7
4 7
5 6
6 8
7 9
8 9

'''


# def find_shortest_paths(N, edges):
#     from collections import deque, defaultdict

#     # Create graph
#     graph = [[]for _ in range(N+1)]
#     for x, y in edges:
#         graph[x].append(y)
#         graph[y].append(x)  # undirected graph

#     # BFS to find shortest paths
#     queue = deque([(1, 0)])  # (node, distance)
#     visited = {i: False for i in range(1, N + 1)}
#     visited[1] = True
#     distances = [-1] * (N + 1)
#     paths = [0] * (N + 1)
#     distances[1] = 0
#     paths[1] = 1

#     while queue:
#         node, dist = queue.popleft()
#         for neighbor in graph[node]:
#             if not visited[neighbor]:
#                 visited[neighbor] = True
#                 distances[neighbor] = dist + 1
#                 paths[neighbor] = paths[node]
#                 queue.append((neighbor, dist + 1))
#             elif dist + 1 == distances[neighbor]:
#                 paths[neighbor] = (paths[neighbor] + paths[node]) % 100003

#     return paths[1:]


# edges = []
# N, m = map(int, input().split())
# for i in range(m):
#     a, b = map(int, input().split())
#     edges.append((a, b))
# # Calling the function with the example graph
# ans=(find_shortest_paths(N, edges))
# for i in ans:
#     print(i)
