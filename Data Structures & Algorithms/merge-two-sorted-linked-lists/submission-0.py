# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    '''
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 == None and list2 == None:
            return None
        if list1 == None:
            return list2
        if list2 == None:
            return list1

        curr = None
        head = None
        p1 = list1
        p2 = list2

        while p1 != None or p2 != None:
            if p1 == None:
                while p2 != None:
                    curr.next = p2
                    p2 = p2.next
                break
            if p2 == None:
                while p1 != None:
                    curr.next = p1
                    p1 = p1.next
                break
            
            if p1.val >= p2.val:
                if curr == None:
                    curr = p2
                    head = p2
                    p2 = p2.next
                else:
                    curr.next = p2
                    p2 = p2.next
            else:
                if curr == None:
                    curr = p1
                    head = p1
                    p1 = p1.next
                else:
                    curr.next = p1
                    p1 = p1.next
        return head
    '''
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 == None and list2 == None:
            return None
        if list1 == None:
            return list2
        if list2 == None:
            return list1


        p1 = list1
        p2 = list2
        curr = ListNode(0, None)
        head = curr

        while p1 != None or p2 != None:
            if p1 == None:
                while p2 != None:
                    curr.next = p2
                    curr = curr.next
                    p2 = p2.next
                break
            
            if p2 == None:
                while p1 != None:
                    curr.next = p1
                    curr = curr.next
                    p1 = p1.next
                break

            if p1.val <= p2.val:
                curr.next = p1
                curr = curr.next
                p1 = p1.next
            else:
                curr.next = p2
                curr = curr.next
                p2 = p2.next
        
        return head.next

        
    


