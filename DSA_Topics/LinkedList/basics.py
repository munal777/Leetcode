# Definition of a Node in a singly linked list
class Node:
    def __init__(self, data):
       # Data part of the node
        self.data = data   
        self.next = None

def traverseList(head):
    if head is None:
        return
    
    print(head.data, end=' ')

    traverseList(head.next)


def searchElement(head,value):

    while head is not None:
        if head.data == value:
            return True
        
        head = head.next
    return False

def countlength(head):
    current = head
    length = 0
    while current is not None:
        length += 1
        current = current.next
    
    return length


def InsertInBegin(head, data):
    current = Node(data)
    current.next = head

    return current

def InsertInEnd(head, data):
    
    if head is None:
        return Node(data)
    
    if head.next is None:
        head.next = Node(data)
    else:
        InsertInEnd(head.next, data)
    
    return head

def print_list(head):

    current = head

    while current is not None:
        print(current.data, end= ' ')

        current = current.next

def main():

    head = Node(10)
    head.next = Node(20)
    head.next.next = Node(30)
    head.next.next.next = Node(40)
    

if __name__ == "__main__":
    main()
