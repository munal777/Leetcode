class Node:
    
    def __init__(self, data):
        self.data = data
        self.next = None
    
def print_list(head):

    while head is not None:
        print(head.data)

        head = head.next

def main():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)

    print_list(head)

if __name__ == '__main__':
    main()
