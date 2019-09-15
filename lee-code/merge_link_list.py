# Definition for singly-linked list.
from typing import List


class ListNode:
   def __init__(self, x):
       self.val = x
       self.next = None

def get_linked_list(l : List) -> ListNode:
    node = ListNode(-1)
    root = node
    for i in range(len(l)):
        node.next = ListNode(l[i])
        node = node.next
    return root.next

def print_linked_list(l : list):
    while l is not None:
        print(l.val)
        l = l.next


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        result = ListNode(0)
        self.mergeLoop(lists, result)
        return result.next

    def mergeLoop(self, lists, result):
        min_val = -1
        min_index = 0
        none_count = 0

        for i in range(len(lists)):
            if lists[i] is None:
                none_count = none_count + 1
                continue

            if lists[i].val < min_val or min_val == -1:
                min_val = lists[i].val
                min_index = i

        if none_count == len(lists):
            return

        print(min_val)
        result.next = ListNode(min_val)
        lists[min_index] = lists[min_index].next
        self.mergeLoop(lists, result)

list1 = [1,3,4,7,9]
list2 = [2,4,6,8,10]
list3 = [6,10,11,56,100]
lists = [get_linked_list(list1), get_linked_list(list2), get_linked_list(list3)]
# print_linked_list(get_linked_list(list1))

solution = Solution()
result = solution.mergeKLists(lists)
