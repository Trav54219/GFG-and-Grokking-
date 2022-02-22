#Linked List vs Array 
# Array is a contigupus data structure

    #The idea is to drop the contiguous memory requirement so insert/delete can happen faster
    #Linked List is a Linear data Structure

#Arrays advantages and disadtvantages
#Arrays
    #Cache Friendly
    #Random Access
    
#LinkedLists
    #Cache Friendly 
    #No Random Access


#Implementation of Linked list 

#Node Class
class Node:
    def __init__(self, k):
        self.key = k
        self.next = None


temp1 = Node(10)
temp2 = Node(20)
temp3 = Node(30)

temp1.next = temp2
temp2.next = temp3

head = temp1
print(head.key)
print(head.next.key)
print(head.next.next.key)


#Applications of LinkedList 
    #Worst case insertion in beginning and end are O(1)
    #Worst case deletion from the beginning is O(1)
    #Insertions and deletions in the middle are if you have a reference to the previous node 
    #Round robin Implementation 
    #Merging two sorted Linked Lists is faster 


#Traversing through a Linked List 
    
    
def printList(head):
    curr = head
    while curr!= None:
        print(curr.key, end=" ")
        curr = curr.next


head = Node(10)
head.next = Node(20)
head.next.next = Node(15)
head.next.next.next = Node(30)
printList(head)



#Search in Linked List 
def search(head, x):
    pos=1
    curr=head
    while curr != head:
        if curr.key == x:
            return pos
        pos=pos+1
        curr=curr.next
    
    return -1


#Insert at the beginning of a LinkedList 
def insertBegin(head, key):
    temp=Node(key)
    temp.next=head
    return temp


#Insert at the end of a Linked List 
def insertend(head, key):
    if head==None:
        return Node(key)
    curr=head
    while curr.next != None:
        curr = curr.next 
    curr.next=Node(key)
    return head 

#Delete First Node of a Linked List Python 
class Node2:
    def __init__(self, k):
        self.key = k
        self.next = None


    def delFirst(head):
        if head == None:
            return None
        else:
            return head.next


    def printList(head):
        curr = head
        while curr != None:
            print(curr.key, end=" ")
            curr = curr.next
        print()


head = Node2(10)
head.next = Node2(20)
head.next.next = Node2(30)
head.next.next.next = Node2(40)

printList(head)

head = delFirst(head)

printList(head)

