class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ans = ListNode(-1)
        cur = ans
        rf = 0
        while l1 is not None and l2 is not None:
            cur.next = ListNode()
            cur = cur.next
            val = l1.val + l2.val + rf
            if val >= 10:
                val = val - 10
                rf = 1
            else:
                rf = 0
            cur.val = val
            l1 = l1.next
            l2 = l2.next

        if l1 is None:
            l1 = l2
        while l1 is not None:
            cur.next = ListNode()
            cur = cur.next
            val = l1.val + rf
            if val >= 10:
                val = val - 10
                rf = 1
            else:
                rf = 0
            cur.val = val
            l1 = l1.next
        if rf:
            cur.next = ListNode(1)

        return ans.next


# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class Solution:
#     def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
#         carry = 0
#         head = l1
#         former = head
#         while l1:
#             if l2:
#                 tem = carry
#                 carry = (l1.val + l2.val + carry) // 10
#                 l1.val = (l1.val + l2.val + tem) % 10
#                 l2 = l2.next
#             else:
#                 tem = carry
#                 carry = (l1.val + carry) // 10
#                 l1.val = (l1.val + tem) % 10
#             former = l1
#             l1 = l1.next
#         while l2:
#             tem = carry
#             carry = (l2.val + carry) // 10
#             former.next = ListNode((l2.val + tem) % 10)
#             former = former.next
#             l2 = l2.next
#         if carry:
#             former.next = ListNode(carry)
#         return head
