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

def main():

    head = Node(10)
    head.next = Node(20)
    head.next.next = Node(30)

    traverseList(head)

if __name__ == "__main__":
    main()

