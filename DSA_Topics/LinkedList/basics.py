# Definition of a Node in a singly linked list
class Node:
    def __init__(self, data):
       # Data part of the node
        self.data = data   
        self.next = None

def traverseList(head):
    if head is None:
        print()
        return
    
    print(head.data, end=' ')

    traverseList(head.next)


def searchElement(head,value):

    while head is not None:
        if head.data == value:
            return True
        
        head = head.next
    return False


def main():

    head = Node(10)
    head.next = Node(20)
    head.next.next = Node(30)

    # traverseList(head)
    result = searchElement(head, 50)

    print("yes" if result else "no")

if __name__ == "__main__":
    main()
