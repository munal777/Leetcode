# Definition for singly-linked list.

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def middleNode(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        length = 0

        while head is not None:
            length += 1
            print(head.val)
            head = head.next
        
        middle_len = length//2
        print(f"Middle Len: {middle_len}")


        # while head is not None:
        #     if length


head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)
head.next.next.next.next.next = ListNode(6)


obj = Solution()
obj.middleNode(head)
    



    
