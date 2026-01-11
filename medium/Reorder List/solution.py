# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: None Do not return anything, modify head in-place instead.
        """

        # idea: Split the list in halves using fast & slow pointers
        # Reverse the second half.
        # Merge 2 halves together.

        slow = fast = head
        while slow.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        # 1 -> 2 -> 3 ------  X  ---------> 4 -> 5 -> 6
        #           ^                       ^
        #          slow --disconnect----second_half_head

        second_half_head = slow.next
        # disconnect 2 halves
        slow.next = None

        # Reverse second half and return the head of the
        # reversed linked list.
        reversed_second_half_head = self.reverseSingleLinkedList(second_half_head)
        first_half_head = head
        self.mergeTwoLinkedList(first_half_head, reversed_second_half_head)

    # Helper method to reverse the second half
    # Return the head of the reversed linked list.
    def reverseSingleLinkedList(self, head):
        prev = None
        current = head
        while current:
            # Save next node for next iteration
            save_next_node = current.next
            # Update next for the current node
            current.next = prev
            # Update prev to be the current node
            prev = current
            # Next iteration
            current = save_next_node

        return prev

    # Helper to merge 2 linked list alternately.
    # List1: 1 -> 2 -> 3
    # List2: 4 -> 5 -> 6
    # Final: 1 -> 4 -> 2 -> 5 -> 3 -> 6

    def mergeTwoLinkedList(self, head1, head2):
        while head2:
            save_next_head1 = head1.next
            save_next_head2 = head2.next

            head1.next = head2
            head2.next = save_next_head1

            head1 = save_next_head1
            head2 = save_next_head2
