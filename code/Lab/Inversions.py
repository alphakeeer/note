# def merge(l,r):
#     ans=[]
#     i=j=val=0
#     while i<len(l) and j<len(r):
#         if l[i]<=r[j]:
#             ans.append(l[i])
#             i+=1
#         else:
#             ans.append(r[j])
#             j+=1
#             val+=len(l)-i
#     ans.extend(l[i:])
#     ans.extend(r[j:])
#     return ans,val
    

# def merge_sort(arr):
#     if len(arr)<=1:
#         return arr,0
#     mid=len(arr)//2
#     l,lv=merge_sort(arr[:mid])
#     r,rv=merge_sort(arr[mid:])
    
#     ans,val=merge(l,r)
#     total=lv+rv+val
#     return ans,total



# n = int(input())
# arr = list(map(int, input().split()))
# _,ans=merge_sort(arr)


    


        
    
                
            
                
    