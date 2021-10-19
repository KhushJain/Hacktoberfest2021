import math
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
def getNode(data):
    new_node = Node(data)
    new_node.data = data
    new_node.next = None
    new_node.prev = None
    return new_node
def push(head_ref, new_node):
    new_node.prev = None
    new_node.next = head_ref
    if (head_ref != None):
        head_ref.prev = new_node
    head_ref = new_node
    return head_ref
def reverseList(head_ref):
    if (head_ref == None or
       (head_ref).next == None):
        return None
    new_head = None
    curr = head_ref
    while (curr != None):
        next = curr.next
        new_head = push(new_head, curr)
        curr = next
    head_ref = new_head
    return head_ref
def prList(head):
    while (head != None) :
        print(head.data, end = " ")
        head = head.next

if __name__=='__main__':
    head = None
    head = push(head, getNode(2));
    head = push(head, getNode(4));
    head = push(head, getNode(8));
    head = push(head, getNode(10));
    print("Original list: ", end = "")
    prList(head)
    head = reverseList(head)
    print("\nReversed list: ", end = "")
    prList(head)
