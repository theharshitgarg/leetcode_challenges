# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def get_linked_list(arr):
	lst = None
	for key, val in enumerate(arr):
		new_node = ListNode(val)
		if lst:
			new_node.next = lst
		lst = new_node

	return lst

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = None
        carry = 0
        temp = l1
        tail = None
        while l1 and l2:
            n_sum = (l1.val+l2.val+carry)%10
            carry = (l1.val+l2.val+carry)/10
            new_node = ListNode(n_sum)
            if not head:
                head = new_node
                tail = new_node
            else:
                tail.next = new_node
                tail = new_node
            l1 = l1.next
            l2 = l2.next

        remaining = l1 or l2
        while remaining:
            n_sum = (remaining.val+carry)%10
            carry = (remaining.val+carry)/10            
            new_node = ListNode(n_sum)
            if not head:
                head = new_node
                tail = new_node
            else:
                tail.next = new_node
                tail = new_node
            
            remaining = remaining.next

        if carry:
            new_node = ListNode(carry)
            if not head:
                head = new_node
                tail = new_node
            else:
                tail.next = new_node
                tail = new_node
            
        return head

def print_list(head):
    while head:
        print head.val
        head = head.next

sol = Solution()
print_list(sol.addTwoNumbers(get_linked_list([2,4,3]), get_linked_list([5,6,4])))
print_list(sol.addTwoNumbers(get_linked_list([1,2,3]), get_linked_list([1,2,3])))
print_list(sol.addTwoNumbers(get_linked_list([2,4,3]), get_linked_list([5,6,4])))
print_list(sol.addTwoNumbers(get_linked_list([1,8]), get_linked_list([0])))