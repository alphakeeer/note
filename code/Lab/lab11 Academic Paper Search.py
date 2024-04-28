'''
一半AC，一半WA
太怪了，决定不用脑子去想.jpg
'''
from collections import deque

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
for i in graph:
    i.sort()


def dfs(graph):
    ans = []
    vis = set()
    stack = [1]
    while stack:
        cur = stack.pop()
        if cur not in vis:
            vis.add(cur)
            ans.append(cur)
            stack.extend(sorted(graph[cur], reverse=True))
    return ans


def bfs(graph):
    ans = []
    vis = set()
    queue = deque([1])
    while queue:
        cur = queue.popleft()
        if cur not in vis:
            vis.add(cur)
            ans.append(cur)
            queue.extend(sorted(graph[cur]))
    return ans


d = dfs(graph)
b = bfs(graph)
print(" ".join(map(str, d)))
print(" ".join(map(str, b)))


# from collections import defaultdict, deque

# def makeGraph(citeRelation):
#     graph = defaultdict(list)
#     for x, y in citeRelation:
#         graph[x].append(y)
#         if y not in graph:  # Ensure all papers are in the graph, even if they cite no one
#             graph[y] = []
#     return graph

# def DFS(graph, start):
#     visited = set()
#     stack = [start]
#     result = []

#     while stack:
#         node = stack.pop()
#         if node not in visited:
#             visited.add(node)
#             result.append(node)
#             # Process neighbors in reverse order to maintain numerical order due to stack's LIFO nature
#             for neighbor in sorted(graph[node], reverse=True):
#                 if neighbor not in visited:
#                     stack.append(neighbor)

#     return result

# def BFS(graph, start):
#     queue = deque([start])
#     visited = set([start])
#     result = []

#     while queue:
#         node = queue.popleft()
#         result.append(node)
#         for neighbor in sorted(graph[node]):
#             if neighbor not in visited:
#                 visited.add(neighbor)
#                 queue.append(neighbor)

#     return result

# def main():
#     n, m = map(int, input().split())  # Read number of papers and citation relations
#     citeRelation = []
#     for i in range(m):
#         citeRelation.append(tuple(map(int, input().split())))  # Read citation relationships

#     graph = makeGraph(citeRelation)

#     # Assume we always start from paper numbered 1
#     if 1 in graph:
#         dfs_result = DFS(graph, 1)
#         bfs_result = BFS(graph, 1)
#         print(" ".join(map(str, dfs_result)))
#         print(" ".join(map(str, bfs_result)))
#     else:
#         print("1")
#         print("1")

# if __name__ == "__main__":
#     main()
