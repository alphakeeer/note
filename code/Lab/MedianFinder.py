import heapq


class MedianFinder():
    def __init__(self):
        self.down_h = []  # 记录小数，h1[0]是小数中最大数，其中数字均为负数
        self.up_h = []  # 记录大数，h2[0]是大数中最小数

    def add(self, val):
        if self.up_h and val>self.up_h[0]:
            heapq.heappush(self.up_h,val)
            if len(self.up_h)>len(self.down_h)+1:
                heapq.heappush(self.down_h,-heapq.heappop(self.up_h))
        else:
            heapq.heappush(self.down_h,-val)
            if len(self.down_h)> len(self.up_h)+1:
                heapq.heappush(self.up_h,-heapq.heappop(self.down_h))
                
        
        

    def show(self):
        print(self.down_h,' ',self.up_h)
        
    def median(self):
        if len(self.down_h)== len(self.up_h):
            print((self.up_h[0]-self.down_h[0])/2.0)
        else:
            print (self.up_h[0] if len(self.down_h)< len(self.up_h) else -self.down_h[0])

    
    
    
ans=MedianFinder()
while True:
    try:
        arr=list(input().split())
        if arr[0]=="add":
            ans.add(int(arr[1]))
        else:
            ans.median()
    except EOFError:
        break
# ans.add(10)
# ans.add(4)
# ans.add(3)
# ans.add(103)
# ans.add(80)
# ans.add(9)
# ans.add(6)
# ans.median()
# ans.show()