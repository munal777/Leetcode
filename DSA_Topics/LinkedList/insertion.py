class Node:
    def __init__(self, data):
        # Each node has two parts: data and a pointer to the next node
        self.data = data
        self.next = None
        

def InsertInSpecificPosition(head, position, data):
    # Create the new node to be inserted
    new_node = Node(data)

    # Case 1: Insert at the beginning (position = 1)
    if position == 1:
        new_node.next = head   # new node points to old head
        return new_node        # new node becomes the new head
    
    # Otherwise, traverse to the node just before the insertion point
    current = head
    current_position = 1

    while current is not None and current_position < position - 1:
        current = current.next       # move forward in the list
        current_position += 1

    # Link the new node into the chain
    new_node.next = current.next     # new node points to the next node
    current.next = new_node          # previous node points to new node

    return head   # return the unchanged head for reference


def print_list(head):
    # Traverse the list and print each node's data
    while head is not None:
        print(head.data)
        head = head.next


def main():
    # Create a simple linked list: 1 -> 2 -> 3
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)

    # Insert 100 at position 2: 1 -> 100 -> 2 -> 3
    head = InsertInSpecificPosition(head, 2, 100)
    print_list(head)


if __name__ == '__main__':
    main()
