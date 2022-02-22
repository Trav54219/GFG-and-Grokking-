#Doubly Linked List Class and traversal 
class Node:

    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


def printDll(head):
    curr = head
    while curr != None:
        print(curr.data, end=" ")
        curr = curr.next
    print()


head = Node(10)
temp1 = Node(20)
temp2 = Node(30)

head.next = temp1
temp1.prev = head

temp1.next = temp2
temp2.prev = temp1

printDll(head)


print("----------------------------------------")
#Insert at the beginning of a doubly Linked List 
class Node:

    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


def insertBegin(head, x):
    temp = Node(x)

    if head != None:
        head.prev = temp
    temp.next=head
    temp.prev = head

    return temp


def printDll(head):
    curr = head
    while curr != None:
        print(curr.data, end=" ")
        curr = curr.next
    print()


head = Node(10)
temp1 = Node(20)
temp2 = Node(30)

head.next = temp1
temp1.prev = head

temp1.next = temp2
temp2.prev = temp1

printDll(head)

head = insertBegin(head, 40)

printDll(head)


print("-----------------------------------")
#Insert at the beginning of a doubly Linked List 
class Node:

    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


def insertEnd(head,x):

    temp = Node(x)

    if head == None:
        return temp

    else:

        curr = head
        while curr.next != None:
            curr = curr.next

        curr.next = temp
        temp.prev = curr

        return head


def printDll(head):
    curr = head
    while curr != None:
        print(curr.data, end=" ")
        curr = curr.next
    print()


head = Node(10)
temp1 = Node(20)
temp2 = Node(30)

head.next = temp1
temp1.prev = head

temp1.next = temp2
temp2.prev = temp1

printDll(head)

head = insertEnd(head, 40)

printDll(head)


print("-----------------------------------")
#Delete head of a doubly Linked List 