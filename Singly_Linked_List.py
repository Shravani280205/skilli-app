class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def solution():
    # 1. Create Linked List
    head = Node(10)
    node2 = Node(20)
    node3 = Node(30)
    node4 = Node(40)

    new_node = Node(25)

    head.next = node2
    node2.next = node3
    node3.next = node4

    # 2. Traverse and Print Values in Linked List
    print("Linked List:")
    current = head
    while current is not None:
        print(current.data, end= " -> ")
        current = current.next
    print("None")

    # 3. Insert Node at a Specific Position 
    current = head
    print("Insert Node at a Specific Position :")

    while current is not None and current.data != 20:
        current = current.next
    # if current is not None:
    new_node.next = current.next
    current.next = new_node

    current = head

    while current:
        print(current.data, end = " -> ")
        current =  current.next
    print("None")

    # 4. Find Middle Node

    n = 0
    current = head
    while current is not None:
        n += 1
        current = current.next

    current = head
    for i in range(0, n//2):
        current = current.next
    print("Middle node:", current.data)

    # 5.a. Delete Node at a Beginning
    if head is not None:
        head = head.next

    current = head
    print("Delete First Node :")
    while current is not None:
        print(current.data, end = " -> ")
        current = current.next
    print("None")

    # 5.b. Delete Node at End
    current = head
    print("Delete last Node :")
    while current.next.next is not None:
        current = current.next
    current.next = None

    current = head
   
    while current is not None:
        print(current.data, end = " -> ")
        current = current.next
    print("None")

    # 5.c. Delete Node at a Specific Postiion
    current = head
    print("Delete Node at a Specific Position :")
    while current.next.data != 30:
        current = current.next
    current.next = current.next.next

    current = head
   
    while current is not None:
        print(current.data, end = " -> ")
        current = current.next
    print("None")

    # 6 Reverse Linked List
    current = head
    prev = None
    print("Reverse Linked List :")
    while current is not None:
        front = current.next
        current.next = prev
        prev = current
        current = front

    head = prev

    current = head

    while current is not None:
        print(current.data, end = " -> ")
        current = current.next
    print("None")

    # Sum of Every Two Consecutive Node Values
    current = head
    print("Sum of Two  Consecutive Node Values in Linked List :")
    while current is not None and current.next is not None:
        total = current.data + current.next.data
        print(current.data, "+", current.next.data, "=", total)
        current = current.next 
        
solution()