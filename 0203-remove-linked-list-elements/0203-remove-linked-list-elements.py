# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        # values = []
        # temp = head

        # while temp:
        #     if temp.val != val:
        #         values.append(temp.val)

        #     temp = temp.next
        # dummy = ListNode(0)
        # curr = dummy
        # for v in values:
        #     curr.next = ListNode(v)
        #     curr = curr.next
        # return dummy.next

        dummy = ListNode(0)
        dummy.next = head

        temp = dummy

        while temp.next:
            if temp.next.val == val:
                temp.next = temp.next.next
            else: temp = temp.next
        return dummy.next