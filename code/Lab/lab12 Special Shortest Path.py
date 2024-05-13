
'''
def Dijkstra(dist, adj_list):
    queue = deque([])
    queue.append(1)
    while queue:
        cur = queue.popleft()
        for son, cur_weight in adj_list[cur]:
            if dist[son] > dist[cur]+cur_weight:
                dist[son] = dist[cur]+cur_weight
                queue.append(son)
            for grandson, son_weight in adj_list[son]:
                if son_weight == k*cur_weight and dist[grandson] > dist[son]+(k-1)*cur_weight:
                    dist[grandson] = dist[son]+(k-1)*cur_weight
                    queue.append(grandson)
    return dist
'''


'''
def init(adj_list, n, k):
    vis = set()
    for cur in range(1, n+1):
        for son, cur_weight in adj_list[cur]:
            for grandson, son_weight in adj_list[son]:
                if son_weight == k*cur_weight and {cur, grandson} not in vis:
                    adj_list[cur].append((grandson, son_weight))
                    adj_list[grandson].append((cur, son_weight))
    return adj_list

adj_list = init(adj_list, n, k)

def Dijkstra(dist, adj_list):
    queue = []
    heapq.heappush(queue, (0, 1))
    while queue:
        cur_dist, cur = heapq.heappop(queue)
        if cur_dist != dist[cur]:
            continue
        for son, cur_weight in adj_list[cur]:
            if dist[son] > dist[cur]+cur_weight:
                dist[son] = dist[cur]+cur_weight
                heapq.heappush(queue, (dist[son], son))
    return dist
'''


from collections import deque
import heapq
n, m, k = map(int, input().split())  # n->node m->edge k->coefficience
adj_list = [[] for _ in range(n+1)]
for i in range(m):
    u, v, w = map(int, input().split())
    adj_list[u].append((v, w))
    adj_list[v].append((u, w))

dist = [float('inf') for _ in range(n+1)]
dist[1] = 0


# def Dijkstra(dist, adj_list, k):
#     queue = []
#     heapq.heappush(queue, (0, 1))
#     while queue:
#         cur_dist, cur = heapq.heappop(queue)
#         if cur_dist != dist[cur]:
#             continue
#         for son, cur_weight in adj_list[cur]:
#             if dist[son] > dist[cur]+cur_weight:
#                 dist[son] = dist[cur]+cur_weight
#                 heapq.heappush(queue, (dist[son], son))
#             for grandson, son_weight in adj_list[son]:
#                 if son_weight == k*cur_weight and dist[grandson] > dist[son]+(k-1)*cur_weight:
#                     dist[grandson] = dist[son]+(k-1)*cur_weight

#                     heapq.heappush(queue, (dist[grandson], grandson))
#     return dist


def Dijkstra(dist, adj_list):
    queue = []
    heapq.heappush(queue, (0, 1))
    while queue:
        cur_dist, cur = heapq.heappop(queue)
        if cur_dist != dist[cur]:
            continue
        for son, cur_weight in adj_list[cur]:
            if dist[son] > dist[cur]+cur_weight:
                dist[son] = dist[cur]+cur_weight
                heapq.heappush(queue, (dist[son], son))

    return dist


dist = Dijkstra(dist, adj_list)
for i in range(1, n+1):
    if dist[i] == float('inf'):
        print(-1, end=' ')
    else:
        print(dist[i], end=' ')
