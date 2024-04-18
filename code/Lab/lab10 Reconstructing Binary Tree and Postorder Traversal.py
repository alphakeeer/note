
'''
preorder    inorder     postorder
r->L->R     L->r->R     L->R->r
显而易见 1.前序的第一个元素即为树的根 2.前序与中序的右子树皆在末尾（虽然子树内顺序不同）
又 3.前序输出要求 左->右->根
则可以无需建树 直接通过深搜解决
思路:   1.找到根(preorder)->inorder根左侧皆为左子树,右侧为右子树
        2.先深搜左子树,后深搜右子树,最后输出根
        3.设置基准条件
over
'''

n = int(input())
preo = list(map(int, input().split()))
ino = list(map(int, input().split()))


def solution(preo, ino):
    # 基准条件
    if len(ino) == 0:
        return
    if len(ino) == 1:
        print(ino[0], end=" ")
        return
    # 根的值与index
    root = preo[0]
    index_root = -1
    # 深搜dfs
    for i in range(len(ino)):
        if ino[i] == root:
            index_root = i
    solution(preo[1:index_root+1], ino[0:index_root])
    solution(preo[index_root+1:], ino[index_root+1:])
    print(root, end=" ")


solution(preo, ino)
