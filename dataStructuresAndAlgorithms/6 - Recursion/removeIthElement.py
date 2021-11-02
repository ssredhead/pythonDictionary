import LinkedList

# Definition for singly-linked list node.
# class ListNode:
#     def __init__(self, value, next_node=None):
#         self.value = value
#         self.next_node = next_node

# define remove_node()
def remove_node(head, i):
    #if i is negative, just return head
  if i < 0:
    return head
    #if the list is empty, return None
  if head is None:
    return None
    #if i is the current index, "remove" head by returning it's pointer to the next node
  if i == 0:
    return head.next_node

    #recursive case, move head to next_node and decrement i
  head.next_node = remove_node(head.next_node, i - 1)
  return head

# Test code - do not edit
gemstones = LinkedList.LinkedList(["Amber", "Sapphire", "Jade", "Pearl"])
head = remove_node(gemstones.head, 1)
print(head.flatten())
