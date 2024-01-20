# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        merged_list_node = ListNode()
        first_node = merged_list_node
        while list1 and list2:

            if list1.val < list2.val:
                merged_list_node.val = list1.val
                new_node = ListNode()
                merged_list_node.next = new_node
                merged_list_node = new_node
                list1 = list1.next

            elif list1.val > list2.val:
                merged_list_node.val = list2.val
                new_node = ListNode()
                merged_list_node.next = new_node
                merged_list_node = new_node
                list2 = list2.next

            elif list1.val == list2.val:
                merged_list_node.val = list1.val
                new_node = ListNode()
                merged_list_node.next = new_node
                merged_list_node = new_node
                list1 = list1.next

                merged_list_node.val = list2.val
                new_node = ListNode()
                merged_list_node.next = new_node
                merged_list_node = new_node
                list2 = list2.next
            
        if list1 and list2 == None:
                while list1:
                    merged_list_node.val = list1.val
                    new_node = ListNode()
                    merged_list_node.next = new_node
                    merged_list_node = new_node
                    list1 = list1.next
                return first_node
        elif list2 and list1 == None:
            while list2:
                merged_list_node.val = list2.val
                new_node = ListNode()
                merged_list_node.next = new_node
                merged_list_node = new_node
                list2 = list2.next
            return first_node
        else:
            return first_node
