# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visited = set()
        p = head

        while p is not None:
            if p not in visited:
                visited.add(p)
            else:
                return True
            
            p = p.next
        
        return False

        