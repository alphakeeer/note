class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=' ')
            current = current.next
        print()

    def promote(self, p_data):
        if self.head == None:
            return
        cur = self.head
        pre = cur
        while cur != None:
            if cur.data != p_data:
                pre = cur
                cur = cur.next
                continue
            node = Node(p_data)
            node.next = self.head
            self.head = node
            pre.next = cur.next
            cur = cur.next

    def init(self, arr):
        self.head = Node(-1)
        cur = self.head
        for data in arr:
            node = Node(data)
            cur.next = node
            cur = cur.next
        self.head = self.head.next


arr = list(map(int, input().split()))
p = int(input())

ans = SinglyLinkedList()
ans.init(arr)
ans.promote(p)
ans.print_list()
