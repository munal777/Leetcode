# Definition of a Node in a singly linked list 
class Node:
    def __init__(self, data):
       # Data part of the node
        self.data = data   
        # Pointer to the next node
        self.next = None

# Function to traverse and print list elements (recursive)
def traverseList(head):
    if head is None:
        return
    print(head.data, end=' ')
    traverseList(head.next)

# Function to search an element in the linked list
def searchElement(head,value):
    while head is not None:
        if head.data == value:   # Element found
            return True
        head = head.next
    return False                 # Element not found

# Function to count the length of linked list
def countlength(head):
    current = head
    length = 0
    while current is not None:
        length += 1
        current = current.next
    return length

# Function to insert a node at the beginning
def InsertInBegin(head, data):
    current = Node(data)
    current.next = head
    return current   # New head

# Function to insert a node at the end (recursive)
def InsertInEnd(head, data):
    if head is None:               # Empty list case
        return Node(data)
    if head.next is None:          # Last node found
        head.next = Node(data)
    else:
        InsertInEnd(head.next, data)
    return head

# Function to print the linked list iteratively
def print_list(head):
    current = head
    while current is not None:
        print(current.data, end= ' ')
        current = current.next

def main():
    # Create initial linked list: 10 -> 20 -> 30 -> 40
    head = Node(10)
    head.next = Node(20)
    head.next.next = Node(30)
    head.next.next.next = Node(40)

    print("orginal list:-")
    print_list(head)

    # Insert at beginning
    print('\n')
    print('Insert in Begin:-')
    head = InsertInBegin(head, 5)
    print_list(head)

    # Insert at end
    print('\n')
    print('Insert in End:-')
    head = InsertInEnd(head, 55)
    print_list(head)

    # Search an element
    print('\n')
    searched_data = searchElement(head, 10)
    print(searched_data)

    # Count size of list
    print('\n')
    print(f'size of list: {countlength(head)}')
    

# Run main function
if __name__ == "__main__":
    main()
