'''
无技术含量
'''
tree=list(map(int,input().split()))
def solution(tree):
    ans=0
    n=len(tree)
    half=n//2
    for i in range(half):
        l=2*i+1
        r=2*i+2
        if l<n:
            ans+=tree[i]^tree[l]
        if r<n:
            ans+=tree[i]^tree[r]
    return ans
print(solution(tree))