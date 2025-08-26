class Node:
    
    def __init__(self, data):
        self.data = data
        self.next = None
    

def InsertInSpecificPosition(head, position, data):
    new_node = Node(data)

    if position == 1:
        new_node.next = head
        return new_node
    
    current = head
    current_position = 1

    while current is not None and current_position < position - 1:
        current = current.next 
        current_position += 1
    
    new_node.next = current.next
    current.next = new_node

    return head

def print_list(head):

    while head is not None:
        print(head.data)

        head = head.next

def main():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)

    head = InsertInSpecificPosition(head, 2, 100)
    print_list(head)


if __name__ == '__main__':
    main()
