# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # pointer1 = head
        # pointer2 = head

        # count = 0

        # while pointer1:

        #     count = count + 1
        #     pointer1 = pointer1.next
        # mid = count // 2

        # for i in range(mid):
        #     print("i",i)
        #     pointer2 = pointer2.next
        # return pointer2

        # tortoise and hare 
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        return slow  