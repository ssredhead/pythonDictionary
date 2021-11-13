from linked_list import LinkedList, Node

linked_list_a = LinkedList()
linked_list_b = LinkedList()
linked_list_a.add('z')
linked_list_a.add('x')
linked_list_a.add('c')
linked_list_a.add('a')
linked_list_b.add('u')
linked_list_b.add('g')
linked_list_b.add('b')

# Given two sorted linked lists as input, your function should return
# a single sorted linked list made up of the nodes from both inputs.
# linked_list_a = a -> c -> x -> z
# linked_list_b = b -> g -> u

# One way to solve this problem would be reassigning .next for each node in both lists. 
# This approach is a constant space solution because we’re combining the inputs rather 
# than creating a new linked list. In the above example, we would start by setting 'a' node’s .next 
# property to the 'b' node.

# Another way would be to create a new linked list. 
# In the example, the head node of our new linked list would be 'a' node. <- what I did
def merge(linked_list_a, linked_list_b):
    current_a = linked_list_a.head
    current_b = linked_list_b.head

    if current_a.val < current_b.val: #get the smallest head node to start our new list
        start = current_a
        current_a = current_a.next
    else:
        start = current_b
        current_b = current_b.next
  
    #Store that head node so we can use it to initialize our return instance of LinkedList. 
    #We’re storing another reference because we’ll overwrite start_node repeatedly 
    #as we build out the list.
    head = start 

    while current_a or current_b: #account for different lengths of a and b
        if not current_a: #make sure there is a next node, if not, b is the only option
            start.next = current_b
            current_b = current_b.next
        elif not current_b:
            start.next = current_a
            current_a = current_a.next
        elif current_a.val < current_b.val: #if both lists have nexts, choose the smaller of the two
            start.next = current_a
            current_a = current_a.next
        else:
            start.next = current_b
            current_b = current_b.next
        start = start.next #move start to the next node to keep the list moving

    # Finally, we’ll use the reference to the new head to return a new LinkedList instance.
    return LinkedList(head)

merged_linked_list = merge(linked_list_a, linked_list_b)

print("Merged list should contain all nodes in sorted order: a -> b -> c -> g -> u -> x -> z")
print("Your function returned: {0}".format(merged_linked_list))