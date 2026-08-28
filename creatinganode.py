class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def printLinkedList(head):
    current = head

    while current:
        print(current.data)
        current = current.next


# Input
n = int(input())

head = None
tail = None

for i in range(n):
    data = int(input())

    new_node = Node(data)

    if head is None:
        head = new_node
        tail = new_node
    else:
        tail.next = new_node
        tail = new_node


# Print linked list
printLinkedList(head)