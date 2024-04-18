'''
无技术含量
'''
class Node:
    def __init__(self) -> None:
        self.val = 0
        self.edge = set()


n = int(input())
tree = [Node() for _ in range(n+1)]

for i in range(n-1):
    a, b = map(int, input().split())
    tree[a].edge.add(b)
    tree[b].edge.add(a)

m = int(input())
for i in range(m):
    a, b = map(int, input().split())
    tree[a].val += b


def solution(root, val, parent):
    global tree
    son = tree[root].edge
    tree[root] = tree[root].val+val
    for i in son:
        if i == parent:
            continue
        solution(i, tree[root], root)


solution(1, 0, 0)
for i in range(1, n+1):
    print(tree[i], end=" ")
